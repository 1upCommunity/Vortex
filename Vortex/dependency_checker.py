# internal imports
import logger

# external imports
import os
import sys
import importlib

deps = importlib.import_module("dependency_list").deps  # get dependency list


def check_deps():
    """
    check_deps

    Check if all dependencies are installed.

    return: bool
    """
    pkgs = []  # list of packages
    # get path to site-packages
    path = sys.executable.split("python.exe")[0] + "Lib\\site-packages"
    for i in os.listdir(path):  # loop through all files in site-packages
        if i.endswith(".egg-info"):  # if it is an egg-info file
            pkgs.append(i.split(".")[0])  # add the package name to the list
        else:  # if it is a folder
            pkgs.append(i)  # add the folder name to the list

    for dep in deps:  # loop through all dependencies
        if dep not in pkgs:  # if the dependency is not installed
            return False  # return false, exits the function

    return True  # return true if all dependencies are installed


if __name__ == "__main__":
    if check_deps():  # check for dependencies
        # if all dependencies are installed, log this
        logger.log("VortexDependencyManager",
                   "All dependencies are installed.")
    else:  # if not,
        logger.log("VortexDependencyManager",
                   "Some dependencies are missing.")  # log this
