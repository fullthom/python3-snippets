# __init__.py means that the directory __init__.py is
# in is a module. The name must be exactly __init__.py.

# Usually, nothing is put into __init__.py.

# When any part of this module is imported, any code
# in __init__.py will be run first.

# Generally speaking however, as little code as possible
# should be run on import. Any initialization code should
# be run on the first use of a module. Otherwise, we
# waste a lot of cycles on things that might not even be needed
# depending on the client code's use. Especially bad is making
# I/O requests to the disk or network on import.
# We want things to import quickly!

print("./__init__.py")
