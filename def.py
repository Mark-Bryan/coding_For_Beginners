global_var = 1
def my_vars():
    print('Global variable:', global_var)

    local_var = 2
    print('Local variable:', local_var)
    global inner_var
    inner_var = 3

my_vars()
print('Second Global:', inner_var)