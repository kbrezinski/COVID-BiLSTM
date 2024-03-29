
import pandas as pd

from utils.config import *


def get_mobil_feat(country_code: str, averaging=None, normalize=True, drop_na=True):
    
    # potential label indices
    feat_indices = ['mobility_retail_and_recreation',
                     'mobility_transit_stations',
                     'mobility_workplaces']
    
    # read csv
    df = pd.read_csv(DATA_DIR_PATH + '\CAN-mobility.csv')
    
    # fetch country code
    df = df.loc[df['location_key'] == country_code]
    
    # prepare datetime and assign to index
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    
    # returns label columns
    df = df.loc[:, feat_indices]
    
    # if averaging, perform rolling overaging of weekend sensitive metrics
    if averaging is not None:
        df['mobility_workplaces'] = df['mobility_workplaces'].rolling(averaging).sum()
        df['mobility_transit_stations'] = df['mobility_transit_stations'].rolling(averaging).sum()
        
    # apply normalization column-wise
    if normalize:
        df = df.apply(lambda x: (x - x.mean() ) / x.std(), axis=0)
        
   # drop rows which do not have full data
    if drop_na:
        df = df.dropna() 
    
    return df


def get_labels(country_code: str, drop_na=True):
    '''
    Get the labels
    '''
    
    # potential label indices
    label_indices = ['TotalCases', 'TotalHospitalized', 'TotalICU']
    
    # read csv
    df = pd.read_csv(DATA_DIR_PATH + '\CAN-health_outcomes.csv')
    
    # fetch country code
    df = df.loc[df['location_key'] == country_code]
    
    # prepare datetime and assign to index
    df['date'] = pd.to_datetime(
        df['SummaryDate'].apply(lambda d: d.split(' ')[0])).rename('date')
    df = df.set_index('date')
    
    # returns label columns
    df = df.loc[:, label_indices]
    
    # drop rows which do not have full data
    if drop_na:
        df = df.dropna()

    return df



def load_population_metadata():
    
    # read csv; forst three columns: id, total_area, population
    df = pd.read_csv(DATA_DIR_PATH + '\demographics.csv',
                     usecols=[0, 1, 2])
    
    df = df.set_index('location_key')
    
    # use to index [id, attr]
    #df df.loc['AB', 'population']
    
    return df
    

    
    
    