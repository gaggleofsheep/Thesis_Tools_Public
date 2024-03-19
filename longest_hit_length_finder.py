import pandas as pd
import os
import json
import csv

#input is a folder/directory containing all the predict_hit.csv files alongside the videos

directory = r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\QF_R16_R32\R32 _ All England Open 2022 _ Viktor Axelsen (DEN) [1] vs Sai Praneeth B. (IND)_OUTPUT"

longest_hit_length = 0
longest_hit_frame = 0
longest_hit_number = 0
longest_hit_path = ""
number_of_hits = 0
#longest_hit_video_path

## Find longest hit length in a match
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # checking if it is a file  
    if f.endswith("hits.csv"):
        video_path = f.removesuffix("_predict_hits.csv") + ".mp4"
        df = pd.read_csv(f)
        hit_list = pd.DataFrame(df.loc[df['Hit'] == 1])
        last_frame = pd.DataFrame(df.tail(1))
        hit_list = pd.concat([hit_list, last_frame])
        # print(hit_list)
        prev_frame = 0
        hit_number = 0
        frame = 0
        
        for row in hit_list.index:
            frame = hit_list["Frame"][row]
            hit_length = frame-prev_frame
            if hit_length > longest_hit_length:
                longest_hit_length = hit_length
                longest_hit_path = video_path
                longest_hit_number = hit_number
                longest_hit_frame = prev_frame
            hit_number = hit_number + 1
            number_of_hits += 1
            prev_frame = frame

    number_of_hits += 1
    print("path =", longest_hit_path)
    print("length = ",longest_hit_length)
    print("hit", longest_hit_number)
    print("frame = ", longest_hit_frame)
print("number of hits = ", number_of_hits)















