import unittest
#decorator:

def logger(func):
    def wrapper(n):
        print("Start processing")
        for val in func(n):
            yield val
        print("End processing")
    return wrapper

#generators:

def get_numbers(n):
    for i in range(1,n+1):
        yield i

def filter_even(gen):
    for value in gen:
        if (value%2==0):
            yield value

def square_numbers(gen):
    for value in gen:
        yield value**2

@logger
def pipeline(n):
    generated_numbers = get_numbers(n)
    even_numbers = filter_even(generated_numbers)
    squared_number = square_numbers(even_numbers)
    return squared_number


class Test_Realworld_mini_project(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(list(pipeline(10)),[4, 16, 36, 64, 100])
    def test_with_zero(self):
        self.assertEqual(list(pipeline(0)),[])
    def test_with_negative(self):
        self.assertEqual(list(pipeline(-5)),[])

if __name__=="__main__":
    user_input = int(input("Enter a number between 1-100: "))
    for val in pipeline(user_input):
        print(val)
    print(list(pipeline(user_input)))
    unittest.main()