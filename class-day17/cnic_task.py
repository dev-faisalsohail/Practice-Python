
age = float(input("Please enter your age:"))
if(age >= 18):
    rv = input("Do you have National ID card? Y/N:")
    if((rv == 'Y') or (rv == 'y')):
     print("WElcome,you can vote")
    else:
     print("Since you donot have CNIC, so you cannot vote")  
else:
  print("You are too young to vote")
  
  
cnic = input("Enter CNIC: ")

cnic = cnic.replace("#", "")
cnic = cnic.replace("@", "")
cnic = cnic.replace("&", "")

if cnic.isdigit() and len(cnic) == 13:
    clean_cnic = cnic[:5] + "-" + cnic[5:12] + "-" + cnic[12:]
    print("Valid CNIC:", clean_cnic)
else:
    print("Invalid CNIC")

