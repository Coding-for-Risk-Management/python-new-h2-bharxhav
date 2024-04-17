import numpy as np
def FizzBuzz(start, finish):

    numvec = np.arange(start, finish+1)
    objvec = np.array(numvec, dtype=object)

    objvec[(numvec % 15 == 0)] = "fizzbuzz"
    objvec[(numvec % 3 == 0) & (numvec % 15 != 0)] = "fizz"
    objvec[(numvec % 5 == 0) & (numvec % 15 != 0)] = "buzz"

    return objvec

# unit test
# x = FizzBuzz(40,45)
# print(x[0])
# print(x[1])
# print(x[5])


