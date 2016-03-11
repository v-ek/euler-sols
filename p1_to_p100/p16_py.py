def get_digit_sum(num):
    return sum([ int(char) for char in str(x) ])

x = 2**1000
print get_digit_sum(x)