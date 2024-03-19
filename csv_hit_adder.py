import pandas as pd
import json
import csv
import os

directory = r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\Training Set\R16 _ All England Open 2022 _ Brian Yang (CAN) vs Lee Zii Jia (MAS) [6]_OUTPUT"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # checking if it is a file
    if f.endswith(".json"):
        json_address = f
        hit_data = open(json_address,"r")
        hit_data  = json.loads(hit_data.read()) 
        csv_address = f.removesuffix(".json")+"_predict.csv"
        output_path = (csv_address.removesuffix(".csv")+"_hits.csv")
        
        df = pd.read_csv(csv_address)
        num_frame = len(df.Frame)
        hit_list = [0] * num_frame

        for i in hit_data['shot_array']:
            hit_frame = i['hit_frame']
            hit_list[hit_frame] = 1
        print(df)

        df["Hit"] = hit_list



        df.to_csv(output_path, index=False)
