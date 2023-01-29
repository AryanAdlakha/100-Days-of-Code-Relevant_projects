print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined = name1 + name2
lower_case_name = combined.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
true = t + r + u + e
love = l + o + v + e
true_score = str(true)+str(love)
print(f" {true_score}")
