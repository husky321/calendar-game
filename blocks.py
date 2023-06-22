import numpy

blocks = [
    numpy.array([[1, 1, 1], [1, 0, 0], [1, 0, 0],
                [1, 0, 0]], dtype=numpy.int32),
    numpy.array([[0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 1]], dtype=numpy.int32),
    numpy.array([[0, 1], [1, 1], [0, 1], [0, 1], [0, 1]], dtype=numpy.int32),
    numpy.array([[1, 0], [1, 0], [1, 0], [1, 0], [1, 1]], dtype=numpy.int32),
    numpy.array([[1, 0, 0], [1, 1, 1], [1, 0, 0],
                [1, 0, 0]], dtype=numpy.int32),
    numpy.array([[1, 0], [1, 0], [1, 0], [1, 1]], dtype=numpy.int32),
    numpy.array([[1, 1], [1, 1], [1, 0]], dtype=numpy.int32),
    numpy.array([[0, 0, 1, 1], [1, 1, 1, 0]], dtype=numpy.int32),
    numpy.array([[0, 1, 1], [0, 1, 0], [1, 1, 1]], dtype=numpy.int32)
]
