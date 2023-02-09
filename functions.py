import pandas as pd
import numpy as np


def player_filter(player: str, df_original: pd.DataFrame) -> pd.DataFrame: 
    '''
    Normalize data of the player of interest.
    INPUT: 
        - player: name of the tennis player 
        - df_original: dataframe of all the matches
    OUTPUT:
        - df: normalized data frame where the player of interest always appears first 
    '''
    win = (df_original['winner_name'] == player)
    lose = (df_original['loser_name'] == player)
    df = df_original[win | lose]
    df['result'] = np.where(df['winner_name'] == player, 'win', 'lose')

    main_player_cols = ['p_name', 'p_id', 'p_seed', 'p_rank', 'p_rank_points', 'p_entry', 'p_hand', 'p_height', 'p_country', 'p_age', 'p_ace', 
                        'p_df', 'p_svpt', 'p_1stIn', 'p_1stWon', 'p_2ndWon', 'p_SvGms', 'p_bpSaved', 'p_bpFaced']
    
    o_cols = ['o_name', 'o_id', 'o_seed', 'o_rank', 'o_rank_points', 'o_entry', 'o_hand', 'o_height', 'o_country', 'o_age', 'o_ace', 'o_df', 
            'o_svpt', 'o_1stIn', 'o_1stWon', 'o_2ndWon', 'o_SvGms', 'o_bpSaved', 'o_bpFaced']
    
    win_cols = ['winner_name', 'winner_id', 'winner_seed', 'winner_rank', 'winner_rank_points', 'winner_entry', 'winner_hand', 
                'winner_ht', 'winner_ioc', 'winner_age', 'w_ace', 'w_df', 'w_svpt', 'w_1stIn', 'w_1stWon', 'w_2ndWon', 'w_SvGms', 
                'w_bpSaved', 'w_bpFaced']
    
    lose_cols = ['loser_name', 'loser_id', 'loser_seed', 'loser_rank', 'loser_rank_points', 'loser_entry', 'loser_hand', 'loser_ht', 'loser_ioc', 
                'loser_age', 'l_ace', 'l_df', 'l_svpt', 'l_1stIn', 'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved', 'l_bpFaced']
    
    for i in range(0, len(main_player_cols)):
        df[main_player_cols[i]] = np.where(df['winner_name'] == player, df[win_cols[i]], df[lose_cols[i]])
        df[o_cols[i]] = np.where(df['winner_name'] != player, df[win_cols[i]], df[lose_cols[i]])
        
    return df

#-----------------------------------------------------------------------------------------------------------------

def concatenate_df (keys: list, df_original: dict) -> pd.DataFrame: 
    '''
    Concatenate dataframes in a dictionary.
    INPUT: 
        - keys: name of the tennis player 
        - df_original: dictionary of DataFrames
    OUTPUT:
        - df: all DataFrames presented in df_original concatenated 
    '''
    df = df_original[keys[0]]
    for key in keys:
        if key == keys[0]:
            pass
        else: 
            df = pd.concat((df, df_original[key]), ignore_index=True)
    
    return df