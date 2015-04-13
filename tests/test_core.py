# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO
import gzip

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

try:
    import __builtin__ as builtins
except ImportError:
    import builtins

from unittest import TestCase
import pytest

from canopener import canopener
from canopener.core import gzfile


# We can't use cStringIO, since we're mocking out the constructor.
class FileMock(StringIO):
    def __init__(self, filename=None, mode=None):
        StringIO.__init__(self, '')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


@patch.object(builtins, 'open', FileMock)
class CompressedFileTestCase(TestCase):
    __test__ = False

    opener = None
    expected_class = None

    def test_open(self):
        test_file = self.opener('blahblah')
        assert isinstance(test_file, self.expected_class)
        test_file.close()

    def test_with(self):
        with self.opener('blahblah') as test_file:
            assert isinstance(test_file, self.expected_class)

    def test_open_flo(self):
        test_file = self.opener(FileMock())
        assert isinstance(test_file, self.expected_class)
        test_file.close()

    def test_with_flo(self):
        with self.opener(FileMock()) as test_file:
            assert isinstance(test_file, self.expected_class)


# Becaue bz2 is implemented as a pure C module, we can't mock out stuff
# inside and test.


class TestGzipfile(CompressedFileTestCase):
    opener = gzfile
    expected_class = gzip.GzipFile


@patch.object(builtins, 'open', FileMock)
class TestCanopener(TestCase):
    # Becaue bz2 is implemented as a pure C module, we can't mock out
    # stuff inside.
    @patch('canopener.core.bz2file', FileMock)
    def test_bz2path(self):
        with canopener('blahblah.bz2') as test_file:
            assert isinstance(test_file, FileMock)

    def test_gzpath(self):
        with canopener('blahblah.gz') as test_file:
            assert isinstance(test_file, gzfile)

    def test_local(self):
        with canopener('blahblah') as test_file:
            assert isinstance(test_file, FileMock)

    @patch('canopener.core.urlopen', FileMock)
    def test_url(self):
        with canopener('http://blahblah/blah') as test_file:
            assert isinstance(test_file, FileMock)

    def test_cant_write_url(self):
        with pytest.raises(ValueError):
            canopener('http://blahblah/blah', 'w')

    @patch('canopener.s3file.make_s3_connection', autospec=True)
    @patch('canopener.s3file.tempfile.TemporaryFile', FileMock)
    def test_s3_url(self, s3_conn_mock):
        with canopener('s3://blahblah/blah') as test_file:
            assert isinstance(test_file, FileMock)
