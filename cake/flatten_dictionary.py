

def flatten_dicionary(input_dict):
    flat_dict = {}
    flat_dict_helper(input_dict, flat_dict, '')
    return flat_dict

def flat_dict_helper(input_dict, flat_dict, initial_key):

    for key in input_dict:
        if isinstance(input_dict[key], dict):
            if initial_key == '':
                flat_dict_helper(input_dict[key], flat_dict, key)
            else:
                flat_dict_helper(input_dict[key], flat_dict, initial_key + '.' + key)
        else:
            if initial_key == '':
                flat_dict[key] = input_dict[key]
            else:
                flat_dict[initial_key + '.' + key] = input_dict[key]

one = {"d":"3", "e":"1"}
two = {"a":"2","b":"3","c":one}
main_dict = {"Key1":"1","Key2":two}

print flatten_dicionary(main_dict)


print ord('a') ^ ord('a')


def flattenHelper(dictionary, partial, res):
    for key in dictionary:
        # partial += key
        if isinstance(dictionary[key], dict):
            flattenHelper(dictionary[key], partial + key + ".", res)
        else:
            res[partial + key] = dictionary[key]
            # res[key] = value


def flattenDictionary(dictionary):
    res = {}
    flattenHelper(dictionary, "", res)
    return res
test = [1,2,3]

test[0], test[0] = test[0], test[0]
print test


