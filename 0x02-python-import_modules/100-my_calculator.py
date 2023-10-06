if __name__ == "__maine__":
 from  calculator_1 import add sub mul div
 from sys import argv
 if len(argv) != 4:
    print(Usage: ./100-my_calculator.py <a> <operator> <b>)
    return 1
 else :
    if argv[2] == "+":
         print("{} + {} = {}".format(argv[1], arg[3], add(argv[1],  arg[3])))
         return 0
    elif argv[2] == "*":
         print("{} * {} = {}".format(argv[1], arg[3], mul(argv[1],  arg[3])))
         return 0
    elif argv[2] == "-":
         print("{} - {} = {}".format(argv[1], arg[3], sub(argv[1],  arg[3])))
         return 0
    elif argv[2] == "/":
         print("{} / {} = {}".format(argv[1], arg[3], div(argv[1],  argv[3])))
         return 0
    else :
       print("Unknown operator. Available operators: +, -, * and /")
       return 1


