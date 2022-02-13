
import argparse

from utils.config import *


def main(cfg):
    
    prov_code = cfg['prov_code'].lower()
    
    if prov_code == ProvCode.ALL.name.lower():
        print(prov_code + "HELLO!")
        
    elif prov_code == ProvCode.ON.name.lower():
        print(prov_code + "HELLO!")
        
    else:
        raise Exception(f'{prov_code} not supported')


def get_training_args():
    
    parser = argparse.ArgumentParser()
    
    # dataset related args
    parser.add_argument("--prov_code", '-p', choices=[p.name for p in ProvCode],
                        help='which province to process the data for', default=ProvCode.ALL.name)
    args = parser.parse_args()
    
    # prepare config dict
    cfg = dict()
    for arg in vars(args):
        cfg[arg] = getattr(args, arg)
    
    return cfg
        
if __name__ == '__main__':
    
    main(get_training_args())