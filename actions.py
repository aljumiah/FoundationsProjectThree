# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Aljumiah"
my_age = 26
my_bio = "Developer"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal.\n--------------------------" % my_name)
    options()

def options():
    # your code goes here!
    
    print("Would you like to:\n1) Create a new club.\nor:\n2) Brwse and join clubs.\nor:\n3) View existing clubs.\nor:\n4) Display members of a club.\nor:\n-1) Close application.")
    while True:
        choose_option = input()
        if choose_option == "1":
            create_club()
        elif choose_option == "2":
            view_clubs()
            join_clubs()
        elif choose_option == "3":
            view_clubs()
        elif choose_option == "4":
            view_club_members()
        elif choose_option == "-1":
            quit()
        else:
            options("Invalid input try agin: ")

def create_club():
    # your code goes here!
    pick_name = input("pick name for you club: ")
    pick_discription = input("What is your club about: ")  
    club = Club(pick_name,pick_discription)
    club.recruit_member(myself)
    club.assign_president(myself)
    clubs.append(club) 
    print("Enter the number of the people you would like to recuit to yout new club (-1 to stop):\n----------------------------------------")
    print("---------------------------------------")   
    for index, person in enumerate(population):
        print("[%s] %s" %(index+1,person.name))
          
    
    while  True:
        member_name = input()
        if member_name == "-1":
            break
        elif int(member_name) >= 1 and int(member_name) <= len(population):
            club.recruit_member(population[int(member_name)-1])
            print("Member addedd")
        else: 
            print("invalid input")

    print("here is your club: %s\n disciption: %s\n" %(club.name,club.description))
    club.print_member_list()   
    options()

def view_clubs():
    # your code goes here!
    for Theculbs in clubs:
        print("Name:%s \nDiscription: %s \n Member: %s" %(Theculbs.name,Theculbs.description,len(Theculbs.members)))
          
def view_club_members():
    # your code goes here!
    flag = False
    view_clubs()
    club_name = input("Enter the name of the club whose members you would like to see: ")
    for clubName in clubs:
        if clubName.name.lower() == club_name.lower():
            clubName.print_member_list()
            flag =True
    if flag == False:
        print("Club name does't exist")
        view_club_members()
    options()


def join_clubs():
     # your code goes here!
    flag = False
    view_clubs()
    club_name = input("Enter the name of the club yout would like to join: ")
    for clubName in clubs:
        if clubName.name.lower() == club_name.lower():
            clubName.recruit_member(myself)
            flag =True
    if flag == False:
        print("Club name does't exist")
        join_clubs()
    options()
def application():
    introduction()
    # your code goes here!

