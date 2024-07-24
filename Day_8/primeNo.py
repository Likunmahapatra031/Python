def prime_checker(number):
    is_prime=True
    for i in range(2,number):
       if number % i == 0:
        is_prime=False     
    if is_prime:
        print("It's a prime.")
    else:
        print("It's not a prime no.")
n=int(input("Enter a no..\n"))
prime_checker(number=n)


