import tkinter as tk
from tkinter import *
import pandas as pd
import mpv
import os

row = 50

directory = r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\Training Set\R16 _ All England Open 2022 _ Brian Yang (CAN) vs Lee Zii Jia (MAS) [6]_OUTPUT"
csv_address = directory+"\\database_test.csv"

# get data base 
df = pd.read_csv(csv_address)
print(df)

# input("Press Enter to continue...")


## ---------------------- Video player loading and hit looping ---------------------------------
vid_player = mpv.MPV(osc=True, input_default_bindings=True, input_vo_keyboard=True, keep_open = True)

def update():
    global row
    global hit_end_time 
    hit_end_time = float(df['hit_end_time'][row])
    global hit_end_frame 
    hit_end_frame = float(df['hit_end_frame'][row])
    global hit_start_time
    hit_start_time = float(df['hit_start_time'][row])
    global hit_start_frame
    hit_start_frame = float(df['hit_start_frame'][row])
    global mp4_path
    mp4_path = df['mp4_filepath'][row]


@vid_player.property_observer('time-pos')
def time_observer(_name, value):
    update()
    print(value)
    print(hit_end_time)
    if value is None:
        return
    current_time = value
    if current_time >= hit_end_time:
        print("loop")
        vid_player.time_pos = hit_start_time
    if current_time*30 < hit_start_frame-1:
        print("jump")
        vid_player.time_pos = hit_start_frame/30

@vid_player.on_key_press('n')
def next_binding():
    global row 
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

@vid_player.on_key_press('b')
def back_binding():
    global row 
    row -= 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

## ------------------------------ shot selection UI and updating -------------------------------
""""Clear, Drop, Drive, Lift, Block, Net, Smash"""


# ---- near side shot functions

def n_clear():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "n_Clear"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def n_drop():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "n_Drop"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def n_smash():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "n_Smash"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def n_drive():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "n_Drive"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def n_net():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "n_Net"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def n_lift():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "n_Lift"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def n_block():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "n_Block"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

# ---- Far side shot functions
def f_clear():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "f_Clear"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def f_drop():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "f_Drop"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def f_smash():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "f_Smash"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def f_drive():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "f_Drive"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def f_net():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "f_Net"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def f_lift():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "f_Lift"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def f_block():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "f_Block"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False

def discard():
    """ Update CSV with hit data """
    global row
    df['shot_classification'][row] = "Discard"
    df.to_csv(csv_address, index=False)

    """ Go to next shot """
    row += 1
    update()
    vid_player.loadfile(mp4_path)
    vid_player.pause = True
    vid_player.time_pos = hit_start_time
    vid_player.pause = False


root = tk.Tk()  
root.title("Tkinter media")
root.configure(padx=15, pady=15)
top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


instructions_label = tk.Label(root, text="press buttons to update shot")
instructions_label.pack()

next_label = tk.Label(root, text="press n to go to next shot")
next_label.pack()

back_label = tk.Label(root, text="press b to go to previous shot")
back_label.pack()


""" Near side shots"""
n_clear_btn = tk.Button(root, text="n_Clear", command=n_clear, state="normal")
n_clear_btn.pack(in_=top, side=LEFT)

n_drop_btn = tk.Button(root, text="n_Drop", command=n_drop, state="normal")
n_drop_btn.pack(in_=top, side=LEFT)

n_smash_btn = tk.Button(root, text="n_Smash", command=n_smash, state="normal")
n_smash_btn.pack(in_=top, side=LEFT)

n_drive_btn = tk.Button(root, text="n_Drive", command=n_drive, state="normal")
n_drive_btn.pack(in_=top, side=LEFT)

n_net_btn = tk.Button(root, text="n_Net", command=n_net, state="normal")
n_net_btn.pack(in_=top, side=LEFT)

n_lift_btn = tk.Button(root, text="n_Lift", command=n_lift, state="normal")
n_lift_btn.pack(in_=top, side=LEFT)

n_block_btn = tk.Button(root, text="n_Block", command=n_block, state="normal")
n_block_btn.pack(in_=top, side=LEFT)

"""Far side shots"""
f_clear_btn = tk.Button(root, text="f_Clear", command=f_clear, state="normal")
f_clear_btn.pack(in_=top, side=RIGHT)

f_drop_btn = tk.Button(root, text="f_Drop", command=f_drop, state="normal")
f_drop_btn.pack(in_=top, side=RIGHT)

f_smash_btn = tk.Button(root, text="f_Smash", command=f_smash, state="normal")
f_smash_btn.pack(in_=top, side=RIGHT)

f_drive_btn = tk.Button(root, text="f_Drive", command=f_drive, state="normal")
f_drive_btn.pack(in_=top, side=RIGHT)

f_net_btn = tk.Button(root, text="f_Net", command=f_net, state="normal")
f_net_btn.pack(in_=top, side=RIGHT)

f_lift_btn = tk.Button(root, text="f_Lift", command=f_lift, state="normal")
f_lift_btn.pack(in_=top, side=RIGHT)

f_block_btn = tk.Button(root, text="f_Block", command=f_block, state="normal")
f_block_btn.pack(in_=top, side=RIGHT)


discard_btn = tk.Button(root, text="Discard", command=discard, state="normal")
discard_btn.pack(in_=top, side=RIGHT)

## -------------------- main video playing loop I think --------------------------------------


update()
vid_player.loadfile(df['mp4_filepath'][row])
#vid_player.time_pos = hit_start_time
vid_player.pause = True


root.mainloop()
    






