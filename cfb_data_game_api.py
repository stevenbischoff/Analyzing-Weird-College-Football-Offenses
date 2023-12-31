import pandas as pd
from cfbd.rest import ApiException

from config import *

division = 'fbs'

first_year = 2004
last_year = 2023

df_list = []
for year in range(first_year, last_year+1):
    print(year)

    api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
    try:
        api_games = api_instance.get_games(year=year,division=division)
    except ApiException as e:
        print("Exception when calling GameApi->get_games: %s\n" % e)

    df = pd.DataFrame.from_records([game.to_dict() for game in api_games])

    df_list.append(df)
    
df_tot = pd.concat(df_list).reset_index(drop=True)
df_tot.to_csv('data/game_info_{}_{}.csv'.format(first_year, last_year),
              index=False)
