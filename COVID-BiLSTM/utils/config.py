"""
Package wide config constants
"""

import os
import enum

# Supported provincial codes
class ProvCode(enum.Enum):
    ALL = 0,
    ON = 1,
    AB = 2,
    BC = 3,
    MB = 4,
    QC = 5,
    SK = 6
    
# Supported location codes
class LocCode(enum.Enum):
    EGB = 0,
    HDA = 1,
    HHA = 2,
    HMC = 3,
    MMN = 4,
    MMS = 5, 
    TAB = 6,
    THC = 7, 
    THU = 8,
    TNT = 9,
    VAI = 10,
    VII = 11,
    VLG = 12, 
    VLI = 13,
    VNL = 14
    
# date constants
labels_start_date = '2020-04-09'

features_end_date = '2020-04-09'
    

# directory information
DATA_DIR_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'data')

BINARIES_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'models', 'binaries')
CHECKPOINTS_PATH = os.path.join(os.path.dirname(__file__), os.pardir, 'models', 'checkpoints')

os.makedirs(BINARIES_PATH, exist_ok=True)
os.makedirs(CHECKPOINTS_PATH, exist_ok=True)