def bool_return():
    try:
        return True
    finally:
        return False
bool_return() # False

# more complicated example
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

print("####")
divide("2", "1")