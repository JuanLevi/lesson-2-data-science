import numpy as np

list1=[9,1,63,8,23]
print(list1)

list = np.array(list1)


print(list[0:3])
print(list[:4])
print(list[::2])
print(list[::-1])

numArray=np.arange(1,50)
print(numArray)

reshapeArray=numArray.reshape(7,7)
print(reshapeArray)

sliceArray=reshapeArray[2:5,2:5]
print(sliceArray)



tenArray=np.arange(1,11)

evenArray=tenArray[tenArray%2==0]
print(evenArray)

oddArray=tenArray[tenArray%2==1]
print(oddArray)

all5Array=tenArray[tenArray>5]
print(all5Array)


tenArray+=1
print(tenArray)

tenArray= tenArray*5
print(tenArray)


print(tenArray[[1,7]]) # in print -> index double bracket


random1Array=np.random.permutation(np.arange(5,21))
reshape1Array=random1Array.reshape(4,4)
print(reshape1Array)

random2Array=np.random.permutation(np.arange(27,43))
reshape2Array=random2Array.reshape(4,4)
print(reshape2Array)


print(reshape1Array-reshape2Array)

def equationArray(array):
    return 2*array+3

def equation2Array(array):
    return 2*array**2-3*array+5

y=equationArray(tenArray)
y2=equation2Array(tenArray)
print(y)
print(y2)