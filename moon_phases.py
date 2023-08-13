import ephem

def get_moon_phase(x):
    moon_phase = round(ephem.Moon(x).moon_phase,2)
    return moon_phase

your_bday = input("Enter your birthday in the format YYYY-MM-DD: \n")
crush_bday = input("Enter your crush's birthday in the format YYYY-MM-DD \n")

your_phase = get_moon_phase(your_bday)
crush_phase = get_moon_phase(crush_bday)
compatibility_score = round((your_phase+crush_phase)*100,0)

if compatibility_score>=100:
    print(f"Your Compatibility Score is off the charts!! Perfect match at 100%")
else:
    print (f"Your Compatibility Score is {compatibility_score}%!")
