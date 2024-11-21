list_is_prime=[]
list_is_factors=[]
list1=[]
# Step 1: Read the text file.
with open('numerical_data.txt', 'r') as file :
    data = file.read()
    datas = data.split()



# Step 2 : Extract prime numbers  calculate their factors.
def is_prime(n):
    # Check if a number is prime.
    k = 0
    if n < 2:
        return False
    else:
        for j in range(1, n + 1):
            if n % j == 0:
                k += 1
    if k == 2:
        return True

# Use list comprehension to extract prime numbers.
for mat in datas:
    if is_prime(int(mat.strip())):
        prime_numbers=int(mat.strip())

        list_is_prime.append(prime_numbers)


# step 3 calculate their factors.
def get_factors():
    for factor in list_is_prime:
        factors=(1,factor)
        list_is_factors.append(factors)
        print(factors)

get_factors()

#  Zip prime numbers with their factors and sort based on factors.
zip_p_and_f=zip(list_is_prime,list_is_factors)
sort_paris=sorted(zip_p_and_f)
print(tuple(zip_p_and_f))
print(sort_paris)



# step 4:Save the sorted pairs to a new text file.
with open('sorted.txt', 'w') as file2:
    file2.write(str(sort_paris))








