
from collections import Counter

class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.
        """
        self.__count = 0      # how many data values seen so far
        self.__avg = 0        # the running average so far
        self.__inputs = []

    def add(self, value):
        """
        Purpose:
            Use the given value in the calculation of mean and
            variance.
        Pre-Conditions:
            :param value: the value to be added
        Post-Conditions:
            none
        Return:
            :return none
        """
        self.__count += 1
        self.__inputs.append(value)
        k = self.__count           # convenience
        diff = value - self.__avg  # convenience
        self.__avg += diff / k


    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__avg

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__count

    def min(self):
        """
        Purpose:
            Return the minimum value seen so far.
        Post-conditions:
            (none)
        Return:
            The minimum seen so far.
            Note: if no data has been seen, NONe is returned.

        """
        if len(self.__inputs) == 0:
            return None
        else:
            return  min(self.__inputs)

    def max(self):
        """
        Purpose:
            Return the maximum value seen so far.
        Post-conditions:
            (none)
        Return:
            The maximum seen so far.
            Note: if no data has been seen, NONe is returned.

        """
        if len(self.__inputs) == 0:
            return None
        else:
            return  max(self.__inputs)

    def mode(self):
        """
        Purpose:
            Return the maximum value seen so far.
        Post-conditions:
            (none)
        Return:
            The maximum seen so far.
            Note: if no data has been seen, NONe is returned.

        """
        data = Counter(self.__inputs)
        data_dict = dict(data)
        if len(self.__inputs) == 0:
            return None
        else:
            return [k for k, v in data_dict.items() if v == max(list(data.values()))][0]

    def range(self):
        """
        Purpose:
            Return the range for the input.
        Post-conditions:
            (none)
        Return:
            The range.
            Note: if no data has been seen, NONe is returned.

        """
        mi = self.min()
        ma = self.max()

        if len(self.__inputs) == 0:
            return None
        else:
            return ma - mi



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
# test Statistics.add()
# We can't test add() directly, so check add() + count()
# these are integration tests


test_item = 'add() + avg()'
data1 = [1, 3, 4, 5, 7, 9, 2]
expected = 4.4285
tolerance = 0.0001
reason = "Check avg after one value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.mean()

if not close_enough(result,expected,tolerance):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

test_item = 'add() + avg()'
data1 = [1, 3, 4, 5, 7, 9, 2]
expected = 4.4285
tolerance = 0.0001
reason = "Check avg after one value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.mean()

if not close_enough(result,expected,tolerance):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


test_item = 'add() + avg()'
data1 = [-1, -2, -4, -7, -12, -19]
expected = -7.5
reason = "Check avg after one value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.mean()
if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


test_item = 'add() + avg()'
data1 = [-1, -13, -6, 4, 5, 19, 9]
expected = 2.4285714285714284
tolerance = 0.000000000000001
reason = "Check avg after one value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.mean()
if not close_enough(result,expected,tolerance):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


test_item = 'add() + avg()'
data1 = [.5, 3.6, 3.3, .6]
expected = 1.9
tolerance = 0.1
reason = "Check avg after one value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.mean()

if not close_enough(result,expected,tolerance):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#min general

test_item = 'min'
data1 = [.5, 3.6, 3.3, .6]
expected = .5
reason = "Check min after multiple value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.min()

if expected != result:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# min none test case
test_item = 'min'
data1 = []
expected = None
reason = "Check min after multiple value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.min()

if expected != result:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


#max general

test_item = 'max'
data1 = [.5, 3.6, 3.3, .6]
expected = 3.6
reason = "Check min after multiple value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.max()

if expected != result:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# max none test case
test_item = 'max'
data1 = []
expected = None
reason = "Check min after multiple value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.max()

if expected != result:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# mode general test case
test_item = 'mode'
data1 = [1,1,2,2,2,3,3,3,3,3]
expected = 3
reason = "Check mode after multiple value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.mode()

if expected != result:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# range general test case
test_item = 'range'
data1 = [1,1,2,2,2,3,3,3,3,3,10]
expected = 9
reason = "Check mode after multiple value added"

# call the operation
stats = Statistics()
for i in data1:
    stats.add(i)

result = stats.range()
if expected != result:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))