# Home Task Fantasy character Profile

# Sample Variables

real_name = 'Faisal Sohail'
home_region = 'theRoyalKindom'
special_phase = 'speak friend and enter'

# create a fantacy name

first_name = real_name[0:4]
print(first_name)
capt = first_name.capitalize()
print(capt)

last_name = real_name[-3:]
print(last_name)
title_case = last_name.title()
print(title_case)

str1 = 'Fais '
str2 = 'Ail'
str3 = str1 + str2
print(str3)

fanstasy_name = ['Fais', 'Ail']

join_name = "".join(fanstasy_name)
print(join_name)

# Generate a Royal Title

ext_lastName= real_name[6:]
print(ext_lastName)

u_case = ext_lastName.upper()
print(u_case)

av = ' of Avalon'
r_title = u_case + av
print(r_title)

# Format the Kingdom Name


part1 = home_region[0:3]      
part2 = home_region[3:8]      
part3 = home_region[8:]      

# join with spaces
result = part1 + " " + part2 + " " + part3

# convert to title case
final_result = result.title()

print(final_result)

# Create a Magical Skill Phrase 
new_phase = special_phase.replace('friend', 'foe')
print(special_phase)
print(new_phase)
new_upper = new_phase.upper()
print(new_upper)

# Final Result after formatting

print("Name: {}\nTitle: {}\nKingdom: {}\nSkill Phase: {}\n" .format(join_name,r_title,final_result,new_upper))