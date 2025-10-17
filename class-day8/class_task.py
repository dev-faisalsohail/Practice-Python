# Take the original message: " H!e@l#l$o% t^h&e*re, W(o)r_l+d! 123 "

original_msg = " H!e@l#l$o% t^h&e*re, W(o)r_l+d! 123 " #rmsg

new_msg = original_msg.strip() # msg

str1=new_msg[0:11:2]
str2=new_msg[11:19:2]
str4=new_msg[21:-3:2]
str3=new_msg[18:21:2]
str5=new_msg[-3:]

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

fmsg1= str1+str2+str3+str4+str5
fmsg=fmsg1.lower()
print(fmsg1)
print(fmsg)

# python Replace spaces with underscores
rmsg = fmsg.replace(' ', '_')

Capitalize the first letter of the sentence
cap = fmsg.capitalize()

Remove the last 4 characters from the string
sentence = cap[0:-4]

Reverse the modified sentence
rev = sentence[::-1]