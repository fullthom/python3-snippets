# This file shows how to import from a sub directory.

# Prints "c.py" so we know when the file in this code is run.
print("c.py")

# Imports the dir1.
# Code in dir1/__init__.py is run.
import dir1

# The commented out line raises an attribute error as dir1 has
# no attribute d. If we want to use this syntax we need
# to include the line "from . import d" in ./dir1/__init__.py
# dObj = dir1.d.D()

# Imports file "d.py" from dir1.
# If we didn't previously have "import dir1", then the code in
# "dir1/__init__.py" would also be run.
# Generally, this is preferred to "import dir1" if we aren't using
# the entire module.
from dir1 import d

# Imports class/function/variable D from "./dir1/d.py".
# If we didn't previously have "import dir1", then the code in
# "dir1/__init__.py" would be run here.
# If we didn't previously have "from dir1 import d", then the
# code in "/dir1/d.py" would be run here.
from dir1.d import D

# Instantiate the imported class
objD = D()

# Same as above, but imports multiple classes/functions/variables
# at the same time:
from dir1.d import D, some_variable, run

# Access the imported variable
print(some_variable)

# Access the imported function
print(run)
run()

# We can also use rename the imported objects:
import dir1 as dir2
from dir1 import d as e
from dir1.d import D as class_d
from dir1.d import some_variable as the_same_variable
from dir1.d import run as run2

# Instantiate the imported class
objD = class_d()

# Access the imported variable
print(the_same_variable)

# Note that when we print the function, it still says "<function run at 0x....>"
# as we only gave a new name to the local pointer to the function rather than
# actually copying the function.
print(run2)
run2()
