# -*- coding: utf-8 -*-

import tempfile
import urlparse

from boto.s3.connection import S3Connection

class s3file(object):
    def __new__(cls, filename, mode='r'):
        """Opens a local copy of an S3 URL.

        Requires the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment
        vars to be set.
        """
        parse = urlparse.urlparse(filename)
        if mode[0] != 'r':
            raise ValueError("can't write to S3")
        if parse.scheme != 's3':
            raise ValueError("s3file can't open non-S3 URLs")

        conn = S3Connection()
        bucket = conn.get_bucket(parse.netloc)
        key = bucket.get_key(parse.path)

        local_file = tempfile.TemporaryFile()
        key.get_contents_to_file(local_file)
        local_file.seek(0)
        return local_file
