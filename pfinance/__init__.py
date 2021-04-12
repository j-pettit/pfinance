from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('pfinance')
except PackageNotFoundError:
    # package is not installed
    pass
