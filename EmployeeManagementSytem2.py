#declaring variables
eMS=[]
response=True           

# Checking the list for same ID
def checkForSameEmployee(id):
    for e in eMS:
        #if same ID is present loop until new ID generated
        if id==e["ID"]:
            return False            
    return True
    
# Sorting using bubble sort in ascending order
def sortEmployee(eMS):
    for e in range(len(eMS)):
        for f in range(e+1,len(eMS)):     
            if eMS[e]["ID"]>eMS[f]["ID"]: 
                temp1=eMS[e]
                eMS[e]=eMS[f]
                eMS[f]=temp1 
                

# Taking Employee Details
def takeDetail():
    resspone=True
    
    #loop untill  unique ID is generated
    while True:
        id=int(input("Enter Enter Employee ID: "))
        # When unique ID is generated break from the loop
        if checkForSameEmployee(id):                
            break
        else:
            print(f"ERROR: Employee {id} already exists. Please enter a different ID: \n")
            
    name=input("Enter Employee name: ")
    age=int(input("Enter employee age: "))
    weight=float(input("Enter employee weight: "))
    salary=int(input("Enter Employee salary: "))
    print("\n")
    details={"ID":id,"Name":name,"Age":age,"Weight":weight,"Salary":salary}
    
    #ADD    the dictionary to the List
    eMS.append(details)        
        
#delete the Employee whos ID is provided
def deleteEmployee(delete):
    
    isFound=True
    #Delete the Employee if ID found
    for i in range(len(eMS)):
        if eMS[i]["ID"] == delete:
            del eMS[i]
            print("Employee Successfully deleted")
            isFound=False
            break
     
    # if not found ask for command
    if isFound:

        
        #check for command and act accordingly
        while True:
            print("Employee not found\n")
            choice=input(("Do you want to delete employee? Enter y for YES, n for NO: "))
            if choice.lower()=="y":
                delete=int(input("Enter Employeeb ID who is to be deleted: "))
                print("\n")
                deleteEmployee(delete)
                break
            elif choice.lower()=="n":
                return
            else:
                print("Invalid choice")
                
                
#User menu of actions    
def choicesOfOperation():
           
    while True:
        print("----------------------------")
        print("What do you want to do now? \nEnter 1 to insert new employee\nEnter 2 to delete an employee\nEnter 3 to print all employee details\nEnter 4 to exit the system")
        response=int(input("Enter yout choice: "))
        print("--------------------\n")
        if response==1:
            takeDetail()
        elif response==2:
            delete=int(input("Enter the Employee ID you want to delete: "))
            deleteEmployee(delete)
        elif response==3:
            sortEmployee(eMS)
            print(f"ID\tNAME\tAGE\tWEIGHT\tSALARY")
            for e in range(len(eMS)):
                print(f"{eMS[e]['ID']}\t{eMS[e]['Name']}\t{eMS[e]['Age']}\t{eMS[e]['Weight']}\t{eMS[e]['Salary']}")
            print("*****************************")
        #End of program if response==4
        elif response==4:
            break
        else:
            print("Invalid Input\n")    

   
print("********Welcome to Employee Management System********\n")       
# Enter into the program
choicesOfOperation()

print("THANK YOU FOR USING OUR SERVICE")
