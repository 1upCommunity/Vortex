# internal imports
import logger

# external imports
import os
import sys
import importlib
import tqdm
import time

deps = importlib.import_module("dependency_list").deps
path = sys.executable


def save_stamp(number):
    """
    save_file

    Save the file.

    number: The number to save.

    return: None
    """
    os.environ.update({"VORTEX_DEPENDENCY_STAMP": str(number)})


def load_stamp():
    """
    load_file

    Load the file.

    return: None
    """
    return os.environ.get("VORTEX_DEPENDENCY_STAMP", "0")


def update_deps():
    if os.path.isfile("last_update.pickle"):
        last_update = load_stamp()
        if last_update < time.time() - 3600 * 12:
            logger.log("VortexDependencyManager",
                       "Last update was more than 10 hours ago. Updating dependencies...")
            for dep in tqdm.tqdm(deps):
                os.system(f'{path} -m pip install --upgrade {dep}')
            save_stamp(time.time())
        else:
            logger.log("VortexDependencyManager",
                       "Dependencies are up to date.")
    else:
        for dep in tqdm.tqdm(deps):
            os.system(f'{path} -m pip install --upgrade {dep}')
        save_stamp(time.time())


if __name__ == '__main__':
    update_deps()
