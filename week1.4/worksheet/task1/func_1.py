
def func_1(lst_value): 
    ''' 
    This function takes a list as an argument 
    and then calculates there mean average. 
    ''' 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 