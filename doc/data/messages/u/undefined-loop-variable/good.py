def find_even_number_1(numbers):
    for x in numbers:
        if x % 2:
            return x
    return None

def find_even_number_2(numbers):
    for x in numbers:
        if x % 2:
            break
    else:
        return None

    return x
