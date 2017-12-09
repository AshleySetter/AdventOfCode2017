import numpy as np

def check_matches_next(sequence, index, jump):
    """
    Checks if element i+jump of sequence is equal to element i.
    If i+jump >= len(sequence) it cycles round.

    Parameters
    ----------
    sequence : ndarray
        sequence of integers
    index : int
        index of current element

    Returns
    -------
    result : bool
        bool telling if next element equals current element
    """
    compare_index = index + jump
    if compare_index > (len(sequence) - 1):
        compare_index = compare_index - (len(sequence))
    result = sequence[index] == sequence[compare_index]
    return result

def captcha_sum(sequence):
    """
    calculates sum of all digits that match the next digit in the sequence.

    Parameters
    ----------
    sequence : ndarray, list
        sequence of integers
    
    Returns 
    -------
    captcha_sum : int
        sum of all digits that match the next digit in the sequence
    """
    if len(sequence) % 2 != 0:
        raise ValueError("Sequence must have even length")
    summation = 0
    jump = int(len(sequence)/2)
    for index, element in enumerate(sequence):
        #print(index, element, check_matches_next(sequence, index))
        if check_matches_next(sequence, index, jump):
            summation += element
    return summation

def string_to_list(string):
    """
    converts string of numbers to numpy array of numbers

    Parameters
    ----------
    string : str
        string of integers
    
    Returns 
    -------
    sequence : ndarray
        sequence of integers

    """
    numlist = np.zeros(len(string))
    for i, char in enumerate(string):
        numlist[i] = int(char)
    return numlist

def part1():
    """
    Solves part1 of advent of code 2017 - http://adventofcode.com/2017/day/1

    Returns
    -------
    catcha_result : int
        result of part1 of day1 on 'input.txt' file

    """
    with open('input.txt') as infile:
        inputstring = infile.read()[:-1] # reads string of numbers from file omitting '\n' character
    numlist = string_to_list(inputstring)
    captcha_result = captcha_sum(numlist)
    return captcha_result

if __name__ == "__main__":
    for i in range(1000):
        result = part1()
    print(result)
