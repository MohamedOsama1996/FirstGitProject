import csv


name1=""
email1=""
mobile1=""
university1=""
major1=""
mydec={
    "name":[],
    "email":[],
    "mobile":[],
    "university":[],
    "major":[]
}
Name =[]
Email =[]
Mobile=[]
University=[]
Major=[]
while 1:
    name1=input( "please enter your name ")
    if(name1=="STOP"):
        break
    mydec['name'].append(name1)
    email1= input("please enter your email ")
    mydec['email'].append(email1)
    mobile1 = input("please enter your mobile ")
    mydec['mobile'].append(mobile1)
    university1= input("please enter your university ")
    mydec['university'].append(university1)
    major1=input("what is your major ")
    mydec['major'].append(major1)

Name = mydec['name']
Email =mydec['email']
Mobile = mydec['mobile']
University=mydec['university']
Major = mydec['major']

with open('dict.csv', 'w') as csvfile:
    i=0
    fieldnames =['name','email','mobile','university','major']
    writer= csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    while i<len(Name):
     writer.writerow({'name':Name[i],'email':Email[i],'mobile':Mobile[i],'university':University[i],'major':Major[i]})
     i=i+1






