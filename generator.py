#problem 1
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2
N = int(input())
squares = square_generator(N)
for square in squares:
    print(square)

#problem 2
def even_generator(n):
    for i in range(0, n+1):
        if i%2 == 0:
            yield i
def main():
    n = int(input())
    even_numbers = even_generator(n)
    print(', '.join(map(str, even_numbers)))

if __name__ == "__main__":
    main()

#problem 3
def num_generator(n):
    for i in range(0, n+1):
        if i%12 == 0:
            yield i
n = int(input())
numbers = num_generator(n)
for number in numbers:
    print(number)

#problem 4
def squares_generator(a, b):
    for i in range(a, b):
        yield i*i
a = int(input())
b = int(input())
squares = squares_generator(a, b)
for square in squares:
    print(square)

#problem 5
def reduced_generator(n):
    for i in range(n, 0, -1):
        yield i
n = int(input())
reduced = reduced_generator(n)
for reduce in reduced:
    print(reduce)
