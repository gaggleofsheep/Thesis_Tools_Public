import tkinter as tk
from tkinter import filedialog
# from tkVideoPlayer import TkinterVideo
import mpv
import os
import json
import math

class Rally:
    start_time: float
    end_time: float
    score_top: int
    score_bottom: int
    set_number: int

# def take_end_times(rally: Rally) -> float:
#     return rally.end_time

# def take_start_times(rally: Rally) -> float:
#     return rally.start_time

class Output:
    name: str
    top_player: str
    bottom_player: str
    file_path: str
    rally_array: list[Rally]
    time_played: float

    def save(self):
        self.name = match_name_text.get()
        self.top_player = top_player_text.get()
        self.bottom_player = bottom_player_text.get()

        self.time_played = 0
        end_time_total = sum([rally.end_time for rally in self.rally_array])
        start_time_total = sum([rally.start_time for rally in self.rally_array])
        self.time_played = end_time_total-start_time_total
        # for rally in self.rally_array:
            # self.time_played += rally.end_time - rally.start_time


        f = open(save_path_text.get(), 'w')

        json.dump(self, f, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
        

output = Output()
output.rally_array = []
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

instructions_label = tk.Label(root, text="press / to begin and end rally recording \n u to undo \n w and s to increase the score of the relevant player \n q and a to decrease the score of the relevant player")
instructions_label.pack()

match_name_text = tk.StringVar()
match_name_label = tk.Label(root, text="Match Name: ")
match_name_label.pack()
match_name_input = tk.Entry(root, width=28, textvariable=match_name_text)
match_name_input.pack()

top_player_text = tk.StringVar()
top_player_label = tk.Label(root, text="Top Player Name: ")
top_player_label.pack()
top_player_input = tk.Entry(root, width=28, textvariable=top_player_text)
top_player_input.pack()

left_text = tk.StringVar(value="0")
points_top = tk.Entry(root, width=14, textvariable=left_text)
points_top.pack()

bottom_player_text = tk.StringVar()
bottom_player_label = tk.Label(root, text="Bottom Player Name: ")
bottom_player_label.pack()
bottom_player_input = tk.Entry(root, width=28, textvariable=bottom_player_text)
bottom_player_input.pack()


# match_name_label = tk.Label(root, text="Match Name: ")
# match_name_label.pack(side="left")


right_text = tk.StringVar(value="0")
points_bottom = tk.Entry(root, width=14, textvariable=right_text)
points_bottom.pack()

#Vincents set number 
set_number_label = tk.Label(root, text="set number: ")
set_number_label.pack()
set_number = tk.StringVar(value="1")
set_number_box = tk.Entry(root, width=14, textvariable=set_number)
set_number_box.pack()

save_btn = tk.Button(root, text="Save Location", command=save_path)
save_btn.pack()

save_path_text = tk.StringVar()
save_path_label = tk.Label(root, textvariable=save_path_text)
save_path_label.pack()

vid_player = mpv.MPV(osc=True, input_default_bindings=True, input_vo_keyboard=True)

rally_toggle = False
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

@vid_player.on_key_press('/')
def my_b_binding():
    global rally_toggle
    global begin_rally_time

    current_time: float = vid_player.time_pos # type: ignore

    if not rally_toggle:
        vid_player.show_text("Begin Rally")
        begin_rally_time = current_time
    else:
        vid_player.show_text("End Rally")
        rally = Rally()
        rally.start_time = begin_rally_time
        rally.end_time = current_time
        rally.score_top = int(left_text.get())
        rally.score_bottom = int(right_text.get())
        rally.set_number = int(set_number.get())
        output.rally_array.append(rally)
        update_latest_rally_val()
        
    rally_toggle = not rally_toggle


@vid_player.on_key_press('w')
def my_left_binding():
    left_val = int(left_text.get())
    left_text.set(str(left_val + 1))
    update_latest_rally_val()

@vid_player.on_key_press('q')
def my_left__dec_binding():
    left_val = int(left_text.get())
    left_text.set(str(left_val - 1))
    update_latest_rally_val()


@vid_player.on_key_press('s')
def my_right_binding():
    right_val = int(right_text.get())
    right_text.set(str(right_val + 1))
    update_latest_rally_val()

@vid_player.on_key_press('a')
def my_right_dec_binding():
    right_val = int(right_text.get())
    right_text.set(str(right_val - 1))
    update_latest_rally_val()

@vid_player.on_key_press('i')
def my_set_binding():
    set_number_holder = int(set_number.get())
    set_number.set(str(set_number_holder + 1))
    right_text.set(str(0))
    left_text.set(str(0))
    update_latest_rally_val()


@vid_player.on_key_press('u')
def my_undo_binding():
    global rally_toggle
    if len(output.rally_array) <= 1:
        vid_player.time_pos = 0
        return

    if rally_toggle == False:
        vid_player.time_pos = output.rally_array[-2].end_time
        output.rally_array.pop()
        right_text.set(str(output.rally_array[-1].score_bottom))
        left_text.set(str(output.rally_array[-1].score_top))
        set_number.set(str(output.rally_array[-1].set_number))
    else: #if undo within a rally undo score but nothing gets saved
        vid_player.time_pos = output.rally_array[-1].end_time
        right_text.set(str(output.rally_array[-1].score_bottom))
        left_text.set(str(output.rally_array[-1].score_top))
        set_number.set(str(output.rally_array[-1].set_number))
        rally_toggle = False

    update_latest_rally_val()


def update_latest_rally_val():
    if len(output.rally_array) == 0:
        return

    #output.rally_array[-1].score_top = int(left_text.get())
    #output.rally_array[-1].score_bottom = int(right_text.get())
    #output.rally_array[-1].set_number = int(set_number.get())
    output.save()


root.mainloop()
