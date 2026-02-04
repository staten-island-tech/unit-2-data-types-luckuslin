def discount(child,resident,member):
  
 resident=input("Are you a citizen?")
 if resident== "Yes":
  print (True)
 else :
  print (False)
  
  member=input("Do you have an active Membership?")
  if member == "I have an Active Membership":
    print(True) 
  else : 
    print (False)

  child=input("How Old are You?")
  if child == range(1-12) or range (65-100):
    print(True)
  else :
    print (False)
    
    if resident and member and child == (True):
      print ("discount")
    else :
      print ("PAY UP")
      


discount