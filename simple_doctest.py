def my_function(a, b):
          """
          >>> my_function(2, 3)
          6
          >>> my_function('a', 3)
          'aaa'
          """

          return a * b

"""
To run the tests, use doctest as the main program via the -m option. Usually no output is produced while the tests are running, so the next example includes the -v option to make the output more verbose.

$ python3 -m doctest -v doctest_simple.py
"""