from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('/matrices')
def generate_and_multiply_matrices():
    matrix_a = np.random.randint(0, 101, size=(10, 10))
    matrix_b = np.random.randint(0, 101, size=(10, 10))

    product = np.dot(matrix_a, matrix_b)

    return {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "product": product.tolist(),
    }

@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}
