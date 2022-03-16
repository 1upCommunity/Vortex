import dependency_checker
import dependency_installer
import dependency_updater
import logger

# check python version
import sys
if sys.version_info < (3, 6):
    logger.critical("Vortex", "Python version is too old. Please use python 3.6 or higher.")
    sys.exit(1)

# check dependencies
if not dependency_checker.check_deps():
    dependency_installer.install_deps()
    if not dependency_checker.check_deps():
        logger.warn("Vortex", "Dependencies are not installed. Please install them manually.")
        sys.exit(1)
else:
    dependency_updater.update_deps()

from rendering import *
import pyglet

window = VortexWindow()

pyglet.app.run()
