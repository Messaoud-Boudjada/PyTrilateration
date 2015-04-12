'''
The MIT License (MIT)

Copyright (c) 2015 Boudjada Messaoud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
# input tree points
x1 = input("x1 = ")
y1 = input("y1 = ")

x2 = input("x2 = ")
y2 = input("y2 = ")

x3 = input("x3 = ")
y3 = input("y3 = ")
# make the points in a 2d tuple if you want to use static points later
R1 = (x1,y1)
R2 = (x2,y2)
R3 = (x3,y3)
# you have to introduce the distances 
d1 = input("d1 = ")
d2 = input("d2 = ")
d3 = input("d3 = ")

# if d1 ,d2 and d3 in known
# calculate A ,B and C coifficents
A = R1[0]**2 + R1[1]**2 - d1**2
B = R2[0]**2 + R2[1]**2 - d2**2
C = R3[0]**2 + R3[1]**2 - d3**2
X32 = R3[0] - R2[0]
X13 = R1[0] - R3[0]
X21 = R2[0] - R1[0]

Y32 = R3[1] - R2[1]
Y13 = R1[1] - R3[1]
Y21 = R2[1] - R1[1]

x = (A * Y32 + B * Y13 + C * Y21)/(2.0*(R1[0]*Y32 + R2[0]*Y13 + R3[0]*Y21))
y = (A * X32 + B * X13 + C * X21)/(2.0*(R1[1]*X32 + R2[1]*X13 + R3[1]*X21))
# prompt the result
print "(x,y) = ("+str(x)+","+str(y)+")"
