#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/30 15:14:48 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
parser = argparse.ArgumentParser (description='attaching error bars #2')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output    = args.output
resolution_dpi = args.resolution

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# check of extension of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing a message
    print (f'ERROR: output file must be either EPS or PDF or PNG or PS file.')
    # stopping the script
    sys.exit (0)

# data to be plotted
data_x = numpy.linspace (1.0, 10.0, 10)
data_y = 2.0 * data_x + 3.0

# generating random numbers for errors of y-value
rng = numpy.random.default_rng ()
data_x_err = rng.uniform (0.3, 0.7, 10)
data_y_err = rng.uniform (1.0, 3.0, 10)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.errorbar (data_x, data_y, xerr=data_x_err, yerr=data_y_err, \
             linestyle='None', marker='o', markersize=8.0, color='orange', \
             ecolor='black', elinewidth=2.0, capsize=5.0, \
             label='Sample data')

# setting ranges of x-axis and y-axis
ax.set_xlim (0.0, +11.0)
ax.set_ylim (0.0, +30.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (0.0, +10.0, 11))
ax.set_yticks (numpy.linspace (0.0, +30.0, 7))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output, dpi=resolution_dpi)
