def product(input_list):
    if len(input_list) < 2:
        raise IndexError("Length of input list must be greater than 1")

    product_list = [None] * len(input_list)

    #product before index
    running_product = 1
    for i in range(len(input_list)):
        product_list[i] = running_product
        running_product *= input_list[i]

    running_product = 1
    for i in range(len(input_list)-1,-1,-1):
        product_list[i] *= running_product
        running_product *= input_list[i]

    #multiply by product after index
    return product_list


print product([1,4,3,6,2])