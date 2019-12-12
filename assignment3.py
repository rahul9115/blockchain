import copy
person=[]
def add_list(name,age,hobbies):
    person_data={
            'name':name,
            'age':age,
            'hobbies':hobbies
    } 
    person.append(person_data)
while True:
    print("Enter 1 for entering person details and diplaying person list")
    print("Enter 2 looking at for list of names")
    print("enter 3 to check whether age is greater than 20")
    print("Enter 4 copying list")
    print("Enter 5 for unpacking")
    print("Enter 6 to quit")
    value=input("enter the value")
    print(value)
    if value=='1':
        name=input("enter the name of the person: ")
        age=int(input("enter the age of the person: "))
        hobbies=[]
        while True:
            hobby=input("Enter your hobbies: ")
            hobbies.append(hobby)
            while True:
                value1=input("Do you have more hobbies [y/n]: ")
                if value1=='n' or value1=='y':
                    break
                else:
                    print("please enter valid input")
                    continue
            if value1=='y':
                continue
            else:
                break 
        add_list(name=name,age=age,hobbies=hobbies)
        print(person)
        while True:
            value1=input("Do you want to continue [y/n]: ")
            if value1=='n' or value1=='y':
                break
            else:
                print("please enter valid input")
                continue
        if value1=='y':
            continue
        else:
            break    
    if value=='2':
        names=[[block.get(i) for i in block if i=='name']for block in person]
        print(names)
        while True:
            value1=input("Do you want to continue [y/n]: ")
            if value1=='n' or value1=='y':
                break
            else:
                print("please enter valid input")
                continue
        if value1=='y':
            continue
        else:
            break 
    if value=='3':
        age_names=[]
        age_names=[[block.get(i) for i in block if block.get('age')<20 and i=='name']for block in person]
        print("this people are below 20",age_names)
        while True:
            value1=input("Do you want to continue [y/n]: ")
            if value1=='n' or value1=='y':
                break
            else:
                print("please enter valid input")
                continue
        if value1=='y':
            continue
        else:
            break 

    if value=='4':
        person1=copy.deepcopy(person)
        person1[0]['name']='aparna'
        print(person1)
        print(person)
        while True:
            value1=input("Do you want to continue [y/n]: ")
            if value1=='n' or value1=='y':
                break
            else:
                print("please enter valid input")
                continue
        if value1=='y':
            continue
        else:
            break 
    if value=='5':
        if len(person)==2:
            a,b=person
            print(a," ",b)
            while True:
                value1=input("Do you want to continue [y/n]: ")
                if value1=='n' or value1=='y':
                    break
                else:
                    print("please enter valid input")
                    continue
        if value1=='y':
            continue
        else:
            break 
    if value=='6':
        break
    else:
        print("Enter the valid input")
        continue        







        