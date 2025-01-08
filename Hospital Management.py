
#PYTHON PROGRAM
##### Defining the required Functions #####

def create_database():
    m="Create database Hospital"
    cursor.execute(m)
    mycon.commit()  
#creating_tables:
def create_patientb():
    m="""create table Patients1(Patient_ID int(10),Patient_Name varchar(30),
    M_or_F varchar(1),Patient_s_Height int(10),
    patient_weight_in_Kgs int(10),Blood_group varchar(10),
    Father_s_name varchar(30),Age int(3))"""
    cursor.execute(m)
    mycon.commit()
def create_patienta():
    m="""create table Patients2(Patient_ID int(10),Address varchar(250),city varchar(30),
    state varchar(30),Phone_number int(20),Email varchar(30),Doctor_s_Name varchar(30),
    Disease_Name varchar(30),Medicine varchar(30),Bill int,Payment_method varchar(30),
    Date_created varchar(30))"""
    cursor.execute(m)
    mycon.commit()
def create_doc():
    n="""create table Doc_s_(Doctors_ID int(5),Doctors_Name varchar(30),M_or_F varchar(10),
    Age int(3),Qualification varchar(100),Specialised_field varchar(30))"""
    cursor.execute(n)
    mycon.commit()

#To enter values into respective tables
def before_visit():
    a=input("Enter Patient_ID:")
    b=input("Enter patients name:")
    c=input("Enter Male Or Female(M/F):")
    d=input("Enter Patinet's Height:")
    e=input("Enter Patinet's Weight(In Kgs):")
    f=input("Enter Patient's Blood Group:")
    g=input("Enter Fathers Name:")
    h=input("Enter Patient's Age':")
    m="""Insert into patients1(Patient_ID,Patient_Name,
    M_or_F,Patient_s_Height,patient_weight_in_Kgs,Blood_group,Father_s_name,Age)
    values({},'{}','{}',{},{},'{}','{}',{})""".format(a,b,c,d,e,f,g,h)
    cursor.execute(m)    
    mycon.commit()
    
def after_visit():
    k=input("Enter Patient_ID:")
    a=input("Enter Address:")
    b=input("Enter City:")
    c=input("Enter State:")
    d=input("Enter Phone number:")
    e=input("Enter E-Mail:")
    f=input("Enter Doctor's Name:")
    g=input("Enter Disease Name:")
    h=input("Enter Prescribed Medicine:")
    i=input("Enter Bill Amount: Rs.")
    j=input("Enter Payment Method(Cash/Cheque/Card):")
    now=datetime.now()
    formatted_date=now.strftime('%y-%m-%d %H:%M:%S')
    m="""Insert into patients2(Patient_ID,Address,city,state,Phone_number,Email,
    Doctor_s_Name,Disease_Name,Medicine,Bill,Payment_method,Date_created)
    values({},'{}','{}','{}',{},'{}','{}','{}','{}',{},'{}','{}')""".format(k,a,b,c,d,e,f,g,h,i,j,formatted_date)
    cursor.execute(m)
    mycon.commit()
    
def docs():
    a=int(input("Enter Doctor_ID :"))
    b=input("Enter Doctors Name:")
    c=input("Male Or Female(M/F):")
    d=int(input("Enter Doctor's Age:"))
    e=input("Education Qualification:")
    f=input("Enter his spcialised field of Treatment:")
    m="""Insert into Doc_s_(Doctors_ID,Doctors_Name,M_or_F,Age,Qualification,Specialised_field)
    values({},'{}','{}',{},'{}','{}')""".format(a,b,c,d,e,f)
    cursor.execute(m)
    mycon.commit()    

#To fetch all values
def all_():
    m="""select * from patients1 JOIN patients2 USING (Patient_ID) """
    cursor.execute(m)
    data=cursor.fetchall()
    for i in data:
        print(i)
    
def viewd():
    m="select * from Doc_s_"
    cursor.execute(m)
    data=cursor.fetchall()
    for i in data:
        print(i)
        
def id_():
    m="select patient_id from patients1"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)
    
def name():
    m="select Patient_Name from patients1"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)
    
