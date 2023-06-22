import numpy
import copy
import blocks


def gen_variants(block):
    base = numpy.zeros((9, 6), dtype=numpy.int32)
    rotations = []
    for quad in range(4):
        rotations.append(numpy.rot90(block, quad))
    variants = []
    for block in rotations:
        block_on_base = copy.copy(base)
        block_on_base[0:block.shape[0], 0:block.shape[1]] = block
        for y_shift in range(base.shape[0]-block.shape[0]+1):
            variant_y = numpy.roll(block_on_base, y_shift, axis=0)
            for x_shift in range(base.shape[1]-block.shape[1]+1):
                variant_x = numpy.roll(variant_y, x_shift, axis=1)
                # generate all x and y flips of variant_x
                variant_x_flip_y = numpy.flip(variant_x, axis=0)
                variant_x_flip_x = numpy.flip(variant_x, axis=1)
                variant_x_flip_xy = numpy.flip(variant_x, axis=(0, 1))
                variants.extend([variant_x, variant_x_flip_y,
                                variant_x_flip_x, variant_x_flip_xy])
    return variants


def print_block(block):
    print('\n'.join([' '.join(str(x)) for x in block]))
    pass


def gen_variant_list(blocks):
    output = []
    for block in blocks.blocks:
        current = gen_variants(block)
        # find the unique blocks of q
        current_set = []
        for block in current:
            if not any(numpy.array_equal(block, x) for x in current_set):
                current_set.append(block)
        output.append(current_set)

    return output

# generate linear combinations of 9 output subsets from gen_variant_list and record the index of the block for each combination


def gen_combinations(variant_list):
    output = []
    for i in range(len(variant_list[0])):
        for j in range(len(variant_list[1])):
            for k in range(len(variant_list[2])):
                for l in range(len(variant_list[3])):
                    for m in range(len(variant_list[4])):
                        for n in range(len(variant_list[5])):
                            for o in range(len(variant_list[6])):
                                for p in range(len(variant_list[7])):
                                    for q in range(len(variant_list[8])):
                                        current = variant_list[0][i] + variant_list[1][j] + variant_list[2][k] + variant_list[3][l] + \
                                            variant_list[4][m] + variant_list[5][n] + \
                                            variant_list[6][o] + \
                                            variant_list[7][p] + \
                                            variant_list[8][q]
                                        output.append(
                                            [current, [i, j, k, l, m, n, o, p, q]])
    return output

# check if a given matrix is valid


def check_matrix(matrix):
    check = True
    # check if first two row are only one zeros and other are only one ones
    if (numpy.count_nonzero(matrix[0]) != 5 or numpy.count_nonzero(matrix[1]) != 5) and numpy.sum(matrix[0]) != 5 and numpy.sum(matrix[1]) != 5:
        check = False
    # check if the 3rd to 7th row has only one zero and other are only one ones
    for i in range(2, 7):
        if numpy.count_nonzero(matrix[i]) != 5 and numpy.sum(matrix[i]) != 5:
            check = False
    # check if the 8th to 9th row (has only one zero and zero is not at (7,1) (7,2) (8, 0) (8, 1)) and other are only one ones
    if (numpy.count_nonzero(matrix[7]) != 5 or numpy.count_nonzero(matrix[8]) != 5) and numpy.sum(matrix[7]) != 5 and numpy.sum(matrix[8]) != 5:
        check = False
    if matrix[7][1] == 0 or matrix[7][2] == 0 or matrix[8][0] == 0 or matrix[8][1] == 0:
        check = False
    return check


# main and record process time
if __name__ == '__main__':
    import time
    start_time = time.time()
    # generate all variants of blocks
    variant_list = gen_variant_list(blocks)
    # generate all combinations of variants
    combinations = gen_combinations(variant_list)
    # check if the combination is valid
    valid_combinations = []
    for combination in combinations:
        if check_matrix(combination[0]):
            valid_combinations.append(combination)
    # print the result
    print("There are " + str(len(valid_combinations)) + " valid combinations")
    end_time = time.time()
    print("The process time is " + str(end_time - start_time) + " seconds")
