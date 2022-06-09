import random
passlen = int(input("Enter length of the password you want: "))
sample_text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
p = "".join(random.sample(sample_text,passlen ))
print(p)
