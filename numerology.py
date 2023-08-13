import string

your_name = input("What is your full name? \n").replace(" ","").lower()
crush_name = input("What is your crush's full name? \n").replace(" ","").lower()

alphabets = list(string.ascii_lowercase)
counter = 0
dict = {}

for alphabet in alphabets:
    dict[alphabet] = counter + 1
    counter+=1

def name_count(name):
    
    i = 0
    for x in list(name):
        y=dict[x]
        i = i+y
    
    return i

your_count = name_count(your_name)
their_count = name_count(crush_name)

diff =round((1-(abs(your_count-their_count)/abs(your_count+their_count)))*100.0)
print(f"Your Compatibility Score is {diff}%!")
