years = input("Type the number of years you want to spend at Hermitage museum:")
exhibits_year = 60/5*8*365
exhibits_day = 60/5*8
exhibits_minute = 60/5
result1 = int(years)*exhibits_year
print("In",years,"years you can see",int(result1),"exhibits")

exhibits = input("Type the number of exhibits you want to see (less than 2800000):")
resulty = (int(exhibits)/exhibits_year)
resultd = (int(exhibits)-(int(resulty)*exhibits_year))/exhibits_day
resultm = ((int(exhibits)-(int(resulty)*exhibits_year))-(int(resultd)*exhibits_day))/exhibits_minute
print("It will take you",int(resulty),"years",int(resultd),"days",int(resultm),"minutes to see",int(exhibits),"exhibits at Hermitage museum")



