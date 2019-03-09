# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

# to plot the pretty figure
mpl.rc("axes", labelsize=14)
mpl.rc("xtick", labelsize=12)
mpl.rc("ytick", labelsize=12)

# where to save the figure
PROJECT_ROOT = "."
CHARPTER_ID = "classification"

def save_fig(fig_id,tight_layout=True):
    dir_path = os.path.join(PROJECT_ROOT,"images",CHARPTER_ID)
    path = os.path.join(PROJECT_ROOT,"images",CHARPTER_ID,fig_id+".png")
    print("Saving figure",fig_id)
    if tight_layout:
        plt.tight_layout()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    plt.savefig(path,format="png",dpi=300)

from scipy.io import loadmat

# 导入数据
mnist = loadmat("mnist-original.mat")
X = mnist["data"].T
y = mnist["label"][0]


def plot_digit(data):
    image = data.reshape(28,28)
    plt.imshow(image,cmap=mpl.cm.binary,interpolation="nearest")
    plt.axis("off")
# some_digit = X[36000]
# save_fig("some_digit_plot")
# plt.show()
def plot_digits(instances,images_per_row=10,**options):
    size = 28
    images_per_row = min(len(instances),images_per_row)
    images = [instance.reshape(size,size) for instance in instances]
    n_rows = (len(instances) - 1) // images_per_row + 1
    row_imags = []
    n_empty = n_rows * images_per_row - len(instances)
    images.append(np.zeros((size,size*n_empty)))
    for row in range(n_rows):
        rimages = images[row * images_per_row :(row+1) * images_per_row]
        row_imags.append(np.concatenate(rimages,axis=0))
    image = np.concatenate(row_imags,axis=1)
    plt.imshow(image,cmap=mpl.cm.binary,**options)
    plt.axis("off")

plt.figure(figsize=(9,9))
example_images = np.r_[X[:12000:600],X[13000:30600:600],X[30600:60000:590]]
plot_digits(example_images,images_per_row=10)
save_fig("more_digits_plot")
plt.show()