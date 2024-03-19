import ffmpeg
import os
import json

input_vid = ffmpeg.input(r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\QF_R16_R32\QF _ All England Open 2022 _ Tai Tzu Ying (TPE) [1] vs Nozomi Okuhara (JPN) [5].mp4")


footage_data = open(r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\QF_R16_R32\QF _ All England Open 2022 _ Tai Tzu Ying (TPE) [1] vs Nozomi Okuhara (JPN) [5].json","r")

# initialise joined with a 3 second intro
data = json.loads(footage_data.read())
top_player = data['top_player']
bottom_player = data['bottom_player']
output_path = R"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\QF_R16_R32\QF _ All England Open 2022 _ Tai Tzu Ying (TPE) [1] vs Nozomi Okuhara (JPN) [5]_OUTPUT\\"

for i in data['rally_array']: #array of all the rallies in a match
    print(i)
    rally_start = i['start_time']
    rally_end = i['end_time']
    score_top = i['score_top']
    score_bottom = i['score_bottom']
    set_number = i['set_number']
    length = rally_end-rally_start
    file_ouput_name = output_path+"_".join((top_player,str(score_top),bottom_player,str(score_bottom),"set",str(set_number)))+".mp4"
    rally = input_vid.trim(start=rally_start, duration = length ).filter('setpts','PTS-STARTPTS')
    out = ffmpeg.output(rally, file_ouput_name)
    out.run()

footage_data.close()




'''
joined = ffmpeg.concat(
    input_vid.trim(start=rally1_start, duration = duration1 ).filter('setpts','PTS-STARTPTS'),
    input_vid.trim(start=rally2_start, duration = duration2 ).filter('setpts','PTS-STARTPTS')    
)

file_ouput_name = "_".join((top_player,bottom_player,".mp4"))
out = ffmpeg.output(joined, file_ouput_name)
out.run()
'''
