import math

nth_term_of_the_fibonacci_sequence = (
    lambda x: (((1 + math.sqrt(5)) / 2) ** x) / 5**0.5
)
print(nth_term_of_the_fibonacci_sequence(3))
