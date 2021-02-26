# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#   Assignment 3: ADTs and Testing

# This script is a starter file for testing the Statistics ADT

import Statistics as S


def close_enough(a, b, tolerance):
    """
    Purpose:
        Check if 2 floating point values are close enough to 
        be considered equal.  See the Addendum in the assignment!
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return True if the difference between a and b is small
    """
    return abs(a - b) < tolerance


#####################################################################
# test Statistics.create()
# We can't test the object's identity, and the attributes are private
# The only thing we can do is check to see if the initial values are correct
# This is indirect testing, and since we're using 2 methods in the test, 
# it's a very limited form of integration testing.


test_item = 'Statistics.create()'
expected = 0
reason = "Initial count value"

# call the operation
stats = S.Statistics()
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


expected = 0
reason = "Initial average value"

# call the operation
stats = S.Statistics()
result = stats.mean()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))




#####################################################################
# test Statistics.add()  
# We can't test add() directly, so check add() + count()
# these are integration tests


test_item = 'add() + count()'
data_in = 0
expected = 1
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


test_item = 'add() + count()'
data_in = [0, 0, 0, 0, 0]
expected = 5
reason = "Check count after 5 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))






#####################################################################
# test Statistics.mean()


test_item = 'add() + mean()'
data_in = 0
expected = 0
reason = "Check average after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mean()

# We shouldn't test the floating point values for equality, because or roundoff error
# So use the close_enough() function.

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


#####################################################################
# test Statistics.mean()


test_item = 'add() + mean()'
data_in = [0, 0, 0, 0, 0]
expected = 0.0
reason = "Check average after 5 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))





print('*** Test script completed ***')