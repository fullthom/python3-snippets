# Imports the file "b".
# When "b" is imported, any code in "b" is run.
import b

# Runs the function "run" in file b
b.run()

# Imports the file "b", but gives a new name to access it from
# You'll see this in code that uses the library numpy a lot:
# "import numpy as np".
# Because we previously imported the entire file "b" above,
# code in "b" is not run a second time.
import b as b2

# Runs the function "run" in file b again:
b.run()

# Imports the specific class "B" from file "b".
# If this was the first import, any code in "b" would be
# run here like it was above, even though we are only importing
# the classes. Try it out by commenting out all of the above code
# and run this file and verify that it printed "b.py".
from b import B

# Instantiates a B object
bObj = B()

# Prints "a.py" so we know when the file in this code is run.
print("a.py")

# Because we used __init__.py to declare this directory a module,
# we can use this to import a too. The "." signifies that we
# are importing from the same directory.
# Beginning in python3.8 this will raise an ImportError if you
# attempt to run a.py directly.
from . import b
