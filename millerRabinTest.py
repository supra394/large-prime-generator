import math
import random


#miller_rabin method shows if we have a possible prime 'n' for the given 'a'
def miller_rabin(n, a):
    exp = n - 1
    
    if(n%2 == 0):
        return False
        

    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n ) == 1:
        return True
        
    while exp < n - 1:
        if pow(a, exp, n) == -1:
            return True
        exp <<= 2

    return False


#this method calls the miller_rabin method but for different values of a to ensure that miller rabin test is indeed returning true for primes
def different_a_test(n):

    for i in range(20):
        a = random.randint(2, n-1)          #picking a random integer "a" between 1 and n-1 
        if (miller_rabin(n, a) == False):
            return False
    return True


    
#this method picks a random value for n for the equation x = 2310K + n where gcd(n, x) = 1
def pickRand():

    ## Set gcd flag to false
    gcdFlag = False

    ## Loop until gcd(n, 2310) = 1
    while (not gcdFlag):

        ## Generate a random int
        n = random.randint(1, 10000)

        ## Check if gcd of n and 2310 = 1
        if (math.gcd(n, 2310) == 1):
            gcdFlag = True
            
    ## Return the random integer such that gcd(n, 2310) = 1 
    return n 


#this method calculates the value of x from the n calculated from above, and then calls the different_a_test(x) method to check if it;s a prime.
def check_prime():

    n = pickRand()
    found = False
    listK = []
    lRange = (math.pow(2,100) - 9999)/2310
    hRange = (math.pow(2,101) - 1)/2310

    #while we don't have a prime, we take a different value of k and then add that value to the list, we will get a new value of x which will be checked for
    #different value of a as well
    while found == False:
        k = random.randint(lRange, hRange)
        listK.append(k)
        x = 2310*n + k
        a = random.randint(2, n-1)
        if(miller_rabin(x, a) == False):
            continue                 #if the number is not a possible prime, then we get a different number
        else:
            if(different_a_test(x)):
                found = True            #the loop stops executing after we get a prime
    print(x, " is possibly a prime number we got after trying ", len(listK), " tries for K.")
    
    #print (listK)
    #return listK


check_prime()



def largePrime(numBits):
   found = False
   while found == False:
       possiblePrime = random.getrandbits(numBits)
       if(different_a_test(possiblePrime)):
           found = True
           return possiblePrime

print("A 1000 bit long orime number could be ", largePrime(1000))