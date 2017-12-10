def get_equal_dividers(row):
    for i, num in enumerate(row):
        for j, div in enumerate(row):
            if i != j:
                if num % div == 0:
                    return num/div
            
    difference = largest - smallest
    return difference

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
    numlist = []
    for num in string.split('\t'):
        numlist.append(int(num))
    return numlist

def calc_checksum(filename):
    checksum = 0
    with open(filename) as infile:
        for line in infile:
            rowlist = string_to_list(line[:-1])
            difference = get_equal_dividers(rowlist)
            checksum += difference
    return checksum

if __name__ == "__main__":
    for i in range(1000):
        result = calc_checksum('input.txt')
    print(result)
