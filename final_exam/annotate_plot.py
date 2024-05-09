import sys
import matplotlib.pyplot as plt
from numpy import linspace
from datetime import *


def annotate_plot(annotations):
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