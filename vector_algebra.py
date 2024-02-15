# file: vector_algebra
# funtions: scalar(), magnitude(), addition(), dotProduct(), crossProduct(), unitVector()

# scalar(): returns the product of a scalar and a vector (vector)
def scalar(scalar, vec):
    if not vec:
        return []
    
    for pos in range(len(vec)):
        vec[pos] = scalar*vec[pos]

    return vec

# magnitude(): returns the Euclidean magnitude of the vector (scalar)
def magnitude(vec):
    mag = 0

    for pos in range(len(vec)):
        mag += pow(vec[pos], 2)

    return pow(mag, .5)


# addition(): returns the summation of an unspecified number of vectors (vector)
def addition(*vec):
    if not vec:
        return []
    
    vecLength = set(len(v) for v in vec)
    if len(vecLength) > 1:
        raise ValueError("Vectors must be of the same dimension!")

    summation = [sum(pos) for pos in zip(*vec)]
    return summation

# dotProduct(): returns the dot product of two vectors (scalar)
def dotProdcut(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of the same dimension!")
    
    dProduct = 0

    for pos in range(len(v1)):
        dProduct += v1[pos]*v2[pos]

    return(dProduct)

# crossProduct(): returns the cross product of two vectors (vector ⊥ to v1, v2)
def crossProduct(v1, v2):
    if len(v1) !=3 or len(v2) !=3:
        raise ValueError("Vectors must be three-dimensional!")
    
    cProduct = [
        v1[1]*v2[2]-v1[2]*v2[1],
        v1[2]*v2[0]-v1[0]*v2[2],
        v1[0]*v2[1]-v1[1]*v2[0]
    ]

    return cProduct

# unitVector(): returnt the unit vector of the given vector (vector)
def unitVector(vec):
    if not vec:
        return []
    
    mag = magnitude(vec)

    for pos in range(len(vec)):
        vec[pos] = vec[pos]/mag
    
    return vec


# testing
vecTest = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9],
    [-10, -11, -12],
    [0, 0, 0],  # Origin
    [1.5, 2.5, 3.5],  # Non-integer coordinates
    [2, -3, 1],  # Mixed positive and negative coordinates
    [0.5, 0.5, 0.5],  # Uniformly distributed coordinates
    [10, 0, 0],  # Along x-axis
    [0, 10, 0],  # Along y-axis
    [0, 0, 10],  # Along z-axis
    [-10, 0, 0],  # Along -x-axis
    [0, -10, 0],  # Along -y-axis
    [0, 0, -10],  # Along -z-axis
]

#print(addition(vecTest[0], vecTest[1], vecTest[4], vecTest[5]))
#print(addition(vecTest[0], vecTest[4]))
#print(scalar(-1, vecTest[0]));
#print(magnitude(vecTest[0]))
print(unitVector(vecTest[0]))