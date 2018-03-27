def leap_year(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leap_year(1999))
print(leap_year(2000))
print(leap_year(2001))
print(leap_year(2004))
print(leap_year(2100))
