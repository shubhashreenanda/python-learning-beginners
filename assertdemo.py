try:
    num = int(input("enter an even number:"))
    assert num%2==0, "You have entered an invalid input or odd number"

except AssertionError as obj:
    print(obj)

print("After assertion")