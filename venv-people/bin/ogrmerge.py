#!/home/usmanghias/UsmanGhias/Mobile Application/Django Rest BackEnd/venv-people/bin/python

import sys
# import osgeo_utils.ogrmerge as a convenience to use as a script
from osgeo_utils.ogrmerge import *  # noqa
from osgeo_utils.ogrmerge import main
from osgeo.gdal import deprecation_warn


deprecation_warn('ogrmerge')
sys.exit(main(sys.argv))
