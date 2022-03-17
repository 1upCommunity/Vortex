# imports
import os
import sys
import importlib
import tqdm
import pickle
import time
import logger

deps = importlib.import_module("dependency_list").deps
path = sys.executable

def update_deps():
    # if the pickle file exists, load it
    if os.path.isfile("last_update.pickle"):
        last_update = pickle.load(open("last_update.pickle", "rb"))
        if last_update < time.time() - 3600 * 12:
            logger.log("VortexDependencyManager", "Last update was more than 10 hours ago. Updating dependencies...")
            for dep in tqdm.tqdm(deps):
                os.system(f'{path} -m pip install --upgrade {dep}')
            pickle.dump(time.time(), open("last_update.pickle", "wb"))
        else:
            logger.log("VortexDependencyManager", "Dependencies are up to date.")
    else:
        for dep in tqdm.tqdm(deps):
            os.system(f'{path} -m pip install --upgrade {dep}')
        pickle.dump(time.time(), open("last_update.pickle", "wb"))

if __name__ == '__main__':
    update_deps()
