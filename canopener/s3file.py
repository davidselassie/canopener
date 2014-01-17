# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import tempfile
import urlparse

from boto.s3.connection import S3Connection


def make_s3_connection(aws_access_key_id=None, aws_secret_access_key=None):
    """Mockable point for creating S3Connections."""
    return S3Connection(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


class s3file(object):
    def __new__(
        cls,
        filename,
        mode='r',
        aws_access_key_id=None,
        aws_secret_access_key=None,
    ):
        """Opens a local copy of an S3 URL."""
        parse = urlparse.urlparse(filename)
        if 'w' in mode:
            raise ValueError("can't write to S3")
        if parse.scheme != 's3':
            raise ValueError("s3file can't open non-S3 URLs")

        conn = make_s3_connection(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        bucket = conn.get_bucket(parse.netloc)
        key = bucket.get_key(parse.path)

        local_file = tempfile.TemporaryFile()
        key.get_contents_to_file(local_file)
        local_file.seek(0)
        return local_file
