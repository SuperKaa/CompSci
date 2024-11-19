adultsbefore = 7.40
adultsafter = 8.90

childrenbefore = 5.40
childrenafter = 6.40

studentsbefore = 5.90
studentsafter = 6.90

seniorsbefore = 5.90
seniorsafter = 6.90

familybefore = 22.60
familyafter = 27.60

tuesdayprice = 5.40

def getnum(statement):
    while True:
        try:
            number = int(input(statement))
            break
                
        except ValueError:
            print("i asked for an integer!")

    return number

print("""+---------------+-------------+------------+
|   Category    | Before 5PM  | After 5PM  |
+---------------+-------------+------------+
| Adults        | 7.40        | 8.90       |
| Children      | 5.40        | 6.40       |
| Students      | 5.90        | 6.90       |
| Seniors       | 5.90        | 6.90       |
| Family        | 22.60       | 27.60      |
| Tuesday Price | 5.40        | 5.40       |
+---------------+-------------+------------+
""")

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

while True:
    day = input("what day is it today? ").lower()

    if day in days:
        break

    else:
        print("are you sure you didn't mis-type that?")


if day == "tuesday":
    adults = tuesdayprice
    children = tuesdayprice
    students = tuesdayprice
    senior = tuesdayprice
    family = tuesdayprice
    print("its tuesday today so all prices will be £5.40!")


while True:
    time = input("is it before or after 5pm? (before/after)").lower()

    if time == "before" or time == "after":
        break

    else:
        print("are you sure you didn't mis-type that?")


if time == "before":
    adults = adultsbefore
    children = childrenbefore
    students = studentsbefore
    senior = seniorsbefore
    family = familybefore

if time == "after":
    adults = adultsafter
    children = childrenafter
    students = studentsafter
    senior = seniorsafter
    family = familyafter

adulttickets = getnum("how many adult tickets? ") * adults
childrenticket = getnum("how many children tickets? ") * children
studentsticket = getnum("how many student tickets? ") * students
seniorsticket = getnum("how many seniors tickets? ") * senior
familyticket = getnum("how many family tickets? ") * family

total = adulttickets + childrenticket + studentsticket + seniorsticket + familyticket

print(f"your total will be £{total}") 
