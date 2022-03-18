# internal imports
import dependency_checker, dependency_installer, dependency_updater, logger
from rendering import *

# external imports
import pyglet, sys

# check if python version is too old. If it is, exit.
if sys.version_info < (3, 6): # if python version is less than 3.6
    logger.critical("Vortex", "Python version is too old. Please use python 3.6 or higher.")
    sys.exit(1)

# check all deps and update them if needed
if not dependency_checker.check_deps(): # if any deps are missing
    dependency_installer.install_deps() # install them
    if not dependency_checker.check_deps(): # if any deps are still missing
        logger.warn("Vortex", "Dependencies are not installed. Please install them manually.") # warn user and exit
        sys.exit(1)
else:
    dependency_updater.update_deps() # update deps

window = VortexWindow() # create the window
pyglet.app.run() # run the app 
