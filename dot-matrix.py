def matrix_dot_vector(a, b):
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    import numpy as np
    a = np.array(a)
    b = np.array(b)
    print(a,b)
    if a.shape[0] == b.shape[-1]:
        return a.dot(b)
    else:
        return -1
a = [1,2]
b = [
        [1,2],
        [3,4]
        ]

matrix_dot_vector(a,b)

