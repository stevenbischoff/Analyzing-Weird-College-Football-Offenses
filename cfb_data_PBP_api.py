import pandas as pd
from cfbd.rest import ApiException

from config import *

first_year = 2023
last_year = 2023

df_list = []
for year in range(first_year, last_year+1): 
    api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
    api_response = api_instance.get_calendar(year)
    dfCal = pd.DataFrame().from_records([g.to_dict()for g in api_response])

    dfPBP_list = []

    # loop through the calendar and get the PBP for each week
    print('Getting PBP data for year '+str(year)+'...')
    for i in range (0,len(dfCal)):
        # iterate through calendar to get variables to pass to the API
        week = int(dfCal.loc[i,'week']) # get week from calendar
        season_type = dfCal.loc[i,'season_type'] # get season type from calendar
        # Get play-by-play Data
        api_instance = cfbd.PlaysApi(cfbd.ApiClient(configuration))
        api_response = api_instance.get_plays(year,week,season_type=season_type)
        dfWk = pd.DataFrame().from_records([g.to_dict()for g in api_response])
        dfPBP_list.append(dfWk)
        print('PBP data downloaded for '+season_type+' week',week)

    dfPBP = pd.concat(dfPBP_list).reset_index(drop=True)
    dfPBP.to_csv('data/game_PBP_{}.csv'.format(year), index=False)
          
