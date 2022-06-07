import random


#	Making A General GCD function 


def gcd(num1,num2):

    if num2 == 0: return num1

    else:

        return gcd(num2,num1%num2)



#	1. Picking a large random integer number in range of (1,10000). n = random.randint(1,10000)

while gcd(n,2310)!= 1:

    n = random.randint(1,10000)


print("Random Number (n): "+str(n))


#	2. Picking a random integer K such that x = 2310K + n is 100-bit long K = random.getrandbits(100)

x = 2310*K + n


print("K: "+ str(K)+" length:"+ str(len(str(K))))

print("x: "+ str(x)+" length:"+ str(len(str(x))))



###	3. Miller Rabin's Primality Test 
# 

def MillerRabinTest(p,a):



#	Base case - 1 not prime 

    if p == 1:

        return False
 
#	Base case - 2 is only prime 

    if p == 2:

        return True


#	Base case - Any even number not prime except for 2. if p % 2 == 0:

    return False



#Computes a^(n-1) mod n, using modular

#	exponentation by repeative squaring. m, k = p - 1, 0

while m % 2 == 0:

m, k = m // 2, k + 1


x = pow(a, m, p)


if x == 1 or x == p - 1:

return True


while k > 1:

x = pow(x, 2, p)

if x == 1:

return False

if x == p - 1:

return True

k = k - 1

return False


#	Method to call on Miller Rabin Test to check if number 'p' is prime or

#	not with witness a.

def isPrime(p):


#	'a': a witness number between 2 and 'p' for which we check if it

#	is relatively prime to a or not.

a	=random.randint(2,p-1)

if not MillerRabinTest(p,a):

return False

return True


##	Driver To Run the Code and Find Prime Number flag = True

num = 1 while (flag):
 
if (isPrime(x)):

print("Iteration "+str(num)+": "+str(x) +

"	is prime " + "length:"+str(len(str(x))));

print("k: "+str(K)) flag = False num+=1

else:

print ("Iteration "+str(num)+": "+str(x) + " is not prime")

K = random.getrandbits(10000)

x = 2310*K + n

isPrime(x)

num+=1
