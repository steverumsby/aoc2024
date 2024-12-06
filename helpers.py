#!/usr/bin/env python
# coding: utf-8

# # Helpers
# 
# Just some helper functions for the advent of code puzzles.

# ## File input
# 
# Starting with functions for reading files, and returning the file content either as one big string or a list of separate lines.

def read_file(f):
    f = open(f)
    l = f.read()
    f.close()
    return l

def read_lines(f):
    f = open(f)
    l = f.read()
    f.close()
    return l.split('\n')

