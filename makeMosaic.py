import aplpy
import atpy
import astropy
import matplotlib
#from IPython.external import mathjax; mathjax.install_mathjax()
import numpy as np
import math
import sys
import scipy
import matplotlib.pyplot as plt
#import pandas as pd
import statsmodels.formula.api as sm
#matplotlib.style.use('ggplot')

#%matplotlib inline
tile = "G000m03"
band = "L"
datapath = "data/raw/"


def fits_display_test(image_file):
    # Create a new figure
    fig = aplpy.FITSFigure(image_file)

    # Show the colorscale
    fig.show_colorscale()

    # Add contours
    fig.show_contour(image_file, cmap='jet', levels=np.linspace(0.0, 1.0, 10))

    # Make ticks white
    fig.ticks.set_color('white')

    # Make labels smaller
    fig.tick_labels.set_font(size='small')

    # Overlay a grid
    fig.add_grid()
    fig.grid.set_alpha(0.5)
    # Add a colorbar
    fig.add_colorbar()

    # Save image for publication
    #fig.save('.png')
