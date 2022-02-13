"""
Package wide config constants
"""

import os
import enum

# Supported provincial codes
class ProvCode(enum.Enum):
    ALL = 0,
    ON = 1

# directory information
DATA_DIR_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
BINARIES_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'models', 'binaries')
CHECKPOINTS_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'models', 'checkpoints')

os.makedirs(BINARIES_PATH, exist_ok=True)
os.makedirs(CHECKPOINTS_PATH, exist_ok=True)