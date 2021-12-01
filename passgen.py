import string
import random

if __name__ == "__main__":

    t1 = string.ascii_letters
    t2 = string.ascii_lowercase
    t3 = string.ascii_uppercase
    t4 = string.digits
    t5 = string.punctuation
    

    plen = int(input("Enter The Length of password :"))

    s = []

    s.extend(list(t1))
    s.extend(list(t2))
    s.extend(list(t3))
    s.extend(list(t4))
    s.extend(list(t5))
    #s.reverse (reverse the list then make it more strong )
    random.shuffle(s)
    print("I am the saifullah. Create strong password here")
    print ("The Stong password which you need is Here :")
    #print("".join(random.shuffle(s, plen)))

    #print ("".join(random.sample(s, plen)))
    #print(s)
    print("".join(s[0:plen]))

    
    


    
    