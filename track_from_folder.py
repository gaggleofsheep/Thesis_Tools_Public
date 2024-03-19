import os
import subprocess

folder_name = R"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\QF_R16_R32\R32 _ All England Open 2022 _ Wang Zhi Yi (CHN) vs Pusarla V. Sindhu (IND) [6]_OUTPUT\\"

for i in os.listdir(folder_name):
    print(i)
    file_path = folder_name+i
    subprocess.run(["python", "3_in_3_out/predict3.py", f"--video_name = {file_path}", "--load_weights = 3_in_3_out/model906_30"])
