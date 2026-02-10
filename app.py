""" # Discount kinda works

resident=input("Are you a citizen?")
if resident == ("Yes"):
    print (True)
else :
    print (False)
    
child=int(input("How Old Are You?"))
   
if child == (1-12):
     print(True)
else :
     print (False)
     
member=input("Do you have an active Membership?") 

if member == ("Yes"):
    
    print(True) 
else : 
    print (False)
if member or child or resident ==True:
    print("give discount")
else : 
    print("Pay full price") """


#Odd and Even Game Works!
""" Guess=int(input("Pick a Number:"))
if Guess % 2 == 0:
        print ("Even")
else :
        print("Odd") """
      
# Tip Works!
""" Bill=(input("How was the Service?"))
if Bill == ('Bad'):
    print ("0% tip")
elif Bill == ("Okay"):
    print ("15% tip")
elif Bill == ("Good"):
    print == ("20% tip")
elif Bill == ("Great"):
    print ("25% tip")
 """
""" 
#Factoring works!
Accept=int(input("Put a Number"))
for i in range(1,Accept+1):
    if Accept%i == 0:
        print (i)
 """
""" #GCF works!
a=int(input("First Number:")) 
b=int(input("Second Number:"))


while b != 0:
    a,b=b, a%b

print(a) """



