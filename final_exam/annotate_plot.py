"""Module that defines a function that serves to annotate graphs using matplotlib's text functionality"""

__author__ = "Tyler Gurney"

import sys
import matplotlib.pyplot as plt
from numpy import linspace
from datetime import *


def annotate_plot(annotations):
    """Takes nested dictionary, annotations, as input where the keys are strings,
    and each key has a dictionary with 'position', 'alignment', and 'fontsize' keys. The values for the subkeys are:
    'position': tuple of int/float values representing (x,y) coordinates where string is placed on graph
    'alignment': list of two arguments (strings) for horizontal/vertical text alignment
    'fontsize': int/float value dictating the size of the font for the relevant string

    Doesn't return an explicit value, but instead the function plots the relevant strings with the given information on
    a figure that should in theory be created before the function is called"""
    try:
        for key in annotations:
            plt.text((annotations[key]["position"][0]), (annotations[key]["position"][1]), key,
                     horizontalalignment=annotations[key]["alignment"][0],
                     verticalalignment=annotations[key]["alignment"][1], fontsize=annotations[key]["fontsize"])
    except ValueError:
        print("Please input dictionary with proper keys/values")
        sys.exit(1)
    except KeyError:
        print("Please input dictionary with proper key names")
        sys.exit(1)
    return


if __name__ == "__main__":
    x_values = linspace(-2,2)
    y_values = linspace(-2,2)**2
    date = date(2024, 5, 8).isoformat()
    test_annotations = {f'Created by Tyler Gurney {date}':
                        {"position": (-2.2, -0.75), "alignment": ['left', 'bottom'], "fontsize": 8}}

    plt.plot(x_values, y_values)
    annotate_plot(test_annotations)
    plt.show()