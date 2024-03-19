import subprocess

with open("list.txt") as w:
    lines = w.readlines()
    for line in lines:
        subprocess.check_output(["yt-dlp", line])

