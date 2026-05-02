import unittest
def logger(func):
    def wrapper(n):
        print("Start processing")
        for value in func(n):
            yield value
        print("End processing")
    return wrapper

@logger
def get_numbers(n):
    for i in range(1,n+1):
        yield i

def filter_even(gen):
    for value in gen:
        if (value%2==0):
            yield value



class testing(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(list(get_numbers(2)),[1,2]) 

    def test_filter_even(self):
        gen = get_numbers(12)
        self.assertEqual(list(filter_even(gen)), [2,4,6,8,10,12])

if __name__ == "__main__":
    user_input = int(input("Enter a number between 1-100: "))
    gen = get_numbers(user_input) #gen is single use function once the value is printed there is no value left for gen2 to use in its generator
    
    gen2 = filter_even(gen)
    print (list(gen))
    print(list(filter_even(get_numbers(user_input))))
    unittest.main()
    