import numpy as np
import pandas as pd

# Basic idea, create tables translating ones, tens, hundreds as dicts, thousands
# as dicts, input ands as appropriate
def convert_to_english(num):
    ones_dict = {
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six' ,
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
    }
    teens_dict = {
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
    }
    tens_dict = {
        20 : 'twenty',
        30 : 'thirty',
        40 : 'forty',
        50 : 'fifty',
        60 : 'sixty',
        70 : 'seventy',
        80 : 'eighty',
        90 : 'ninety',
    }
    hundreds_dict = {
        100 : 'one hundred',
        200 : 'two hundred',
        300 : 'three hundred',
        400 : 'four hundred',
        500 : 'five hundred',
        600 : 'six hundred',
        700 : 'seven hundred',
        800 : 'eight hundred',
        900 : 'nine hundred',
    }
    thousands_dict = {
        1000 : 'one thousand'
    }

    """ idea: convert to string, check length, match appropriate, and add and between as needed
    """

    num_str = str(num)
    length = len(num_str)

    thousands = 0
    hundreds = 0
    teens = 0
    tens = 0
    ones = 0
    if length == 4:
        thousands = int(num_str[0]) * 1000
        hundreds = int(num_str[1]) * 100
        if num_str[-2:] > '19':
            tens = int(num_str[2]) * 10
            ones = int(num_str[3])
        else: 
            teens = int(num_str[-2:])

    elif length == 3:
        hundreds = int(num_str[0]) * 100
        if num_str[-2:] > '19':
            tens = int(num_str[1]) * 10
            ones = int(num_str[2])
        elif num_str[-2:] > '09': 
            teens = int(num_str[-2:])
        else:
            ones = int(num_str[2])

    elif length == 2:
        if num_str > '19':
            tens = int(num_str[0]) * 10
            ones = int(num_str[1])
        elif num_str > '09': 
            teens = int(num_str)
        else:
            ones = int(num_str[1])

    elif length == 1:
        ones = int(num_str)
    """
    if thousands:
        print 'thousands'
        print thousands
    if hundreds:
        print 'hundreds'
        print hundreds
    if teens:
        print 'teens'
        print teens
    if tens:
        print 'tens'
        print tens
    if ones:
        print 'ones'
        print ones
    """

    number_text = ''

    # Thousands
    try:
        thousands_text = thousands_dict[thousands]
    except Exception, e:
        thousands_text = ''
    
    # Hundreds
    try:
        hundreds_text = hundreds_dict[hundreds]
    except Exception, e:
        hundreds_text = ''

    # Tens
    try:
        tens_text = tens_dict[tens]
    except Exception, e:
        tens_text = ''
    
    # Teens
    try:
        teens_text = teens_dict[teens]
    except Exception, e:
        teens_text = ''

    # Ones
    try:
        ones_text = ones_dict[ones]
    except Exception, e:
        ones_text = ''

    if hundreds_text:
        if teens_text:
             number_text = hundreds_text + ' and ' + teens_text
        elif tens_text:
            if ones_text:
                number_text = hundreds_text + ' and ' + tens_text + '-' + ones_text
            else:
                number_text = hundreds_text + ' and '  + tens_text
        elif ones_text:
            number_text = hundreds_text + ' and ' + ones_text
        else:
            number_text = hundreds_text
    elif teens_text:
        number_text = teens_text
    elif tens_text:
        if ones_text:
            number_text = tens_text + '-' + ones_text
        else:
            number_text = tens_text
    elif ones_text:
        number_text = ones_text
    elif thousands_text:
        number_text = thousands_text

    return number_text.strip()

def letters(num):
    return ''.join(filter(str.isalpha, num))

total_length = 0
for ii in range(1,1001):
    curr_text = convert_to_english(ii)
    cleaned_text = letters(curr_text)
    curr_len = len(cleaned_text)
    total_length += curr_len
    print ii
    print curr_text
    print cleaned_text
    print curr_len
    print total_length
    if ii % 100 == 0:
        variable = raw_input('input something!: ')

print total_length