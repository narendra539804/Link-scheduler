import webbrowser
import time 
# Taking website to be opened as input
#link = input("Enter the link to website you want to open ->")
# Taking alarm time from the user
#alarm = input("Set the website alarm time as (Format:- HH:MM:SS)(24 hour format) ->")
# This is the actual time that we will use to print. *
my_file = open("form-save.txt", "r")
content = my_file.read()
links = content.split(",")
my_file.close()
#print(links)
#links=['https://meet.google.com/yxf-tdyg-aoq?authuser=0'
#,'https://meet.google.com/hkw-yxvw-vjg?authuser=0','https://meet.google.com/lookup/cp6zphddbe','https://meet.google.com/lookup/acnd6odh67']
alarms=['23:37:50', '10:50:00', '01:20:00', '02:10:00']
i=0
while i<len(links):
    link=links[i]
    alarm=alarms[i]
    Current_time = time.strftime("%H:%M:%S") 
    print("The Given Link should be Open at ",alarm)
    # Printing current time untill alarm time
    while (Current_time != alarm): 
       print ("Waiting, the current time is " + Current_time +" :-( " )
       Current_time = time.strftime("%H:%M:%S") 
       time.sleep(1) 

    # Opening the webpage at alarm time
    if (Current_time == alarm): 
       print ("WEBSITE IS OPENING :D") 
       webbrowser.open(link)
    i=i+1
