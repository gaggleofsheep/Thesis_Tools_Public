import ffmpeg
import os
import json

footage_data = open(r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\QF_R16_R32\R32 _ All England Open 2022 _ Viktor Axelsen (DEN) [1] vs Sai Praneeth B. (IND).json","r")

data = json.loads(footage_data.read())

time_played = 0

for i in data['rally_array']:
    print(i)
    rally_start = i['start_time']
    rally_end = i['end_time']
    time_played = time_played+rally_end-rally_start
    print(time_played)


footage_data.close()







