'''import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[2,3,4]])
print(arr1)
print(arr2.shape)

#ndarray.ndmin(return the number of dimensions of the array)
import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([[1,2,3],[2,3,4]])
arr3=np.array([[[1,2,3],[2,3,4],[5,6,7]]])
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#ndarray.size(total count of elements in the array)
import numpy as np
arr =np.array([[1,2,3],[4,5,6,]])
print(arr.size)

#ndarry.dtype(returns the data type of elements)
import numpy as np
arr = np.array([1, 2, 3])
print(arr.dtype) 
arr_float = np.array([1.5, 2.3, 3.7], dtype=np.float32)
print(arr_float.dtype)

#ndarray.itemsize (Memory Size of Each Element)
#Returns the size (in bytes) of each element in the array
import numpy as np
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr.itemsize)

6. ndarray.nbytes (Total Memory Used by the Array)
Returns the total memory (in bytes) occupied by the array.
Formula: nbytes = size * itemsize'
arr = np.array([1, 2, 3], dtype=np.int32)
print(arr.nbytes)  # Output: 12 (since 3 elements × 4 bytes = 12 bytes)

7. ndarray.T (Transpose of the Array)
Swaps rows and columns (only useful for 2D or higher arrays).
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.T)'''

