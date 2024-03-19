
import sys
import os

def main():
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        a = input("請輸入a:")
        b = input("請輸入b:")

    print("a:",a)
    print("b:",b)

    return a,b

if __name__ == "__main__":
    a,b = main()
    try: 
        c = a / b
        print(c)
    except:
        os.system("python sys_argv.py {} {}".format(a,b))
    