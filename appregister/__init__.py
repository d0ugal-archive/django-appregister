# following PEP 386, versiontools will pick it up
__version__ = (0, 4, 0, "dev", 0)

from appregister.base import Registry, NamedRegistry, SortedRegistry

__all__ = ['__version__', 'Registry', 'NamedRegistry', 'SortedRegistry']
