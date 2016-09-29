import pkg_resources

__title__ = 'marquee'
try:
    __version__ = pkg_resources.require('marquee')[0].version
except (AttributeError, pkg_resources.DistributionNotFound, IndexError):
    __version__ = 'unknown'
