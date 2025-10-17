''' A student got marks in three subjects: math=78, science=83, english=85. find the total marks and average marks using division '''


# Marks obtained in three subjects
maths = 78
science = 85
english = 69

# Calculate total marks
total_marks = maths + science + english

# Calculate average marks using division
average_marks = total_marks / 3

# Display the results
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

print(round(average_marks, 2))  # Rounding to 2 decimal places


# Boys hostel per room price is 54000 Rs.
room_price = 54000
total_boys = 3

# Calculate individual share using division
individual_share = room_price / total_boys  # Using division operator to get a float result 
print("Each boy's share:", individual_share)


# You and 3 fiends go to pizza shop. one pizza cost 850 PKR. calculate total bill if each friend buys one pizza.
# Divide the bill equally among all friends.
# use modules % to check if the bill can be divided equally (no remainder) 
pizza_price = 850
total_friends = 3
# Calculate total bill
total_bill = pizza_price / total_friends 
print("Total bill:", total_bill)
print(round(total_bill, 2))  # Rounding to 2 decimal places
print ("Remainder:", total_bill % total_friends)
print(round(total_bill % total_friends, 2))  # Rounding to 2 decimal places


''' A student enters their ID while logging in. The system stores the correct ID as 12345.

correct_id = 12345
entered_id = 54321
Task: use the != operator to check if the entered ID is wrong, without using if-else statement. output: login:True

'''
correct_id = 12345
entered_id = 54321
login = (entered_id != correct_id)
print("Login:", login)  # Output: Login: True if the ID is wrong, False if correct
