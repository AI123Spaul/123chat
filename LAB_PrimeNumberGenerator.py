# Python Program to Generate Prime Numbers up to a Specified Number
def generate_primes(limit):
    prime_list = []

    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
            is_prime = False
            break
        if is_prime:
            #print(num)
            prime_list.append(num)
    return prime_list
# Main program
if __name__ == "__main__":
    try:
        limit = int(input("Suvadip requests to enter the upper limit to generate prime numbers: "))
        if limit < 2:
            print("Prime numbers start from 2. Suvadip requests to please enter a number greater than 1.")
    else:
        primes = generate_primes(limit)
        print(f"Prime numbers up to {limit}: {primes}")
    except ValueError:
        print("Invalid input. Suvadip requests to please enter a valid integer.")