"""
plotutil.py - A module for plotting utilities.
"""

import ntpath
import os

import h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# define constants
COLOR_PALETTE = ["blue", "red", "green", "pink", "purple", "orange", "teal",
                 "grey", "black", "cyan", "magenta", "brown"]

def plot_uks(file_path, save_path=None,
             amplitude_unit="GHz", time_unit="ns",
             dpi=1000):
    """
    Get the final uks from a grape H5 file and plot them as a png.
    Args:
    file_path :: str - the full path to the H5 file
    save_path :: str - the full path to save the png file to
    amplitude_unit :: str - the unit to display for the pulse amplitude
    time_unit :: str - the unit to display for the pulse duration
    dpi :: int - the quality of the image
    Returns: nothing
    """
    # Open file and extract data.
    file_name = os.path.splitext(ntpath.basename(file_path))[0]
    f = h5py.File(file_path, "r")
    # Get the last set of uks.
    uks = np.array(f["uks"][-1])
    step_count = len(uks[0])
    h_names = list(f["Hnames"])

    # If the user did not specify a save path,
    # save the file to the current directory with
    # the data file's prefix.
    if save_path is None:
        save_path = "{}.png".format(file_name)

    # Plot the data.
    patches = list()
    labels = h_names
    plt.figure()
    plt.title(file_name)
    for i, pulse in enumerate(uks):
        label = labels[i]
        color = COLOR_PALETTE[i]
        patches.append(mpatches.Patch(label=label, color=color))
        plt.plot(np.arange(step_count), pulse, "o", color=color, ms=2,
                 alpha=0.9)
    #ENDFOR
    plt.legend(handles=patches, labels=labels, loc="upper right", framealpha=0.5)
    plt.xlabel("Time ({})".format(time_unit))
    plt.ylabel("Amplitude ({})".format(amplitude_unit))
    plt.savefig(save_path, dpi=dpi)
    

def _tests():
    """
    Run tests on the module.
    """
    pass


if __name__ == "__main__":
   _tests()
