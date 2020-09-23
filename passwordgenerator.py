
import random


s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 50
p =  "".join(random.sample(s,passlen ))
print(p)
f = open('password.txt', 'w')
f.write(p)