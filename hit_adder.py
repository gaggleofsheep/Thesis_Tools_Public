import tkinter as tk
from tkinter import filedialog
# from tkVideoPlayer import TkinterVideo
import mpv
import os
import json
import math

class Shot:
    hit_time: float
    hit_frame: int
    shot_number: int

class Output:
    name: str
    top_player: str
    bottom_player: str
    top_player_score: int
    bottom_player_score: int
    set_number: int
    fps: int
    file_path: str
    shot_array: list[Shot]

    def save(self):
        self.name = rally_identifier_text.get()
        self.top_player = top_player_text.get()
        self.bottom_player = bottom_player_text.get()
        self.top_player_score = int(top_player_score_text.get())
        self.bottom_player_score = int(bottom_player_score_text.get())
        self.set_number = int(set_number.get())
        self.fps = int(fps_number.get())
        f = open(save_path_text.get(), 'w')
        json.dump(self, f, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
        

output = Output()
output.shot_array = []
output.name = ""



# def update_duration(event):
#     """ updates the duration after finding the duration """
#     duration = vid_player.properties.get("time-pos")
#     print(duration)
#     # end_time["text"] = str(datetime.timedelta(seconds=duration))
#     # progress_slider["to"] = duration


# def update_scale(event):
#     """ updates the scale value """
#     progress_slider.set(vid_player.)


def load_video():
    """ loads the video """
    output.file_path = filedialog.askopenfilename()

    print(output.file_path)
    file_name = output.file_path.split("/")[-1]
    print(file_name)
    name_list = file_name.removesuffix(".mp4").split("_")
    print(name_list)
    # example format set_1_AXELSEN_0_SAI PRANEETH_0
    rally_identifier_text.set(file_name.removesuffix(".mp4"))
    set_number.set(name_list[1])
    top_player_text.set(name_list[2])
    top_player_score_text.set(name_list[3])                         
    bottom_player_text.set(name_list[4])
    bottom_player_score_text.set(name_list[5])
    json_output_path = output.file_path.removesuffix(".mp4")+".json"
    print(json_output_path)
    save_path_text.set(json_output_path)
    if output.file_path:
        vid_player.loadfile(output.file_path)


def save_path():
    global output

    file_path = filedialog.asksaveasfilename()
    if file_path:
        save_path_text.set(file_path)
        load_btn.configure(state="active")
        if os.path.isfile(file_path):
            f = open(file_path)
            output = json.load(f)
    

root = tk.Tk()
root.title("Tkinter media")
root.configure(padx=15, pady=15)

load_btn = tk.Button(root, text="Load", command=load_video, state="disabled")
load_btn.pack()

instructions_label = tk.Label(root, text="press z when a player hits the shuttle")
instructions_label.pack()

rally_identifier_text = tk.StringVar()
rally_identifier_label = tk.Label(root, text="rally_identifier: ")
rally_identifier_label.pack()
rally_identifier_input = tk.Entry(root, width=28, textvariable=rally_identifier_text)
rally_identifier_input.pack()

top_player_text = tk.StringVar()
top_player_label = tk.Label(root, text="Top Player Name: ")
top_player_label.pack()
top_player_input = tk.Entry(root, width=28, textvariable=top_player_text)
top_player_input.pack()

top_player_score_text = tk.StringVar(value="0")
points_top = tk.Entry(root, width=14, textvariable=top_player_score_text)
points_top.pack()

bottom_player_text = tk.StringVar()
bottom_player_label = tk.Label(root, text="Bottom Player Name: ")
bottom_player_label.pack()
bottom_player_input = tk.Entry(root, width=28, textvariable=bottom_player_text)
bottom_player_input.pack()


# match_name_label = tk.Label(root, text="Match Name: ")
# match_name_label.pack(side="left")


bottom_player_score_text = tk.StringVar(value="0")
points_bottom = tk.Entry(root, width=14, textvariable=bottom_player_score_text)
points_bottom.pack()

#Vincents set number 
set_number_label = tk.Label(root, text="set number: ")
set_number_label.pack()
set_number = tk.StringVar(value="1")
set_number_box = tk.Entry(root, width=14, textvariable=set_number)
set_number_box.pack()

fps_label = tk.Label(root, text="fps: ")
fps_label.pack()
fps_number = tk.StringVar(value="30")
fps_number_box = tk.Entry(root, width=14, textvariable=fps_number)
fps_number_box.pack()

output.fps = int(fps_number.get())

save_btn = tk.Button(root, text="Save Location", command=save_path, state = "disabled")
save_btn.pack()

save_path_text = tk.StringVar()
save_path_label = tk.Label(root, textvariable=save_path_text)
save_path_label.pack()

vid_player = mpv.MPV(osc=True, input_default_bindings=True, input_vo_keyboard=True, keep_open=True)

load_video()

begin_rally_time = 0.0

# Property access, these can be changed at runtime
# @vid_player.property_observer('time-pos')
# def time_observer(_name, value):
#     # current_time = value
#     # Here, _value is either None if nothing is playing or a float containing
#     # fractional seconds since the beginning of the file.
#     # print('Now playing at {:.2f}s'.format(value))
#     end_time["text"] = str(datetime.timedelta(seconds=value))
#     progress_slider["to"] = value

@vid_player.on_key_press('z')
def my_b_binding():
    shot = Shot()
    current_time: float = vid_player.time_pos # type: ignore
    current_frame: int = int(current_time * float(output.fps))
    hit_count = len(output.shot_array)
    vid_player.show_text("Hit")
    vid_player.show_text(hit_count)
    shot.hit_time = current_time
    shot.hit_frame = current_frame
    shot.shot_number = hit_count
    output.shot_array.append(shot)
    update_latest_shot()

@vid_player.on_key_press('u')
def my_undo_binding():
    global rally_toggle
    if len(output.shot_array) <= 1:
        vid_player.time_pos = 0
        return

    vid_player.time_pos = output.shot_array[-2].hit_time
    output.shot_array.pop()


    update_latest_shot()


def update_latest_shot():
    if len(output.shot_array) == 0:
        return

    output.save()


root.mainloop()
