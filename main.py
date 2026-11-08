import hebb
import file_handling
import test


def initialize():
    """
    this function is the core of the program
    :return: the weights of the neural network
    """
    # reading the input files and extracting the inputs for teaching the neural network
    input_files_path_location = "inputs.txt"
    input_files_paths = file_handling.input_file(input_files_path_location)
    inputs = []
    for i in input_files_paths:
        inputs.append(file_handling.read_teaching_input(i))

    # teaching the neural network
    my_hebb = hebb.Hebb(inputs)
    weights = my_hebb.weight
    weight_bios = my_hebb.weight_bios
    weights.append(weight_bios)

    return weights


def shape_calculation(shape: list, weights: list):
    """
    :param shape: an input that we want to check in the neural network to check its classification
    :param weights: the weights of the neural network
    :return: yes or no answer
    """
    # fix the structure of the input
    for i in range(0, len(shape)):
        shape[i] = file_handling.variable_structuring(shape[i])

    # calculate
    stop = len(shape) - (len(weights) - 1)
    answer = 0

    if stop <= 0:
        for i in range(0, len(shape)):
            answer += shape[i] * weights[i]
    elif stop > 0:
        for i in range(0, len(weights) - 1):
            answer += shape[i] * weights[i]

    answer += weights[len(weights) - 1]

    return answer


def main():
    # creating the neural network
    weights = initialize()
    print("this is the weights after teaching the neural network: ")
    for i in range(0, len(weights) - 1):
        print(weights[i], end="")
        print("(" + "x" + str(i) + ")", end=" + ")
    print(weights[len(weights) - 1])

    print("\n.........................................\n")

    # testing x and o
    x_test = shape_calculation(test.x, weights)
    print("x is", x_test)
    x_test = shape_calculation(test.o, weights)
    print("o is", x_test)

    print("\n.........................................\n")

    # testing other inputs
    x_test = shape_calculation(test.other1, weights)
    print("other1 is", x_test)
    x_test = shape_calculation(test.other2, weights)
    print("other2 is", x_test)
    x_test = shape_calculation(test.other3, weights)
    print("other3 is", x_test)
    x_test = shape_calculation(test.other4, weights)
    print("other4 is", x_test)
    x_test = shape_calculation(test.other5, weights)
    print("other5 is", x_test)
    x_test = shape_calculation(test.other6, weights)
    print("other6 is", x_test)

main()