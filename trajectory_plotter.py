import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from numpy import diff
import numpy as np

def HitFinder(table, threshold, searchwidth):
    flag = 0
    holder = [0,0,0]
    hit_frame_array = []

    for accel,i in acceleration_table:
        holder[3] = holder[2]
        holder[2] = holder[1]
        holder[1] = accel

        if abs(accel) > threshold and flag != 1:
            flag = 1
            hit_frame_array.append(i)
        else: 
            if abs(accel) <= accel_minimum:
                flag = 0
    return hit_frame_array
    

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ['Frame','Visibility','X','Y','Time']
df = pd.read_csv(r"C:\Users\hongz\Dev\Thesis\Match Footage\All England 2022 Games\QF_R16_R32\R32 _ All England Open 2022 _ Viktor Axelsen (DEN) [1] vs Sai Praneeth B. (IND)_OUTPUT\set_1_AXELSEN_0_SAI PRANEETH_0_predict.csv", usecols=columns)

#remove untracked frames
data = df.loc[df["Visibility"] != 0]
#print(data)

# Convert frames to seconds
store_time = data['Frame'].to_numpy()/30
#print("time = ", store_time.shape, store_time)

store_X = data['X'].to_numpy()
#print("X values = ", store_X.shape, store_X)

store_Y = data['Y'].to_numpy()
#print("Y values =", store_Y.shape, store_Y)

t = store_time
dt = diff(store_time)
dt2 = dt[1:]
dt3 = dt[2:]

dx = diff(store_X)
dx2 = diff(dx)
dx3 = diff(dx2)
dx_dt = dx/dt
dx2_dt = dx2/dt2
dx3_dt = dx3/dt3

dy = diff(store_Y)
dy2 = diff(dy)
dy3 = diff(dy2)
dy_dt = dy/dt
dy2_dt = dy2/dt2
dy3_dt = dy3/dt3

t_index = t[1:]
dt2_index = t[2:]
dt3_index = t[3:]

fig, axs = plt.subplots(2, 3)

axs[0, 0].plot(t_index, dx_dt)
axs[0, 0].set_title("x velocity")
axs[1, 0].plot(t_index, dy_dt)
axs[1, 0].set_title("y velocity")
axs[0, 1].plot(dt2_index, dx2_dt)
axs[0, 1].set_title("x acceleration")
axs[1, 1].plot(dt2_index, dy2_dt)
axs[1, 1].set_title("y acceleration")
axs[0, 2].plot(dt3_index, dx3_dt)
axs[0, 2].set_title("X jerk")
axs[1, 2].plot(dt3_index, dy3_dt)
axs[1, 2].set_title("Y jerk")


# acceleration shot detection



Matrix1= np.array(dy2_dt)
Matrix2 = np.array(dt2_index)

acceleration_indexed = np.stack((Matrix1, Matrix2), axis=1)
with np.printoptions(precision=3, suppress=True):
    print("acceleration \n", acceleration_indexed)
acceleration_table = zip(dy2_dt, dt2_index)

flag = 0

accel_thresh = 1200
accel_minimum = 1500

for accel,i in acceleration_table:
    if abs(accel) > accel_thresh and flag != 1:
        flag = 1
        hit_frame_array.append(i)
    else: 
        if abs(accel) <= accel_minimum:
            flag = 0

# jerk shotdetection

# jerk_sum = zip(dy3_dt, dt3_index)
# print(dy3_dt)
# flag = 0

# jerk_amount = 1200
# jerk_minimum = 500

# for jerk,i in jerk_sum:
#     if abs(jerk) > jerk_amount and flag != 1:
#         flag = 1
#         hit_frame_array.append(i)
#     else: 
#         if abs(jerk) <= jerk_minimum:
#             flag = 0


print(hit_frame_array)
print(len(hit_frame_array))

hit_time_array = (np.array(hit_frame_array)+3)/30


fig.tight_layout()
plt.show()

