from reader.compressed.bzipped import opener as bz2_opener
from reader.compressed.gzipped import opener as gz_opener

__all__ = ['bz2_opener', 'gz_opener']