class InvalidPasswordException(Exception):
    pass

try:
    p = (input(("Enter the Password: ")))
    if (len(p) <8):
        raise InvalidPasswordException
except InvalidPasswordException:
    print("Length of your password (", p, ") is ", len(p), ". Kindly re-enter more than 8.")
finally:
    print("End of Program.")