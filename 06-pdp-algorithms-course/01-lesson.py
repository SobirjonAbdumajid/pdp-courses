def fibonacci_up_to_100():
    fib_sequence = []
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    while a <= 100:
        fib_sequence.append(a)
        a, b = b, a + b  # Update the values for the next iteration
    return fib_sequence

# Generate and print Fibonacci numbers up to 100
fib_numbers = fibonacci_up_to_100()
print(fib_numbers)