# module -> it is a file that contains Python code - functions, classes, or variables - that you can use  in other files

# 1. Built-in Modules -> already included in Python
from math import sqrt
print(sqrt(16))

# written above is as same as writing this
import math
print(math.sqrt(16))

# 2. Creating my own module
import mymodule
print(mymodule.greet("Jack"))

# 3. External Modules -> need to be installed using pip
import requests # this module is used to fetch the HTML of online pages
response = requests.get("https://api.github.com/")
print(response.status_code)