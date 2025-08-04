'''import numpy as np
arr = np.array([1,2,3,4])
print(arr)

import numpy as np
arr = np.array([1,2,3,4])
print(arr[2])

import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr)

import numpy as np
arr = np.array([[[1,2],[3,4],[3,5]]])
print(arr)

import numpy as np
arr = np.array([1,2,3],ndmin=5)
print(arr)

import numpy as np
arr=np.array([1,2,3])
arr1=np.array([1,2,3])
print(arr+arr1)

import numpy as np
arr=np.array([[1,2,3],[2,3,4]])
arr1=np.array([[1,2,3],[4,5,6]])
print(arr+arr1)

import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr[1][1])

import numpy as np
arr = np.array([[[1,2,3],[3,4,5],[6,7,8]]])
print(arr[0][2])

import numpy as np
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr[0][1])

import numpy as np
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr[::-1])

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3,1)
print(newarr)

import numpy as np
arr=np.array ([1,2,3])
for x in arr:
    print(x)

import numpy as np
arr=np.array ([[[1,2,3],[4,5,6],[3,5,6]]])

for row in arr:
    print(row)

import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.concatenate((arr1,arr2),axis=0)
print(result)

import numpy as np
arr1=np.array([[1,2,3,4]])
new_arr=np.array_split(arr1,4)
print(new_arr)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(arr==10)
print(x)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(arr%2==0)
print(x)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(arr<5)
print(x)

import numpy as np
arr=np.array([6,7,2,7,1,2])
x=np.sort(arr)
print(x)'''

import numpy as np
arr=np.array(['vaishu','tanu','harshi'])
x=np.sort(arr)
print(x)




