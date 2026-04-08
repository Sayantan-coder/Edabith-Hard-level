def count_datatypes(*data_types):
    int_count = 0
    str_count = 0
    bool_count = 0
    list_count = 0
    tuple_count = 0
    dictionary_count = 0
    if len(data_types) == 0:
        return [
            int_count,
            str_count,
            bool_count,
            list_count,
            tuple_count,
            dictionary_count,
        ]
    else:
        for data in data_types:
            if type(data) == int:
                int_count += 1
            elif type(data) == str:
                str_count += 1
            elif type(data) == bool:
                bool_count += 1
            elif type(data) == list:
                list_count += 1
            elif type(data) == tuple:
                tuple_count += 1
            elif type(data) == dict:
                dictionary_count += 1
            else:
                return f"{data} is not valid types of data . Data type must be in between int,str,bool,list,tuple,dict"
        return [
            int_count,
            str_count,
            bool_count,
            list_count,
            tuple_count,
            dictionary_count,
        ]


print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1))
print(count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))
print(
    count_datatypes(
        "Hello",
        "Bye",
        True,
        True,
        False,
        {"1": "One", "2": "Two"},
        [1, 3],
        {"Brayan": 18},
        25,
        23,
    )
)
print(count_datatypes(2, 5.8, True, "Sayantan"))
