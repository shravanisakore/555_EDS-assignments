import numpy as np
f1 = np.genfromtxt("/content/testmarks1.csv",delimiter=",")
print(f1)
r=f1[1:,1]
print(r)
print(type(r))
print(max(r))
f2 = np.genfromtxt("/content/testmarks2.csv",delimiter=",")
print(f2)
print(f1)
print(f2)
#SUBSTRACT
result=f1-f2
print("Using operator",result)
result=np.subtract(f1,f2)
print("Using Numpy function", result)
#ADDITION
addition=f1+f2
print("Using Operator",addition)
addition=np.add(f1,f2)
print("USing Numpy function",addition)
#MULTIPICATION
multiply=f1*f2
print("Using operator",multiply)
multiply=np.multiply(f1,f2)
print("Using Numpy fuction",multiply)
#DIVISON
div=f1/f2
print("Using operator",div)
div=np.divide(f1,f2)
print("Using Numpy operator",div)
#MODULAS
mod=f1%f2
print("Using operator",mod)
mod=np.mod(f1,f2)
print("Using Numpy operator",mod)
mod=np.hstack((f1,f2))
mod
#VERTICAL_STACKING
mod=np.vstack((f1,f2))
mod
#RANGE
arr=np.arange(800,810,1)
print(arr)
#STATISTICAL OPERATION
print("Standard derivation",f1.std())
print("min=", f1.min())
print("max=", f1.max())
print("sum=", f1.sum())
print("product=", f1.prod())
#ARITHMETIC OPERATION
print("\nADDITION\n",np.add(f1,f2))
print("\nSUBSTRACT\n",np.subtract(f1,f2))
print("\nMULTIPLICATION\n",np.multiply(f1,f2))
print("\nDIVISION\n",np.divide(f1,f2))
#coping and viewing
x = arr.view()#viewing
arr[0] = 42
print(arr)
print(x)
#coping
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
#Mean median and mode
import numpy
mean = numpy.mean(arr)
print("Mean=",mean)
median=numpy.median(arr)
print("Median",median)
from scipy import stats
mode = stats.mode(arr)
print(mode)
#BITWOSE OPERATOR
a=60
b=40
print("Binary of a ",bin(a))
print("Binary of b ",bin(b))
print("Bitwise a and b ",np.bitwise_and(a,b))
print("Bitwise a or b",np.bitwise_or(a,b))
print("Bitwise a xor b",np.bitwise_xor(a,b))
