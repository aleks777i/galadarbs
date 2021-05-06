def countInterest(deposit, term, rate):
    sum = deposit
    for i in range(0, term-1):
        sum = sum * rate
    return sum - deposit


print(countInterest(1000, 2, 1.05))