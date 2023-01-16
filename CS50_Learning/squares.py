# with python, we can not use a function without declaring or importing in another file
from functions import square
for i in range(8):
    print(f"The square of {i} is {square(i)}")
    