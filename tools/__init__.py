from os.path import dirname, basename, isfile
import glob
m = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in m if isfile(f) and not f.endswith('__init__.py')]

modules = ['tools.' + m for m in __all__]