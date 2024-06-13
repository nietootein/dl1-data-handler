import os
import sys
parent_directory = os.path.abspath('..')
sys.path.append(parent_directory)
from dl1_data_handler.dl1_data_handler.version import get_version_pypi

def get_version():
    return get_version_pypi()


if __name__ == "__main__":
    print(get_version())
