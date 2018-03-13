count_calls = 0
count_interation = 0

def fact_prime_loop(n):
    global count_interation
    i = 2
    while i <= n:
        if n % i == 0:
            print(i ,end = " ")
            n = n / i
        else: i = i + 1
        count_interation += 1
def fact_prime_recursion(n):
    if n == 1 or n == 2:
        print(n)
    else:
        i += 1

i = 2

def fact_prime_recursion(n):
    global count_calls 
    global i
    count_calls += 1
    if n == 1:
        return
    elif n % i == 0:
        n = n / i
        print(i, end = ' ')
        return (fact_prime_recursion(n))
    else:
        i = i +1
        return(fact_prime_recursion(n))



n = int(input("Input number (to get prime factors): "))
fact_prime_recursion(n)
print()
fact_prime_loop(n)
print()
print("count of iteration with loop",count_interation)
print("count of calls ",count_calls)
#n = int(input(("Input number : ")))
        
