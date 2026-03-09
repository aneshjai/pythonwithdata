


def tax_calculate(type,a,b):
    if type == "add":
        print("adding")
        return  a+b
    elif type=="subtract":
        print("subtratcing")
        return a-b
    elif type=="multiply":
        return a*b
    elif type =="divide":
        return  a/b


if __name__ == "__main__":
    hra = 10
    bp= 5
    tax= 3

    gross_result = tax_calculate("add", hra,bp)
    salary   = tax_calculate("subtract",gross_result,tax)
    net_salary = tax_calculate("multiply",salary,12)
    print(net_salary)


    x= int(input("Bill Amount: "))

    print(x, type(x))


    print("Hello")
