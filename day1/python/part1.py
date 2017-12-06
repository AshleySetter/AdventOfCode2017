import numpy as np

def check_matches_next(sequence, index):
    """
    Checks if next element of sequence is equal to current element.
    For last element, checks if last element equals first element.

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
    if index != len(sequence)-1:
        result = sequence[index] == sequence[index+1]
    else:
        result = sequence[index] == sequence[0]
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
    summation = 0
    for index, element in enumerate(sequence):
        #print(index, element, check_matches_next(sequence, index))
        if check_matches_next(sequence, index):
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
    print(part1())
