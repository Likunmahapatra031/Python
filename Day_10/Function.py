def my_fun(f_name, l_name):
    if f_name =="" or l_name=="":
        return "You didn't provided valid inputs."
    my_fun_f_name=f_name.title()
    my_fun_l_name=l_name.title()
    return f"Result:{my_fun_f_name} {my_fun_l_name}"

print(my_fun(input("What is your first name ?"),
input("What is your last name ?")))

    