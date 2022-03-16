# imports
import os
import sys
import importlib

deps = importlib.import_module("dependency_list").deps

def check_deps():
    # get all package names
    pkgs = []
    path = sys.executable.split("python.exe")[0] + "Lib\\site-packages"
    for i in os.listdir(path):
        if i.endswith(".egg-info"):
            pkgs.append(i.split(".")[0])
        else:
            pkgs.append(i)

    for dep in deps:
        if dep not in pkgs:
            return False

    return True

if __name__ == "__main__":
    if check_deps():
        print("All dependencies are installed.")
    else:
        print("Some dependencies are missing.")
