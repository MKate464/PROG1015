def near100(num):
  if(num-100<=10 and num-100>-10):
   return "near"
  else:
    return "not near"

num=int(input("Enter a number(1:1000)"))
print("The number", num, "is", near100(num), "100")