def binary2decimal(bitArray):
    intNumber = 0
    counter = 0
    for bit in bitArray[::-1]:
        intNumber += pow(2, counter)*bit
        counter += 1

    return intNumber