def Age():
    m="select Age from patients1"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)
        
def gen():
    m="select M_or_F from patients1"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)
        
def BG():
    m="select Blood_group from patients1"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)

def disease():
    m="select Disease_Name from patients2"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)

def city():
    m="select city from patients2"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)
    
def date():
    m="select Date_created from patients2"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i)
    
def pay():
    m="select Payment_method from patients2"  
    cursor.execute(m)
    dat=cursor.fetchall()
    for i in dat:
        print(i) 
        
#__main__
import time
from datetime import datetime
import matplotlib.pyplot as plt
plt.axis("equal")
import mysql.connector as sqltor
mycon=sqltor.connect(user='user',host='localhost',password='4321')
if mycon.is_connected()==False:
    print("Error connecting to Mysql....!!")
else:
    print("Successfully connected to database...")
cursor=mycon.cursor()
print('\n'*2)
print("###################################################################")
print("#    *                                                            #")
print("#  *****  Welcome to Hospital Management System                   #")
print("#    *                                                            #")
print("###################################################################")
print('\n'*2)
while True:
    print("1.Create Database")
    time.sleep(.3)
    print("2.Create Tables")
    time.sleep(.3)
    print("3.Enter patient detail")
    time.sleep(.3)
    print("4.Enter Doctors detail")
    time.sleep(.3)
    print("5.View")
    time.sleep(.3)
    print("6.Modify")
    time.sleep(.3)
    print("7.Analytics")
    time.sleep(.3)
    print("8.Exit")
    time.sleep(.3)
    ch=int(input("Enter your Choice:"))
    if ch==1:
        print()
        create_database()
        print("Successfully created database....")
        print('\n'*2)
        continue
    mycon=sqltor.connect(user='user',host='localhost',password='4321',database='Hospital')
    if mycon.is_connected==False:
        print("Error connecting to database..!!")
    cursor=mycon.cursor()
    if ch==2:
        create_patientb()
        create_patienta()
        create_doc()
        time.sleep(.3)
        print ("."),
        time.sleep(.3)
        print ("."),
        time.sleep(.3)
        print ("."),
        time.sleep(.3)
        print ("."),
        time.sleep(.3)
        print (".")
        print("Successfully created 3 tables......")
        print('\n'*2) 
    if ch==3:            
        while True:
            print("***A.Before Doc\'s visit.....***")
            time.sleep(3)
            print("***B.After Doc\'s visit.....***")
            time.sleep(3)
            print("***C.Exit.....***")
            time.sleep(3)
            ch=input("Enter your choice(A/B):")
            if ch=="A":
                before_visit()
                print()
            elif ch=="B":
                after_visit()
                print()
            elif ch=="C":
                break
            else:
                time.sleep(2)
                print("!!!!")
                print("Your choice is invalid")
                break
    elif ch==4:
        print("Enter doctors details *****ONLY FOR AUTHORISED PERSONS...*****")
        password=input("Enter your password:")
        if password=="4321":
            docs()
            print()
        else:
            print("WRONG Password!!!!!")
            print("Please try again or Later!")
    elif ch==5:
        print("To view doctors detail choose ***ADMIN*** mode")
        print("To view patient detail choose ***USER*** mode")
        print("1.Admin Mode   *****ONLY FOR AUTHORISED PERSONS...*****")
        print("2.User mode")
        mode=int(input("Enter your choice:"))
        if mode==1:
            password=input("Enter your password:")
            if password=="4321":
                viewd()
                print()   
            else:
                print("WRONG Password!!!!!")
                print("Please try again or Later!")
            
        elif mode==2:
            while True:
                print("VIEW BY:")
                print("1. Patient_ID")            
                print("2. Patient_Name")
                print("3. Age")
                print("4. Gender")        
                print("5. Patient Blood_Group")            
                print("6. Patients_Disease")            
                print("7. City.")
                print("8. Date")
                print("9. Pay_Method")
                print("10. view all patient details...")
                print("11.Exit")
                ch=int(input("Enter your choice:"))
                if ch==1:
                    id_()
                    c=input("Do you want to view particular ID PATIENT_details(Y/N)?")
                    if c=='Y':
                        ID=int(input("Enter Patient_ID:"))
                        m="""select * from Patients1 NATURAL JOIN patients2 where Patient_ID='{}'""".format(ID) 
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                    
                elif ch==2:
                    name()
                    a=input("Do you want to view particular NAMED PATIENT_details(Y/N)?")
                    if a=='Y':
                        name=input("Enter Patient_Name:")
                        m="""select * from Patients1 NATURAL JOIN patients2 where Patient_Name='{}' """.format(name) 
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                elif ch==3:
                    Age()
                    a=input("Do you want to view particular Aged PATIENT_details(Y/N)?")
                    if a=='Y':
                        age=input("Enter the required Age:")
                        m="""select * from Patients1 where Age='{}' """.format(age) 
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                elif ch==4:
                    gen()
                    print()                
                    a=input("Do you want to know NO. of Male or Female...(Y/N)?")
                    if a=='Y':
                        m="""select M_or_F from Patients1 where M_or_F='M'""" 
                        cursor.execute(m)
                        dat1=cursor.fetchall()
                        l1=len(dat1)
                        n="""select M_or_F from Patients1 where M_or_F='F'""" 
                        cursor.execute(n)
                        dat2=cursor.fetchall()
                        l2=len(dat2)
                        print("The Numbers of Males who visited the hospital is",l1)
                        print("The Numbers of Females who visited the hospital is",l2)
                        print()
                    
                elif ch==5:
                    BG()
                    print()
                    a=input("Do you want to view particular Blood_grouped PATIENT_details(Y/N)?")
                    if a=='Y':
                        BG=input("Enter Blood_group:")
                        m="""select * from Patients1 NATURAL JOIN patients2 where Blood_group='{}'""".format(BG) 
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                
                elif ch==6:
                    disease()
                    a=input("Do you want to view particularly Disease affected PATIENT_details(Y/N)?")
                    if a=='Y':
                        D=input("Enter Name of Disease:")
                        m="""select * from Patients1 NATURAL JOIN patients2 where Disease_Name='{}'""".format(D) 
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                    
                elif ch==7:
                    city()
                    a=input("Do you want to view particular city PATIENT_details(Y/N)?")
                    if a=='Y':
                        city=input("Enter City:")
                        m="""select * from Patients1 NATURAL JOIN patients2 where city='{}'""".format(city) 
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                elif ch==8:
                    date()
                    a=input("Do you want to view particular Date and PATIENT_details(Y/N)?")
                    if a=='Y':
                        date=eval(input("Enter the Date&Time from above:"))
                        m="""select * from Patients1 NATURAL JOIN patients2 where Date_created='{}' """.format(date) 
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                elif ch==9:
                    pay()
                    a=input("Do you want to view particular method of payment used(Y/N)?")
                    if a=='Y':
                        m="""select  Distinct(Payment_method) from patients2"""
                        cursor.execute(m)
                        dat=cursor.fetchall()
                        for i in dat:
                            print(i)
                        print()
                elif ch==10:
                    all_()
                elif ch==11:
                    break
                else:
                    print("Your choice is INVALID!!!")
    elif ch==6:
        print("Enter doctors details *****ONLY FOR AUTHORISED PERSONS...*****")
        password=input("Enter your password:")
        if password=="4321":
            print("\n")
            print("=====================================================")
            print("|Choose the table you want to edit Patient details  |")
            print("|1.Patients                                         |")
            print("|2.Docs                                             |")
            print("=====================================================")
            print("\n")
            ch=int(input("Enter your choice: "))
            if ch==1:
                id=input("Enter Patient_ID:")
                while True:
                    print("\n")                
                    print("=======================================")
                    print("|Choose the coloumn to edit           |")
                    print("|1.Name                               |")
                    print("|2.Height                             |")
                    print("|3.Weight                             |")
                    print("|4.Address                            |")
                    print("|5.City                               |")
                    print("|6.Phone Number                       |")
                    print("|7.Email-Id                           |")
                    print("|8.Exit                               |")
                    print("=======================================")
                    print("\n")
                    choice=int(input("Enter your choice: "))
                    if choice==1:
                        n=input("Enter the Final name:")
                        m="""update patients1 set Patient_Name='{}' where Patient_ID={}""".format(n,id)
                        cursor.execute(m)
                        mycon.commit()
                    elif choice==2:
                        n=input("Enter the Final Height:")
                        m="""update patients1 set Patient_s_Height='{}' where Patient_ID={}""".format(n,id)
                        cursor.execute(m)
                        mycon.commit()
                    elif choice==3:
                        n=input("Enter the Final Weight:")
                        m="""update patients1 set patient_weight_in_Kgs='{}' where Patient_ID={}""".format(n,id)
                        cursor.execute(m)
                        mycon.commit()
                    elif choice==4:
                        n=input("Enter the Final Address:")
                        m="""update patients2 set Address='{}' where Patient_ID={}""".format(n,id)
                        cursor.execute(m)
                        mycon.commit()
                    elif choice==5:
                        n=input("Enter the Final City:")
                        m="""update patients2 set city='{}' where Patient_ID={}""".format(n,id)
                        cursor.execute(m)
                        mycon.commit()
                    elif choice==6:
                        n=input("Enter the Final Phone_Number:")
                        m="""update patients2 set Phone_number='{}' where Patient_ID={}""".format(n,id)
                        cursor.execute(m)
                        mycon.commit()
                    elif choice==7:
                        n=input("Enter the Final E-mail:")
                        m="""update patients2 set Email='{}' where Patient_ID={}""".format(n,id)
                        cursor.execute(m)
                        mycon.commit()
                    elif choice==8:
                        break
                    else:
                        print("Your Choice is Invalid!!")
            elif ch==2:
                id=input("Enter Doctor_ID:")
                while True:
                    print("\n")                
                    print(" ======================================= ")
                    print("|Choose the coloumn to edit             |")
                    print("|1.Name                                 |")
                    print("|2.Update Qualification                 |")
                    print("|(INclude all degrees while updating...)|")
                    print("|3.Exit                                 |")
                    print(" ======================================= ")
                    print("\n")
                    choice=int(input("Enter your choice: "))
                    if choice==1:
                        n=input("Enter the Final name:")
                        m="""update Doc_s_set Doctors_Name='{}' where Doctors_ID ={}""".format(n,id)
                        cursor.execute(m)
                    elif choice==2:
                        n=input("Update your respective Qualification:")
                        m="""update Doc_s_set Qualification='{}' where Doctors_ID ={}""".format(n,id)
                        cursor.execute(m)
            elif ch==3:
                break
                print()
    elif ch==7:
        while True:
            print("1.Disease Analysis...")
            print("2.Age-wise ...")
            print("3.Exit")
            op=int(input("Enter your choice:"))
            if op==1:
                m="""select Disease_Name from patients2"""
                cursor.execute(m)
                data=cursor.fetchall()
                lst=[]
                lst1=[]
                for i in data:
                    lst+=i
                for j in lst:
                    a=lst.count(j)
                    lst1.append(a)
                plt.bar(lst,lst1,width=[0.35],color=['cyan','red','black','green'])
                plt.ylabel("No. of people")
                plt.xlabel("Disease affected")
                plt.show()
                print()
            elif op==2:
                m="""select Age from patients1"""
                cursor.execute(m)
                data=cursor.fetchall()
                lst=[]
                lst1=[]
                for i in data:
                    lst+=i
                    lst.sort()
                for j in lst:
                    a=lst.count(j)
                    lst1.append(a)
                plt.bar(lst,lst1,width=[0.35],color=['cyan','red','black','green'])
                plt.ylabel("No. of people")
                plt.xlabel("Age Group")
                plt.show()
                print()
            elif op==3:
                break
            else:
                print("Invalid Choice...")
                break
            
    elif ch==8:
        print("***************************************")
        print("*_______________EXIT__________________*")
        print("***************************************")
        break
    else:
        print("Invalid Choice...")
    input("Press ENTER to Continue")
    print()
    
mycon.commit()
mycon.close()
                
                
                
            
                
                
       
   
    
        


    
