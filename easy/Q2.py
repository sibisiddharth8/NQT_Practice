start_of_month_day = input()
no_of_days = int(input())

no_of_sundays = 0 

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

i=days.index(start_of_month_day)+1

while (no_of_days !=0):
    if (days[i]=="sun"):
        no_of_sundays+=1
        i=0
    else:
        i+=1    
    no_of_days-=1    
print(no_of_sundays)
