import random
import string

import quantumrandom

BLOCK_SIZE = 128
MAX_LENGTH = 1024
DEFAULT_NUMBER = 1
DEFAULT_LENGTH = 24
DEFAULT_POPULATION = string.ascii_lowercase + string.ascii_uppercase + string.digits


def rand(population = DEFAULT_POPULATION, number = DEFAULT_NUMBER, length = DEFAULT_LENGTH):
    quantum_data = quantumrandom.get_data(
        data_type='hex16',
        block_size=BLOCK_SIZE,
        array_length=number,
    )

    data = []

    for quantum_hex in quantum_data:
        random.seed(quantum_hex)
        data.append("".join([random.choice(population) for _ in range(length)]))

    return data
