import dependency_checker
import dependency_installer

# check python version
import sys
if sys.version_info < (3, 6):
    print("Python version is too old. Please use python 3.6 or higher.")
    sys.exit(1)

# check dependencies
if not dependency_checker.check_deps():
    dependency_installer.install_deps()
    if not dependency_checker.check_deps():
        print("Dependencies are not installed. Please install them manually.")
        sys.exit(1)
