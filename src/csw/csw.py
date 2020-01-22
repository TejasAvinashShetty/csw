from warnings import warn


def crude_string_writer(cstrw_file_name, obj_list, obj_name_list):
    '''Write string variables to a file

    Basically a script file to reduce the drudgery of writing
    results, intermediate values to script files.

    obj      : list, ndarray, Qobj
               The object to be written

    obj_name : str
               Name of that object

    The place holder value in case
        - a name is forgotten is 'forgotten'
        - less objects more names is '42'

    Parameters
    ----------

    cstrw_file_name  : str
                    The name of the file in which the objects would be written

    obj_list      : list of str
                    The list containing all the objects to be written

    obj_name_list : list (containing only strings)
                    The list containing the names of the respective objects
                    in the obj_list.


    Returns
    -------
    None
    '''
    cstrw_file = cstrw_file_name + '.txt'
    if len(obj_list) == len(obj_name_list):
        pass
    else:
        warn('len(obj_list) != len(obj_name_list)')
        deficit_len = len(obj_list) - len(obj_name_list)
        if deficit_len > 0:
            for dl in range(deficit_len):
                obj_name_list.append('forgotten')
        else:
            for dl in range(abs(deficit_len)):
                obj_list.append(str(42))

    with open(cstrw_file, 'w') as cstrw:
        for obj, obj_name in zip(obj_list, obj_name_list):
            cstrw.write(obj_name)
            cstrw.write('\n')
            cstrw.write(obj)
            cstrw.write('\n\n')
            cstrw.write('\n\n')
            cstrw.write('\n\n')

    return None
