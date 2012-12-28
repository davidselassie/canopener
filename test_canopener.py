# -*- coding: utf-8 -*-

import bz2
import cStringIO
import gzip

from mock import patch
import testify
from testify import TestCase

import canopener


FILE_MOCK = lambda *args, **kwargs: cStringIO.StringIO('')


@patch('__builtin__.open', FILE_MOCK)
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
        test_file = self.opener(cStringIO.StringIO(''))
        assert isinstance(test_file, self.expected_class)
        test_file.close()

    def test_with_flo(self):
        with self.opener(cStringIO.StringIO('')) as test_file:
            assert isinstance(test_file, self.expected_class)

# Becaue bz2 is implemented as a pure C module, we can't mock out stuff inside and test.

class GzipfileTestCase(CompressedFileTestCase):
    opener = canopener.gzfile
    expected_class = gzip.GzipFile


@patch('__builtin__.open', FILE_MOCK)
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


if __name__ == "__main__":
    testify.run()
