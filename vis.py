import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from matplotlib.widgets import Slider
from matplotlib import style

#Vehicle Ranges
MIN = 200
MIN_CAR = MIN
MAX_CAR = 240
MIN_LARGECAR = 310
MAX_LARGECAR = 350
MIN_LGV = 400
MAX_LGV = 449
MIN_HGV = 450
MAX_HGV = 500

f = open("readings", "r")
x = f.read().split(" ")
vals = [int(i) for i in x[:-1]]

style.use("fivethirtyeight")
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

time = np.arange(0.0, len(vals), 1)
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(2*np.pi*t)
l, = plt.plot(time,vals, lw=1)
plt.axis([0, 200, 50, 250])

axcolor = 'lightgoldenrodyellow'
axpos = plt.axes([0.2, 0.1, 0.65, 0.03])

spos = Slider(axpos, 'Pos', 0.1, 90.0)

def update(val):
    pos = spos.val
    ax.axis([pos,pos+200, -10, 300])
    fig.canvas.draw_idle()

spos.on_changed(update)

plt.show()

def prettify(plots):
    for k, ax in plots.items():
        ax.spines["top"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    global plt
    plt.sca(plots["count"])
    #plt.ylim(0, 70)
    if v:
        plt.yticks(np.arange(min(v), max(v)+1, 1.0))
    plt.xlabel('time (s)', fontsize=18)
    plt.ylabel('vehicle count', fontsize=16)
    plt.sca(plots["lidar"])
    #plt.xlabel('', fontsize=18)
    plt.ylabel('distance (cm)', fontsize=16)
    plt.ylim(0, 200)
    plt.yticks(range(0, 200, 10), [str(x) for x in range(0, 200, 10)], fontsize=14)
