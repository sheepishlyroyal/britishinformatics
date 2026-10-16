
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

l, p, q = tuple(map(int, input().split()))

powers_two = []
count=1
while count <= l:
   powers_two.append(count)
   count*=2

def get_children(n, prime_list):
  children = []
  for prime in prime_list:
     if abs(prime-n) in powers_two:
        children.append(prime)
  return children

prime=generate_primes(l-1)

def recur_calculate(n, height, checked):
  if q in n:
    return height

  child_list=[]
  for parent in n:
    for child in get_children(parent, prime):
      if child not in checked:
        child_list.append(child)
        checked.append(child)

  if child_list == []:
    return 0

  return recur_calculate(child_list, height+1, checked)

checked=[p]
print(recur_calculate([p], 1, checked))
