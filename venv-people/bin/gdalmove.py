#!/home/usmanghias/UsmanGhias/Mobile Application/Django Rest BackEnd/venv-people/bin/python

import sys
# import osgeo_utils.gdalmove as a convenience to use as a script
from osgeo_utils.gdalmove import *  # noqa
from osgeo_utils.gdalmove import main
from osgeo.gdal import deprecation_warn


deprecation_warn('gdalmove')
sys.exit(main(sys.argv))
