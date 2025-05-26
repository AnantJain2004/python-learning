# *args and **kwargs are very important in python, especially when working with functions that accept a variable number of arguments
# ● **kwargs - Variable Keyword arguments
#              ∘ it lets you pass any number of keyword arguments
#              ∘ internally, kwargs is a dictionary of key-value pairs 

def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(anant = 100, ritish = 90, ashwin = 80, medhansh = 70, shivam = 60)