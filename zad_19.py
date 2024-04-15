def change_first_arg_in_tuple(tup,new_value):
    tup_as_list=list(tup)
    tup_as_list[0]=new_value
    new_tuple=tuple(tup_as_list)
    return new_tuple

example_tuple=(1,2,3)
changed_tuple=change_first_arg_in_tuple(example_tuple,4)
print(changed_tuple)

    

