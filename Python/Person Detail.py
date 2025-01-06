import datetime
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_valid_date():
    while True:
        try:
            year = int(input("Enter your birth year: "))
            month = int(input("Enter your birth month (1-12): "))
            day = int(input("Enter your birth day (1-31): "))
            
            if not (1900 <= year <= date.today().year):
                print("Please enter a valid year between 1900 and present")
                continue
                
            if not (1 <= month <= 12):
                print("Please enter a valid month (1-12)")
                continue
                
            if not (1 <= day <= 31):
                print("Please enter a valid day (1-31)")
                continue
                
            return datetime.date(year, month, day)
            
        except ValueError:
            print("Invalid date! Please try again.")

def main():
    print("\n=== Personal Details Form ===\n")
    
    # Get name
    while True:
        name = input("Enter your name: ").strip()
        if name and all(char.isalpha() or char.isspace() for char in name):
            break
        print("Please enter a valid name (letters and spaces only)")
    
    # Get date of birth and calculate age
    print("\nEnter your date of birth:")
    dob = get_valid_date()
    age = calculate_age(dob)
    
    # Get education
    degrees = [
        "High School",
        "Bachelor's",
        "Master's",
        "PhD",
        "Other"
    ]
    
    print("\nSelect your highest education level:")
    for i, degree in enumerate(degrees, 1):
        print(f"{i}. {degree}")
        
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(degrees):
                education = degrees[choice-1]
                break
            print(f"Please enter a number between 1 and {len(degrees)}")
        except ValueError:
            print("Please enter a valid number")
    
    # Get aim in life
    aim_in_life = input("\nWhat is your aim in life? ")
    
    # Display all information with personalized messages
    print("\n" + "="*50)
    print("🌟 PERSONAL PROFILE SUMMARY 🌟".center(50))
    print("="*50)
    
    # Name section
    print(f"\n📌 Name: {name.title()}")
    print(f"    Hello {name.split()[0].title()}! Great to meet you!")
    
    # Age section
    print(f"\n🎂 Date of Birth: {dob.strftime('%B %d, %Y')}")
    print(f"📅 Age: {age} years")
    if age < 20:
        print("    You have a wonderful journey ahead!")
    elif age < 30:
        print("    The perfect age to chase your dreams!")
    else:
        print("    Age is just a number - keep pursuing your goals!")
    
    # Education section
    print(f"\n🎓 Education: {education}")
    education_messages = {
        "High School": "    A great foundation for future success!",
        "Bachelor's": "    Excellent academic achievement!",
        "Master's": "    Advanced knowledge and expertise!",
        "PhD": "    Outstanding commitment to academia!",
        "Other": "    Learning comes in many forms!"
    }
    print(education_messages[education])
    
    # Life goal section
    print(f"\n🎯 Life Goal: {aim_in_life}")
    print("    That's an inspiring ambition!")
    
    # Final motivation
    print("\n" + "-"*50)
    print("💫 Remember: Every great achievement begins with the".center(50))
    print("decision to try! 💫".center(50))
    print("-"*50)
    
    # Save option
    save_choice = input("\nWould you like to save your profile? (yes/no): ").lower()
    if save_choice.startswith('y'):
        with open(f"{name.lower()}_profile.txt", "w") as file:
            file.write(f"Personal Profile for {name.title()}\n")
            file.write("="*30 + "\n")
            file.write(f"Date of Birth: {dob.strftime('%B %d, %Y')}\n")
            file.write(f"Age: {age} years\n")
            file.write(f"Education: {education}\n")
            file.write(f"Life Goal: {aim_in_life}\n")
        print(f"\nProfile saved as '{name.lower()}_profile.txt'!")
    
    print("\nThank you for sharing your details! Have a great day! 👋\n")

if __name__ == "__main__":
    main()