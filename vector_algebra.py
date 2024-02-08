# vector_algebra

# addition(): returns the summation of an unspecified number of vectors
def addition(*vec):
    if not vec:
        return []
    
    vecLength = set(len(v) for v in vec)
    if vecLength > 1:
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