import numpy as np
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    # len_of_vector = np.sqrt(np.sum(vector ** 2))
    return len_of_vector

def compute_dot_product(vector1, vector2):
    result = vector1.dot(vector2) # --> it's okay
    # result = np.dot(vector1, vector2)
    # result = vector1 @ vector2
    return result

def matrix_multi_vector(matrix, vector):
    # result = matrix.dot(vector) 
    result = np.dot(matrix, vector)
    return result

def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def compute_cosine(vector1, vector2):
    cos_sim = np.dot(vector1, vector2) / (compute_vector_length(vector1) * compute_vector_length(vector2))
    return cos_sim

def main():
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([-100, -100, 3])
    print(compute_dot_product(vector1, vector2))
    
if __name__ == "__main__":
    main()