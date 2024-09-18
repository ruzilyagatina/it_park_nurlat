max_d = float('-inf')
r = []
A_n = 9*21**8 + 4*21**7 + 3*21**6 + 6*21**5 + 9*21**4 + 7*21**3 + 2*21**1 + 1
B_n = 2*21**5 + 9*21**3 + 2*21**2 + 5*21**1 + 3 

for x in range(21):
  for y in range(21):
    A = A_n + x*21**2
    B = B_n + y*21**4
    if (A-B) % 20 == 0 and x-y > max_d:
      max_d = x - y
      r = [(A-B) // 20]
     elif (A-B) % 20 == 0 and x-y == max_d:
       r += [(A-B) // 20]
 print(*r)