def do_fizzbuzz(n):
    for i in range(n+1):
        if i%3==0 and i%5==0:
            print(i, ": fizzbuzz")
        elif i%3==0:
            print(i, ": fizz")
        elif i%5==0:
            print(i, ":buzz")
        else:
            print(i)

def init():
    num = input("Enter the number: ")
    do_fizzbuzz(int(num))

if __name__=="__main__":
    init()
