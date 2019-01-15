num = int(input("Enter a number: ")) #prompt user to enter a number
def collatz_conjecture(n):
    while n != 1:
        if n % 2 == 0: # if n is even
            n = n / 2  # do
            print (n)
        else:            #check if number is odd
            n = (3*n + 1)
            print(n)

collatz_conjecture(num) #call function
