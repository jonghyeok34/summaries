
constructors = {
}


def get_next_number(number: int):
    # digits = [int(x) for x in str(number).split()]
    total_number = number
    number_for_digit = number
    while number_for_digit > 0:
        total_number += number_for_digit % 10
        number_for_digit //= 10
    return total_number


for i in range(1, 10001):
    next_number = get_next_number(i)
    if constructors.get(next_number) is None:
        # print(next_number)
        constructors[next_number] = []
    constructors[next_number].append(i)

for i in range(1, 10001):
    # print self number
    if constructors.get(i) is None:
        print(i)
