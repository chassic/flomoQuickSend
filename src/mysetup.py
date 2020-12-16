from distutils.core import setup
import py2exe

setup(windows=[{"script": "flomo.py", "icon_resources": [(1, u"flomo.ico")] }])
