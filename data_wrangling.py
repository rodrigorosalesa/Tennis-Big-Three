import pandas as pd
import numpy as np
from functions import player_filter, concatenate_df



##############################################################################
# E X T R A C T 
##############################################################################
matches_raw = {year: pd.read_csv(f'data/atp_matches_singles_{year}.csv') for year in range(2000,2024)}
ranking_raw = {decade: pd.read_csv(f'data/atp_rankings_{decade}.csv') for decade in ["90s", "00s", "10s", "20s"]}



##############################################################################
# T R A N S F O R M 
##############################################################################
# MATCHES --------------------------------------------------
# Joining all data sets in one
matches_all = concatenate_df(list(matches_raw.keys()), matches_raw)

# Normalizing DataFrames for the Big Three
df_federer = player_filter('Roger Federer', matches_all)
df_nadal = player_filter('Rafael Nadal', matches_all)
df_djokovic = player_filter('Novak Djokovic', matches_all)

# Concatenating the Data Frames for all 3 players
matches_final = pd.concat((df_federer, df_nadal, df_djokovic), ignore_index=True)

# Dropping extra columns
cols = ['winner_seed', 'winner_entry', 'winner_hand', 'winner_ht', 'winner_ioc', 'winner_age', 'w_ace', 'w_df', 'w_svpt', 'w_1stIn', 
        'w_1stWon', 'w_2ndWon', 'w_SvGms', 'w_bpSaved', 'w_bpFaced', 'loser_seed', 'loser_entry', 'loser_hand', 'loser_ht', 'loser_ioc', 
        'loser_age', 'l_ace', 'l_df', 'l_svpt', 'l_1stIn', 'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved', 'l_bpFaced', 'winner_id', 
        'winner_name', 'loser_id', 'loser_name', 'winner_rank', 'winner_rank_points', 'loser_rank', 'loser_rank_points']
matches_final.drop(cols, axis=1, inplace=True)

# Feature Engineering
# Changing name of some columns
matches_final = matches_final.rename(columns={'tourney_id':'tournament_id', 'tourney_name':'tournament_name', 
                                            'tourney_level':'tournament_level', 'tourney_date':'tournament_date'})

# Date Columns
matches_final['tournament_date'] = pd.to_datetime(matches_final['tournament_date'], format='%Y%m%d')
matches_final['tournament_year'] = matches_final['tournament_date'].dt.year
matches_final['tournament_month'] = matches_final['tournament_date'].dt.month
matches_final['tournament_day'] = matches_final['tournament_date'].dt.day

# Deal with missing values
matches_final.sort_values(by=['p_name','tournament_date','tournament_name','match_num'], inplace=True)
cols = ['p_ace', 'p_df', 'p_svpt', 'p_1stIn', 'p_1stWon', 'p_2ndWon', 'p_SvGms', 'p_bpSaved', 'p_bpFaced', 'o_bpFaced', 'o_bpSaved']
for col in cols:
    matches_final[col].bfill(inplace=True)
    matches_final[col].ffill(inplace=True)

# Fixing tournament names
matches_final['tournament_name'] = np.where(matches_final['tournament_name'] == 'Us Open', 'US Open', matches_final['tournament_name'])

# Statistics of the match
matches_final['p_bpCreatedR'] = matches_final['o_bpFaced']
matches_final['p_bpWonR'] = matches_final['p_bpCreatedR'] - matches_final['o_bpSaved']
matches_final['p_bpConRate'] = matches_final['p_bpWonR'] / matches_final['p_bpCreatedR']
matches_final['p_2ndIn'] = matches_final['p_svpt'] - matches_final['p_df'] - matches_final['p_1stIn']
matches_final['p_1stIn_percentage'] = matches_final['p_1stIn'] / matches_final['p_svpt']
matches_final['p_2ndIn_percentage'] = matches_final['p_2ndIn'] / (matches_final['p_2ndIn'] + matches_final['p_df'])
matches_final['p_prob_win_point_1st'] = matches_final['p_1stWon'] / matches_final['p_1stIn']
matches_final['p_prob_win_point_2nd'] = matches_final['p_2ndWon'] / matches_final['p_2ndIn']
matches_final['p_prob_win_point_serve'] = matches_final['p_1stIn_percentage'] * matches_final['p_prob_win_point_1st'] \
            + (1 - matches_final['p_1stIn_percentage']) * matches_final['p_2ndIn_percentage'] * matches_final['p_prob_win_point_2nd']
matches_final['p_preassure_points'] = matches_final['p_bpCreatedR'] + matches_final['p_bpFaced']
matches_final['p_preassure_points_won'] = matches_final['p_bpWonR'] + matches_final['p_bpSaved']
matches_final['p_preassure_points_ratio'] = matches_final['p_preassure_points_won'] / matches_final['p_preassure_points']


# RANKING --------------------------------------------------
# Joining all data sets in one
ranking_all = concatenate_df(list(ranking_raw.keys()), ranking_raw)

# Feature Engineering
# Writing the name of the player in ranking dataset
c1 = (matches_all['winner_name']=='Roger Federer')
c2 = (matches_all['winner_name']=='Rafael Nadal')
c3 = (matches_all['winner_name']=='Novak Djokovic')
players_id = matches_all[c1 | c2 | c3][['winner_id', 'winner_name']].groupby('winner_name').max().reset_index()
ranking_final = ranking_all.merge(players_id, left_on='player', right_on='winner_id')
ranking_final = ranking_final.rename(columns={'player': 'player_id', 'winner_name': 'player_name'})
ranking_final = ranking_final[ranking_final['player_name'].isin(['Roger Federer', 'Rafael Nadal', 'Novak Djokovic'])]

# Dropping extra columns
ranking_final.drop('winner_id', axis=1, inplace=True)

# Date Columns
ranking_final['ranking_date'] = pd.to_datetime(ranking_final['ranking_date'], format='%Y%m%d')
ranking_final['ranking_year'] = ranking_final['ranking_date'].dt.year
ranking_final['ranking_month'] = ranking_final['ranking_date'].dt.month
ranking_final['ranking_day'] = ranking_final['ranking_date'].dt.day



##############################################################################
# L O A D 
##############################################################################
ranking_final.to_csv('ranking.csv', index=False)
matches_final.to_csv('matches.csv', index=False)