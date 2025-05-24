while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter seconf number: "))
        print(f"The division is {a/b}")

    except ValueError:
        print("Please dont perfrom bad typecasts!")

    except ZeroDivisionError:
        print("Please dont divide by zero!")

    except Exception as e:
        print("Some error occurred!", e)