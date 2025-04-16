lucky_num = int(input("Enter a number between 1 and 10: "))

match lucky_num:
    case 1:
        print("You won a headphone")
    case 3:
        print("You won a powerbank")
    case 6:
        print("You won a smartphone")
    case _:
        print("Better luck next time")