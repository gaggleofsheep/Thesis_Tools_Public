import tkinter as tk
from tkinter import filedialog

import pandas as pd
import os
import json
import csv
import mpv

column_titles = ['data_index','shot_classification', 'csv_filepath', 'mp4_filepath','hit_start_frame', 
                    'hit_end_frame', 'hit_start_time', 'hit_end_time','internal_shot_number',
                    'top_player','bottom_player','set_number', 'top_player_score',
                    'bottom_player_score','fps','resolution']

for i in range(150):
    string_holder = "x"+ str(i)
    column_titles.append(string_holder)
    

for i in range(150):
    string_holder = "y"+ str(i)
    column_titles.append(string_holder)


shot_database = pd.DataFrame(columns = column_titles, index=range(1200))
print(shot_database)

directory = r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\Testing Set\QF _ All England Open 2022 _ Chou Tien Chen (TPE) [4] vs Jonatan Christie (INA) [7]_OUTPUT"

# def add_shot_without_classification():

longest_hit_length = 0

shot_database_row = 0
hit_number = 1


def updateDatabaseRow(shot_database_row, hit_number, prev_hit_row, row):
    shot_database['hit_start_frame'][shot_database_row] = df['Frame'][prev_hit_row]
    shot_database['hit_end_frame'][shot_database_row] = df['Frame'][row]
    shot_database['hit_start_time'][shot_database_row] = df['Frame'][prev_hit_row]/30
    shot_database['hit_end_time'][shot_database_row] = df['Frame'][row]/30
    shot_database['mp4_filepath'][shot_database_row] = video_path
    shot_database['csv_filepath'][shot_database_row] = csv_path
    shot_database['set_number'][shot_database_row] = match_meta_data[5]

    shot_database['top_player'][shot_database_row] = match_meta_data[0]
    shot_database['top_player_score'][shot_database_row] = match_meta_data[1]
    shot_database['bottom_player'][shot_database_row] = match_meta_data[2]
    shot_database['bottom_player_score'][shot_database_row] = match_meta_data[3]
    shot_database['fps'][shot_database_row] = 30
    shot_database['resolution'][shot_database_row] = "1280x720"
    shot_database['internal_shot_number'][shot_database_row] = hit_number

    hit_number += 1
    shot_database_row += 1
    return shot_database_row, hit_number

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file file with hits 
    if f.endswith("hits.csv"):
        csv_path = f
        video_path = f.removesuffix("_predict_hits.csv") + ".mp4"
        split_video_path = video_path.split("\\")
        # print(split_video_path)
        last = len(split_video_path)
        # print(last)
        match_rally_title = split_video_path[last-1]
        # print(match_rally_title)
        match_rally_title = match_rally_title.removesuffix(".mp4")
        match_meta_data = match_rally_title.split("_")



        df = pd.read_csv(f)

        hit_list = pd.DataFrame(df.loc[df['Hit'] == 1])
        last_frame = pd.DataFrame(df.tail(1))
        hit_list = pd.concat([hit_list, last_frame])
        print(hit_list)

        prev_hit_row = None
        # current_hit_frame = 0
        hit_number = 1
        frame = 0


        
        for row in df.index:
            # print( df['Frame'][row], df['Hit'][row])
            if df['Hit'][row] == 1:
                #hit happened here
                if prev_hit_row is None:
                    prev_hit_row = row
                    # print(prev_hit_row)
                    continue
                
                shot_database_row, hit_number = updateDatabaseRow(shot_database_row, hit_number, prev_hit_row, row)

                prev_hit_row = row
            if prev_hit_row is None:
                continue
            shot_database['x'+ str(row-prev_hit_row)][shot_database_row] = df['X'][row]
            shot_database['y'+ str(row-prev_hit_row)][shot_database_row] = df['Y'][row]
        if prev_hit_row is None:
            continue
        shot_database_row, hit_number = updateDatabaseRow(shot_database_row, hit_number, prev_hit_row, df.shape[0]-1)


print(shot_database)

shot_database.to_csv(directory+"\\database_test.csv", index=False, )
