import numpy as np 

# a = np.array([1,2,3,4,5,6,7,8,9])
# a = np.array([[1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8]])
# print(a)
# print(np.maximum(a,2))

# print(a.T)

# #sigmoid
# a = 1/(1+ np.exp(-a))
# print(a[:,1])

# print(a.sum(axis=0))
# print(a.sum(axis=1))

# a = np.random.rand(5,1)
# print(np.dot(a,a.T))
# print(np.dot(a.T,a))

# b = np.array([1,2,3])
# b=b.reshape(3,1)
# print(b*b.T)

# a = np.random.randn(12288, 150) # a.shape = (12288, 150)
# b = np.random.randn(150, 45) # b.shape = (150, 45)
# c = np.dot(a,b)
# print(c.shape)


# a = np.random.randn(3, 3)
# b = np.random.randn(3, 1)

# c = a*b
# print(c.shape)

# c = np.dot(a,b)
# print(c.shape)


a = np.array( [[1,2],[3,4]] )
b = np.array( ([5,6],[0,7]) )
print(a)
print(b)

print(a*b)
print(np.dot(a,b))





