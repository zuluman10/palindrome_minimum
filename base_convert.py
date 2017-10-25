""" Module base_palindrome"""
import sys
import csv
import os

# Strategy:
# 1) We only need to check up to the base + 1 of the highest integer
# 2) We don't need to be limited to letters...who knows how high the bases go
def base_convert(base_ten_int, new_base):
    """ Utility function to convert base ten int to new base"""
    if new_base < 2:
        raise ValueError("new_base cannot be less than 2")
    if base_ten_int < new_base:
        # just return what you found
        return list(str(base_ten_int))
    else:
        # take mod, do division, recursively try again
        return base_convert(base_ten_int//new_base, new_base) + \
                            list(str(base_ten_int % new_base))

def palindrome_check(number_of_ints):
    """ Build minimum base for palindrome and print to csv"""
    if number_of_ints <= 0:
        raise ValueError("number_of_ints must be greater than 0")
    # These tuples will be written to csv at the end
    palindrome_tuples = []
    # Using xrange, just in case we try this with really large ints one day
    for i in xrange(1, number_of_ints + 1):
        min_base = 2
        while min_base < number_of_ints + 2:
            base_list = base_convert(i, min_base)
            if base_list == base_list[::-1]:
                palindrome_tuples.append((str(i), str(min_base)))
                # Move on to the next number
                break
            min_base = min_base + 1
    palindrome_file = os.getenv('PALINDROME_FILE','palindrome_results.csv')
    # Using docs from python.org to write this part
    with open(palindrome_file, 'w') as csvfile:
        fieldnames = ['decimal',
                      'smallest base in which the number is a palindrome']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in palindrome_tuples:
            writer.writerow({fieldnames[0]: item[0],
                             fieldnames[1]: item[1]})

if __name__ == "__main__":
    palindrome_check(int(sys.argv[-1]))
