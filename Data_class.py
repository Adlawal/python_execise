# Write a simple Python program that takes a persons name as input and greet them
# Write a simple Python program that takes a persons name and age as input. Then welcome the person and their age plus 20

#name= input("Enter your name:")
#print("how are you doing", name )
#Age= int(input("Enter your age:?"))
#Additional_age= Age + 20
#print(f"How are you doing {name}, you are {Additional_age}years old")



#Write a Python script that prompts for a students name and last exam grade. Add 50 to their score and divide their score by 4. Save the result. Then print their name and their result
#student_name= input("Enter your name:")
#Exam_grade= float(input("Enter your last exam grade:"))
#Add_grade= (Exam_grade + 50) / 4
#print(f"{student_name}, {Add_grade}")




#You are going to get input from a student. And then tell them their class of grade. Ensure that you are able to filter out wrong input
#3.5- 4.00 – First Class Honours
#3.0-3.49 – Second Class Honours (Upper Division)
#2.0-2.99 – Second Class Honours (Lower Division)
#1.0-1.99 – Third Class Honours


student_grade =float(input("Enter your grade:"))
print(student_grade)
if grade >=3.5:
  
  print ("first class honour")
elif grade>=3.0:
    print(" Second Class Honours Upper Division")
elif grade>=2.0:
  print("Second Class Honours (Lower Division)")
elif grade<=1.99:
  print ("Third Class Honours")
else:
  print ("incorrect grade")


