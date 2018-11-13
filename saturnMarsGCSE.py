#An Experiment has taken place which measures the reaction
#speeds of students. Each student is aged from 12 to 16
# and belongs to a school house (Saturn or Mars).
#A program is required to store the age, school house
#and reactrion time of each student in the school.
#There are 650 students in the school.
#The program should be able to output the reaction times
#of different student groups.

#Write and test a program for the school that.

#Task 1 - Set up arrays and store records
#Setup one dimensional arrays for the whole school to store the following data:
#The age of each student in whole years
#The school house of each student
#The reaction time of each student

#Input and store the records for an appropriate sample of
#students. Inputs must be validated on entry and any invalid inputs rejected.

#Set up the variables
studentName=[]
studentAge=[]
studentHouse=[]
studentReaction=[]
saturnTotal = 0
marsTotal = 0
averageReactionSaturn = 0
averageReactionMars = 0
saturnCount = 0
marsCount = 0


#Assume a sample of 3 students for testing purposes, to be updated to 30
#as an appropriate sample size.
for i in range(2):
    name = str(input("Please input the name of the student"))
    studentName.append(name)
    while True:
        try:
            age= int(input("Please enter the age of the student"))
            if age >=12 and age <=16:
                studentAge.append(age)
                break
            else:
                print("The age is invalid, please input the age again")

        except ValueError:
            print("Totally inacceptable input, Try again")
    while True:
        try:
            house = str(input("Please enter the house of the student"))
            house.lower()
            if house == "saturn" or house == "mars":
                studentHouse.append(house)
                break
            else:
                print("That is not a valid house, please re-enter your choice.")

        except ValueError:
            print("Totally inacceptable input")

    while True:
        try:
            reaction = int(input("Please enter the reaction time of the student"))
            studentReaction.append(reaction)
            break
            
        except ValueError:
            print("Totally inacceptable input")


#TASK 2 - Output School Based statistics
#Output the average reaction time for a house
for i in range(len(studentHouse)):
    if studentHouse[i] == "saturn":
        saturnTotal = saturnTotal + int(studentReaction[i])
        saturnCount += 1
    if studentHouse[i] == "mars":
        marsTotal = marsTotal + int(studentReaction[i])
        marsCount += 1


if saturnCount>0:
    averageReactionSaturn = saturnTotal/saturnCount
    print("\nThe average reaction of Saturn House is: " , averageReactionSaturn)
if marsCount>0:
    averageReactionMars = marsTotal/marsCount
    print("\nThe average reaction of Mars House is: ", averageReactionMars)

