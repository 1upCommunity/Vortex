# external imports
import os
import tqdm
import sys
import importlib

deps = importlib.import_module("dependency_list").deps  # get dependency list
path = sys.executable  # get path to python


def install_deps():
    """
    install_deps

    Install all dependencies.

    return: None
    """
    for dep in tqdm.tqdm(deps):  # loop through all dependencies
        os.system(f"{path} -m pip install {dep}")  # install the dependency


if __name__ == '__main__':
    install_deps()  # install dependencies
