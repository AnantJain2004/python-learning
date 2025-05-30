import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="operation to perform")

args = parser.parse_args()

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")

elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")

elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")

elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")

else:
    print(f"Invalid Operation")