
name=input("ENTER NAME:")
fname=input("ENTER FILE NAME:")
fh=open(fname)
details=[]
sts=[]
status=[]
for line in fh:
    if name in line:
        line=line.split(",")
        here=line[3].strip()
        status.append(here)
        date=line[2]
        stat=line[3]
        details.append(date)
        sts.append(stat)
summary=dict()
for x in status:
    summary[x]=summary.get(x,0)+1
print(summary)

#to calculate attendance percentage
total_days=[]
for k,v in summary.items():
    total_days.append(v)
    y=sum(total_days)
present_count=summary.get("Present",0)
percentage=(present_count/y)*100
print(percentage)


#to display other details
print("for other details choose option1")
option=input("option1 or end-")
if option=="option1":
        reg_no=line[0]
        print("REGISTRATION NUMBER IS-",reg_no)
        print("DETAILED SUMMARY IS AS FOLLOWS:")
        print(details)
        print(sts)

else:
    print("COMPLETED")
    
print("THANKYOU")
            


    

    

