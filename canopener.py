# -*- coding: utf-8 -*-

import bz2
import gzip


class WithMixin(object):
    """Gives a file-like object `with` powers."""

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

class bz2file(bz2.BZ2File, WithMixin):
    """Wrapper around bz2.BZ2File that imparts `with` powers.

    Only required in Python <= 2.6.
    """
    pass

class gzfile(gzip.GzipFile, WithMixin):
    """Wrapper around gzip.GzipFile that imparts `with` powers.

    Only required in Python <= 2.6.
    """
    pass


class canopener(file):
    """Convenience opener. Seamlessly decompresses .gz and .bz2 files."""

    def __new__(cls, filename, mode='r'):
        if filename.endswith('.gz'):
            return gzfile(filename, mode)
        elif filename.endswith('.bz2'):
            return bz2file(filename, mode)
        else:
            return cls(filename, mode)
