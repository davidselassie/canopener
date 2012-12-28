# -*- coding: utf-8 -*-

import bz2
import StringIO
import gzip

from mock import patch
import testify
from testify import TestCase
from testify import assert_raises

import canopener


class FileMock(StringIO.StringIO):
    def __init__(self, filename=None, mode=None):
        StringIO.StringIO.__init__(self, '')


@patch('__builtin__.open', FileMock)
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

# Becaue bz2 is implemented as a pure C module, we can't mock out stuff inside and test.

class GzipfileTestCase(CompressedFileTestCase):
    opener = canopener.gzfile
    expected_class = gzip.GzipFile


@patch('__builtin__.open', FileMock)
class CanopenerTestCase(TestCase):
    # Becaue bz2 is implemented as a pure C module, we can't mock out stuff inside.
    def test_bz2path(self):
        with patch('canopener.bz2file') as mock_bz2file:
            test_file = canopener.canopener('blahblah.bz2')
            # No way to test instance, since won't be a bz2file.
            test_file.close()
    
    def test_gzpath(self):
        test_file = canopener.canopener('blahblah.gz')
        assert isinstance(test_file, canopener.gzfile)
        test_file.close()

    def test_local(self):
        test_file = canopener.canopener('blahblah')
        assert isinstance(test_file, FileMock)
        test_file.close()

    @patch('canopener.urllib2.urlopen', FileMock)
    def test_url(self):
        test_file = canopener.canopener('http://blahblah/blah')
        assert isinstance(test_file, FileMock)
        test_file.close()

    def test_cant_write_url(self):
        with assert_raises(ValueError):
            canopener.canopener('http://blahblah/blah', 'w')


if __name__ == "__main__":
    testify.run()
