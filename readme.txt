Building on the ideas from http://2e5.com/kite/parametric/
this library supports parametric CAD design based on polar vectors.

See http://en.wikipedia.org/wiki/Vector_notation#Polar_vectors

The goal of this library is to emulate a manual design process. Doing the following programatically instead of manually enables parametric design:

- 14 LE bridle points, 2 TE bridle points (in same bridle) -> 13 LE segments: 1 center, 6 per side
- stack 7 segments (array command)
- clip off at an angle to create shorter segments toward tips, length range: [16-10] lr
- choose a segment incidence angle to create LE curve: [5°] ia
- rotate segments into their final angle: grab 6, rotate by ia, grab 5 rotate, etc.
- choose a notch wall length: [8] nw
- choose a notch angle: [8°] na (greater or equal to segment incidence angle ia)
- make 7 notches total (array command) 
- scale notches so smaller toward end, range: [100%-70%] -> 100, 95, 90, 85, 80, 75, 70% sn
- choose mid and tip notch rotation angle: [8°,74°] sr, er (should follow tension vector from bridle point, see wrinkle in canopy)
- rotate all notches by sr (11°)
(74-8)/6=11 nr,  so rotate each notch an additional 10° using the same segment grab and rotate procedure
choose a tip width, tw, probably less than last segment length: [8]

The key decision for this library is the correct choice of abstraction. Basing all items on Polar Vectors allows great design freedom and concise implementation code.

Todo:
- move testing code to own file
- “inversion of control” later on to abstract CAD program when 2nd CAD target is made
- each time a new design is made, output from that design is made part of the test
    in this way, we can guarantee that any future changes are backwards compatible
