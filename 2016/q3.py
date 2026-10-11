def generateprimes(n):
  primes=[]
  for i in range(2,n+1):
    c=True
    for q in range(2,(int(i**(1/2)))+1):
       if i % q == 0:
          c=False
          break
    if c:
       primes.append(i)
  return primes
#print(generateprimes(100)

l, p, q = tuple(map(int, input().split()))


pow2=[]

count=1
while count  <= l:
  pow2.append(count)
  count*=2

def checkvalid(prime, listprime):
  approved=[]
  for i in listprime:
    if abs(prime-i) in pow2:
        approved.append(i)

  return approved

def findchain(firstp, lastp, listprime, writechain):
  curr_list=checkvalid(firstp, listprime)
  for i in range(len(curr_list)):
    print('????')

####???


