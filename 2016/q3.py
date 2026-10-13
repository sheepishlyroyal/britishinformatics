def generate_primes(n):
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

powers_two = []
count=1
while count <= l:
   powers_two.append(count)
   count*=2


def get_children(n, prime_list):
  # being all primes under l that fit n+2^k
  children = []
  for prime in prime_list:
     if abs(prime-n) in powers_two:
        children.append(prime)

  return children

def cleanup(array):
  clean=[]
  for i in array:
    clean += i
  return list(set(clean))



prime_list=generate_primes(l)
child_primes=get_children(p, prime_list)
iterations = 2 # 1 coming from child_primes pre, 2 coming from 1 iteration not counting.
while q not in child_primes:

  iterations += 1
  child_primes=cleanup([get_children(newprime, prime_list) for newprime in child_primes])


   
  


print(iterations)
