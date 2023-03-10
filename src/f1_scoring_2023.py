import pandas as pd
import os


def f1_parameters(drivers, teams): 

    HAM_bet = [4, 4, 4, 5, 3, 3]
    RUS_bet = [5, 3, 3, 4, 1, 4]

    PER_bet = [6, 2, 2, 6, 5, 5]
    VER_bet = [1, 1, 1, 2, 2, 1]

    NOR_bet = [7, 6, 7, 7, 7, 9]
    PIA_bet = [9, 9, 14, 8, 16, 7]

    ALO_bet = [12, 16, 8, 13, 9, 13]
    STR_bet = [13, 19, 12, 19, 15, 15]

    OCO_bet = [8, 10, 9, 10, 17, 8]
    GAS_bet = [10, 8, 10, 9, 10, 11]

    LEC_bet = [2, 5, 5, 1, 4, 2]
    SAI_bet = [3, 7, 6, 3, 6, 6]

    DEV_bet = [17, 15, 19, 16, 18, 16]
    TSU_bet = [15, 12, 16, 15, 12, 17]

    BOT_bet = [11, 11, 11, 11, 8, 12]
    ZHO_bet = [14, 13, 17, 14, 14, 18]

    MAG_bet = [16, 17, 13, 12, 13, 10]
    HUL_bet = [18, 20, 15, 18, 11, 14]

    SAR_bet = [20, 18, 20, 20, 20, 20]
    ALB_bet = [19, 14, 18, 17, 19, 19]

    merc_bet        = [3, 2, 2, 3, 1, 2]
    redbull_bet     = [2, 1, 1, 2, 2, 1]
    mclaren_bet     = [4, 4, 5, 4, 4, 4]
    aston_bet       = [6, 9, 6, 9, 7, 8]
    alpine_bet      = [5, 5, 4, 5, 6, 5]
    ferarri_bet     = [1, 3, 3, 1, 3, 3]
    alphatauri_bet  = [8, 7, 9, 7, 9, 9]
    alfaromeo_bet   = [7, 6, 7, 6, 5, 7]
    haas_bet        = [9, 10, 8, 8, 8, 6]
    wiliiams_bet    = [10, 8, 10, 10, 10, 10]

    #Creating dataframes of the bets
    df_driver_bet  = pd.DataFrame(
        list(
            zip(HAM_bet, RUS_bet, PER_bet, VER_bet, NOR_bet, PIA_bet, \
        ALO_bet, STR_bet, OCO_bet, GAS_bet, LEC_bet, SAI_bet, DEV_bet, TSU_bet, BOT_bet,\
            ZHO_bet, MAG_bet, HUL_bet, SAR_bet, ALB_bet )
            ) ,index= ['Jesper', 'Jonas', 'Lindskog', 'Mattias', 'Jonas_Far', 'Edvard*'], columns = drivers)

    df_constructor_bet  = pd.DataFrame(list(zip(merc_bet, redbull_bet, mclaren_bet, aston_bet, alpine_bet, ferarri_bet, alphatauri_bet,\
        alfaromeo_bet, haas_bet, wiliiams_bet)) ,  index= ['Jesper', 'Jonas', 'Lindskog', 'Mattias', 'Jonas_Far', 'Edvard*'], columns = teams)


    ######################## THE SCORING  ########################

    df_driver_points = pd.read_excel(os.path.join(os.getcwd(), 'f1scores_2023.xlsx'), 'Blad1')
    df_driver_points = df_driver_points.transpose()
    new_header = df_driver_points.iloc[0] #grab the first row for the header
    df_driver_points = df_driver_points[1:] #take the data less the header row
    df_driver_points.columns = new_header #set the header row as the df header
    df_driver_points = df_driver_points.astype(float)
    
    ######################## THE MODIFICATIONS FOR THOSE WITH SAME SCORE  ########################
    
    df_driver_mod = pd.read_excel(os.path.join(os.getcwd(), 'f1scores_2023.xlsx'), 'Blad2')
    df_driver_mod = df_driver_mod.transpose()
    new_header = df_driver_mod.iloc[0] #grab the first row for the header
    df_driver_mod = df_driver_mod[1:] #take the data less the header row
    df_driver_mod.columns = new_header #set the header row as the df header
    df_driver_mod = df_driver_mod.astype(int)



    df_constr_mod = pd.read_excel(os.path.join(os.getcwd(), 'f1scores_2023.xlsx'), 'Blad3')
    df_constr_mod = df_constr_mod.transpose()
    new_header = df_constr_mod.iloc[0] #grab the first row for the header
    df_constr_mod = df_constr_mod[1:] #take the data less the header row
    df_constr_mod.columns = new_header #set the header row as the df header
    df_constr_mod = df_constr_mod.astype(int)

    tracks = list(df_constr_mod.index.values) 

    return df_driver_bet, df_constructor_bet, df_driver_points, df_driver_mod, df_constr_mod, tracks