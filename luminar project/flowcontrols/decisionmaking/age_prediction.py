birth_year=int(input("enter your birth year"))
birth_month=int(input("enter your birth month"))
birth_date=int(input("enter your birth date"))
current_year=int(input("enter current year"))
current_month=int(input("enter current month"))
current_date=int(input("enter current date"))
age_year=abs(current_year-birth_year)
age_month=abs(current_month-birth_month)
age_days=abs(current_date-birth_date)
print("you are",age_year,"years",age_month,"months",age_days,"days old")