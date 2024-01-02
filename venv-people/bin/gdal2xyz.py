#!/home/usmanghias/UsmanGhias/Mobile Application/Django Rest BackEnd/venv-people/bin/python

import sys
# import osgeo_utils.gdal2xyz as a convenience to use as a script
from osgeo_utils.gdal2xyz import *  # noqa
from osgeo_utils.gdal2xyz import main
from osgeo.gdal import deprecation_warn


deprecation_warn('gdal2xyz')
sys.exit(main(sys.argv))
