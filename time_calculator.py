#FCC Project 2
""" #do three quotes in front of text for long comment commencement
Write a function named add_time that takes in two required parameters and one
optional parameter:
A start time in 12 hour clock format with AM/PM: HH:MM AM/PM
A duration time in H:MM format
Optional: Starting day of the week, case insensitive

Function should add duration of time to the start time/day and return the result.
If the result is in the next day, (next day) should be added to the end of the result.
If the result is more than one day later, it should show (x days later).
If optional argument day is given, result should also include day before x days later.

Examples:

add_time("3:00 PM", "3:10") returns 6:10 PM
add_time("11:43 PM", "24:20", "tueSday") returns 12:03 AM, Thursday (2 days later)
"""
def add_time(start,duration,day = False): # Max of 999 hours duration
    a = start
    b = duration
    c = day
    dayList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    hour = 0
    min = 0
    dhour = 0
    dmin = 0
    oday = ""
    odayInd = 0
    if a[1] == ":":
        hour = int(a[0])
        min = (int(a[2]) * 10) + int(a[3])
        if a[5] == "P":
            hour += 12  #converts to 24 hour time
    if a[2] == ":":
        hour = (int(a[0]) * 10) + int(a[1])
        min = (int(a[3]) * 10) + int(a[4])
        if a[6] == "P":
            hour += 12
    
    if b[1] == ":":
        dhour = int(b[0])
        dmin = (int(b[2]) * 10) + int(b[3])
    if b[2] == ":":
        dhour = (int(b[0]) * 10) + int(b[1])
        dmin = (int(b[3]) * 10) + int(b[4])
    if b[3] == ":":
        dhour = (int(b[0]) * 100) + (int(b[1]) * 10) + int(b[2])
        dmin = (int(b[4]) * 10) + int(b[5])

    if day != False:
        for d in dayList:
            if day.lower() == d.lower():
                oday = d # instead of daylist.indexOf(d), d is already daylist[d]
                odayInd = dayList.index(d)

    new_min = min + dmin
    totmin = 0
    remh = 0
    new_hour = hour + dhour
    tothour = 0
    remd = 0
    new_d = oday
    new_d_ind = odayInd
    dCount = 0

    if new_min>60:
        totmin = new_min
        new_min = totmin % 60
        remh = round((totmin - new_min) / 60) #round to full int
    if remh>0:
        new_hour += remh
    if new_hour>24:        
        tothour = new_hour
        new_hour = tothour % 24
        remd = round((tothour - new_hour) / 24) #round to full int

    if remd>0 and day!= False:
        new_d_ind = odayInd + remd
        dCount = remd
        if new_d_ind>6:
            new_d_ind = new_d_ind % 7
        new_d = dayList[new_d_ind]

    final_hour = ""
    final_min = ""
    dhalf = "" #AM/PM    
    dCountStr = ""

    if new_hour>12:
        final_hour = new_hour - 12
        final_hour = str(final_hour)
        dhalf = "PM"
    else:
        final_hour = str(new_hour)
        dhalf = "AM"
    
    final_min = str(new_min)
    if len(final_min)==1: #adds 0 in front of single digit minute
        final_min = "0" + final_min

    if new_hour == 0 or new_hour == 24: #changes 12 midnight to AM
        dhalf = "AM"
        final_hour = "12"
    if new_hour == 12: #changes 12 midday to PM
        dhalf = "PM"

    odayInd = str(odayInd)

    if dCount == 0:
        dCountStr = ""
    if dCount > 0:
        if dCount == 1:
            dCountStr = " (next day)"
        else:
            dCountStr = " (" + str(dCount) + " days later)"

    if b[1] != ":" and b[2] != ":" and b[3] != ":":
        print("error: too big duration")
    else:
        #print(hour,min,"Plus",dhour,dmin)
        #print("mins",new_min,totmin,remh)
        #print("hours",new_hour,tothour,remd)
        if day == False:
            print(final_hour + ":" + final_min + " " + dhalf + dCountStr)
        else:
            print(final_hour + ":" + final_min + " " + dhalf + ", " + new_d + dCountStr)

#add_time("3:00 PM","3:10")
add_time("11:43 PM", "24:20", "tueSday")