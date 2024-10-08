#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/09/17 09:46:01 (UT+8) daisuke>
#

# importing os module
import os

# knowing where I am now
cwd = os.getcwd ()

# printing where I am now
print (f'currently working directory = "{cwd}"')

# target directory
dir_target = '/etc'

# printing status
print (f'now, changing directory to "{dir_target}"...')

# changing directory
os.chdir (dir_target)

# printing status
print (f'finished changing directory to "{dir_target}"!')

# knowing where I am now
cwd = os.getcwd ()

# printing where I am now
print (f'currently working directory = "{cwd}"')
