# define a func to reverse a string

def reverse(s): 
  str = ""
  for i in s:
    str = i + str #print the following character first
  return str
  
s = str(input ("write an input :  ")) #input
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s)) #reversed string from return to function