Building on the ideas from http://2e5.com/kite/parametric/
this library supports parametric CAD design based on polar vectors.

See http://en.wikipedia.org/wiki/Vector_notation#Polar_vectors

------
Vision:
------
The goal of this library is to emulate a manual design process. Doing the following programatically instead of manually enables parametric design.

The key decision for this library is the correct choice of abstraction. Basing all items on Polar Vectors allows great design freedom and concise implementation code.

-------
Testing:
-------
The file 'tests.txt' contain tests of all functionality in the library. In addition, each time
a design is created which relies on this library, it is a good idea to include the design in the test
file. This will ensure that future changes to the library will maintain backward compatibility 
with existing usage.

----
Todo:
----
- “inversion of control” later on to abstract CAD program when 2nd CAD target is made

