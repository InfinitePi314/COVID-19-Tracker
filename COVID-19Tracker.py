##########  COVID-19 Tracker  ##########
##########  Hack for Africa: A Microsoft Challenge  ##########

import pickle

class Patient:
    def __init__(self, name, age, gender, covidTestResult, otherIllness):
        self.name=name
        self.age=age
        self.gender=gender
        self.covidTestResult=covidTestResult
        self.otherIllness=otherIllness

    def info(self):
        return("Name: "+ str(self.name)+"\nAge: "+str(self.age)+"\nGender: "+str(self.gender)+"\nCOVID-19 Test Result: "+str(self.covidTestResult)+"\nOther Illnesses: "+str(self.otherIllness))

    def save(self):
        people.update({"self.name":Patient(self.name, self.covidTestResult, self.otherIllness)})

    def deletePatient(self):
        people.pop(self.name)

    def __str__(self):
        return("Name: "+ str(self.name)+"\nAge: "+str(self.age)+"\nGender: "+str(self.gender)+"\nCOVID-19 Test Result: "+str(self.covidTestResult)+"\nOther Illnesses: "+str(self.otherIllness))
'''     

people={}
pickle.dump( people, open( "save.p", "wb" ) )


'''
def begin():
        print("Welcome to the COVID-19 Tracker \n")
        people = pickle.load(open("save.p", "rb"))
        userChoice=input("Type 0 to leave \nType 1 to add a patient \nType 2 to view all patients \nType 3 to view a patient's details \nType 4 to remove a patient \n")
        if userChoice == "0":
                quit()
        elif userChoice == "1":
                addPatient()
        elif userChoice == "2":
                viewPatients()
        elif userChoice == "3":
                viewPatientDetails()
        elif userChoice == "4":
                deletePatientWI()

                

def addPatient():
        nameX=""
        covidresultX=""
        otherillnessX=""
        ageX=""
        genderX=""

        nameX=str(input("Type the patients name or exit to leave: "))
        print(" ")

        if nameX=="exit":
                begin()

        ageX=str(input("What was the patient's age?"))
        genderX=str(input("What was the patient's gender? "))

        covidresultX=str(input("What was the patient's COVID-19 test result? Type positive or negative: "))
        print(" ")
        otherillnessX=str(input("Enter any other illnesses the patient has, or type NULL: "))
        print(" ")
        people = pickle.load(open("save.p", "rb"))
        people[nameX]=Patient(nameX, ageX, genderX, covidresultX, otherillnessX)
        pickle.dump(people, open("save.p", "wb"))
        begin()

def viewPatients():
        people = pickle.load(open("save.p", "rb"))
        print(people.keys())
        print(" ")
        begin()


def viewPatientDetails():
        nameFD=str(input("Type the name of the patient or exit to leave: "))
        print(" ")
        people = pickle.load(open("save.p", "rb"))
        if nameFD=="exit":
                begin()
        elif nameFD not in people.keys():
                print("Invalid Name")
                viewPatientDetails()
        
        print(people[nameFD])
        begin()

def deletePatientWI():
        nameDelete=str(input("Type the name of the patient or exit to leave: "))
        people = pickle.load(open("save.p", "rb"))
        if nameDelete=="exit":
                begin()
        elif nameDelete not in people.keys():
                print("Invalid Name")
                deletePatientWI()
        
        people.pop(nameDelete)
        pickle.dump(people, open("save.p", "wb"))
        begin()

begin()
        




    


