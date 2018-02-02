'''
Challenge 1 - IP Address
An IP address consists of 4 numbers separated by periods. Each number can be 0
to 255. There are no periods at the start or end of a valid IP address.

Create a program that takes an IP address and prints out whether the received IP
address is valid or invalid. If the IP address is valid, print out the
length of each segment and their numbers. If the IP address is invalid, let the
program detail why the address was invalid and suggestions for fixing the
address.

Rules:
    1. 4 numbers 0-255
    2. Each number is separated by a period
    3. There are no periods at the start or the end
'''
import re
import string
import sys

def error_printer(error_list):
    '''
    Input:
        A list containing the all of the errors the program found
        with the IP Address.
    Output:
        Prints the reasons why the IP Address was invalid, as well as
        suggestions for fixing it.
    '''
    print('The IP Address provided was invalid for the following reasons:')
    for i in error_list:
        print(i)

def check_substitutions(ip_addr):
    '''
    This only will be called if the user did not provide a valid ip address,
    after they have been told which errors were raised.

    Input:
        A raw ip_addr string which has failed our validity tests
    Output:
        If a simple tweak can turn the ip_addr string into a valid IP
        Address (replacing commas with periods, etc.), this will suggest
        the valid address to the user by printing it.
    '''
    non_digit = re.compile('[^\d]+') # <- This pattern matches any sequence of
                                     # characters that are not digits.
    re_strip = re.compile('(^[^\d]+|[^\d]+$)') # <- This matches any sequence of
                                            # characters that are not digits at the
                                            # beginning of end of the string
    leading_trailing = re.sub(re_strip,'',ip_addr)  # <- Here we're removing any
                        # non-digits from the beginning and/or end of the string
    period_split = leading_trailing.split('.')
    nondigit_split = re.split(non_digit, leading_trailing)
    if len(ip_checker(leading_trailing)) == 0:
        # ^This is one of the simplest cases. If the IP Address is valid after
        # we remove leading/trailing non-digit characters, we have a very good
        # guess as to what the user meant.
        print('''
    It looks like your IP Address might have had some periods or other non-digit
    characters at the beginning and/or end. When they were removed, the IP Address
    was valid. Did you mean to type:
        {}'''.format(leading_trailing))
    elif len(period_split) == 4:
        # ^Check to see if splitting JUST on periods will give us a list that's
        # the right size. If so, the problem MIGHT be a non-digit character
        # somewhere in the string.
        ip_new = '.'.join([non_digit.sub('',i) for i in period_split])
        # ^Removing non-digit characters.
        if len(ip_checker(ip_new)) == 0:
        # ^If this is true, then we were able to get a valid IP Address. The
        # user might have mis-typed something.
            print('''
    It looks like you might have had some non-digit characters in your IP Address.
    When they were removed, the IP Address was valid. Did you mean to type:
        {}'''.format(ip_new))
        check_binary(period_split)

    elif len(nondigit_split) == 4:
    # ^Looking at the case where we split on ANY sequence of non-digit characters
        ip_new = '.'.join(nondigit_split)
        if len(ip_checker(ip_new)) == 0:
        # ^If splitting like this gives a valid IP Address, the user probably used
        # something like a comma, or a period followed by a space to separate the numbers.
            print('''
    It looks like you might have used a character or string of characters other than
    a period to separate the numbers in your IP Address. Did you mean to type:
        {}'''.format(ip_new))
        check_binary(nondigit_split)
    check_binary([non_digit.sub('',ip_addr)])

def check_binary(ip_guess):
    '''
    The other way a user might make a mistake is if they entered the address
    in binary. An IPv4 address would be represented as either 4 octets of binary
    digits separated by periods/other, or as 32 binary digits.

    Input:
        A list containing the IP Address, already split into what this function
        will assume are the right pieces.
    Output:
        If ip_guess can be translated from binary into a valid IP Address, the
        function will print the translated  IP Address with an explanation to
        the user. If not, it returns None.
    '''
    if set(''.join(ip_guess)) == {'0','1'}: # <- Does the list contain only 1s and 0s?
        if len(ip_guess) ==1: # Is it unseparated? If so, split into groups of 8
            ip_guess = [ip_guess[0][i:i+8] for i in range(0,len(ip_guess[0]),8)]
        ip_new = '.'.join([str(int(i, base=2)) for i in ip_guess]) # convert from binary to int
        if len(ip_checker(ip_new)) == 0:    # If this gave us a valid IP Address,
                                            # let the user know.
            print('''
    It looks like you might have entered the IP Address in binary. Did you mean:
        {}'''.format(ip_new))


def ip_checker(ip_addr):
    '''
    Input:
        The raw ip_addr string we want to check for validity.
    Output:
        A list containing all the errors found by the function.
        If the length of this list is 0, the ip_addr is valid.
    '''
    error_list = []
    p = re.compile('[^\d]+')
    ip_addr = str(ip_addr)
    if len(ip_addr)==0:
        return ['- Address was an empty string.']
    if ip_addr[0] == '.': # Checks for leading periods
        error_list.append('- Address contains a leading period.')
    if ip_addr[-1] =='.': # Checks for trailing periods
        error_list.append('- Address contains a trailing period.')
    ip_list = ip_addr.strip('.').split('.') # Removes any leading or trailing periods
                                            # so we can see what else is wrong, and
                                            # splits on remaining periods
    if len(ip_list) < 4: # Checking to see that we have 4 segments
        error_list.append('- Found fewer than 4 numbers when the address was split into period-separated groups.')
    if len(ip_list) >4:
        error_list.append('- Found more than 4 numbers when the address was split into period-separated groups.')
    if not all([all([j in string.digits for j in i]) for i in ip_list]):
    # ^Are there any non-digit numbers in the IP Address after we've split?
        error_list.append('- Address contains characters other than 0-9 and period.')
    ip_list = [p.sub('0',i) for i in ip_list]   # <- substituting '0' for any non-digit
                                                # characters, so we can keep going
                                                # without raising any errors
    if not all([len(i)>0 for i in ip_list]):
        error_list.append('- Address contains empty segments. Use zero instead of ".."')
    if not all([int(i)<=255 if len(i)>0 else True for i in ip_list]):
        # ^Are the valid numbers (not empty strings) greater than 255
        error_list.append('- Address contains numbers greater than 255.')
    return error_list   # Returns a list containing the errors in the address.
                        # If it's empty, the address is valid.

def main():
    print('Running test cases now.')
    with open('test_cases/exercise_1.txt') as f:
        f.readline()
        for v,row in enumerate(f):
            print('Test case {}:'.format(v))
            row = row.strip('\n').split('     ')
            error_list = ip_checker(row[1])
            if len(error_list) == 0:
                assert row[2] == 'valid'
                print(row[1],'is a valid IP Address.')
            else:
                assert row[2] == 'invalid'
                print(row[1],'is an invalid IP address.')
            print('Passed.')
            print('---------------------')

if __name__ == '__main__':
    main()

#
