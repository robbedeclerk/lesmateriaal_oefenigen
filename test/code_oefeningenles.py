def add(a,b):
    c=a+b
    return c

def reverse_string(a):
    return a[::-1]

def max_number(num1,num2):
    if num1 > num2:
        return num1
    elif num1<num2:
        return  num2
    else:
        return ('de nummers zijn even groot\n')

def is_even(getal):
    x = getal %2
    if x == 0:
        return ('getal is een even getal\n')
    else:
        return ('getal is een oneven getal\n')


def filter_even_numbers(x):
    even = []
    for item in x:
        if item%2==0:
            even.append(item)
        else:
            continue
    return even

def concatenate_strings(str1,str2):
    x = str1,str2
    return x

def is_prime(getal):
    for i in range(2,getal):
        if getal % i == 0:
            return ('getal is een prime getal\n')
    else:
        return ('getal is geen prime getal\n')

