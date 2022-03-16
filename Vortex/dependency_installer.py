# imports
import os
import tqdm
import sys
import importlib

deps = importlib.import_module("dependency_list").deps
path = sys.executable

def install_deps():
    for dep in tqdm.tqdm(deps):
        os.system(f"{path} -m pip install {dep}")

if __name__ == '__main__':
    install_deps()
