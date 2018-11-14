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
studentName=[]#Array to hold names
studentAge=[]#Array to hold ages
studentHouse=[]#array to hold houses
studentReaction=[]#Array to hold reaction times
saturnTotal = 0
marsTotal = 0
averageReactionSaturn = 0
averageReactionMars = 0
saturnCount = 0
marsCount = 0
running = True # controls the dynamic loop for individual searches
dataTotal = 0
dataCount = 0
dataAverage = 0
slowestReaction = 1000000 # large number to ensure reaction time is always less
slowestStudent = ""
agesAvailable = [] #Temporary array to inform ages in dataset after invalid entry

#Assume a sample of 3 students for testing purposes, to be updated to 30
#as an appropriate sample size.
for i in range(3):
    name = str(input("\nPlease input the name of the student"))
    studentName.append(name)
    while True:
        try:
            age= int(input("\nPlease enter the age of the student"))
            if age >=12 and age <=16:
                studentAge.append(age)
                break
            else:
                print("\nThe age is invalid, please input the age again")

        except ValueError:
            print("Totally inacceptable input, Try again")
    while True:
        try:
            house = str(input("\nPlease enter the house of the student"))
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
            reaction = int(input("\nPlease enter the reaction time of the student"))
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

#TASK 3 – Output statistics based on user input 
#Extend your program to prompt users to input a 
#specific age and school house. Using only records 
#that match the criteria input, the program should 
#identify, calculate and output: • The average 
#reaction time • The slowest reaction time The 
#output should include a suitable message for 
#each of the reaction times identified.

while running:
    dataRequired = str(input("\nDo you want to run another specific data Search (y/n)"))
    if dataRequired == "n":
        running = False
    else:
        while True:
            try:
                houseRequired = str(input("\nWhich house do you want for calculations?"))
                if houseRequired in studentHouse:
                    break
                else:
                    print("\nThat house is not in the dataset")
            except ValueError:
                print("That is not a valid input")

        while True:
            try:
                ageRequired=int(input("\nWhat age do you want to calculate?"))
                if ageRequired in studentAge:       
                    for i in range(len(studentHouse)):
                        if studentHouse[i] == houseRequired and studentAge[i]== ageRequired:
                            dataTotal = dataTotal + studentReaction[i]
                            dataCount = dataCount + 1
                            if studentReaction[i]< slowestReaction:
                                slowestReaction = studentReaction[i]
                                slowestStudent = studentName[i]
                    break
                else:
                    print("That age is not in the dataset")
            except ValueError:
                print("That is not a valid input")
        
        if dataCount>0:
            dataAverage = dataTotal/dataCount
            print("\nThe average reaction time for ",houseRequired, ageRequired, " year olds is ", dataAverage )
            print("\nThe slowest reaction time for ",houseRequired, ageRequired, " year olds is ", slowestReaction, " being ",slowestStudent)
        else:
            print("\nThere are no combinations of that age and house!")
            for y in range(len(studentHouse)):
                if studentHouse[y] == houseRequired:
                    agesAvailable.append(studentAge[y])
            print("Ages available in ", houseRequired," are ", agesAvailable)

        dataCount = 0
        dataTotal = 0
        slowestReaction = 1000000
        agesAvailable = []
print("\nThank you for using Mr W's reaction Time app ")
