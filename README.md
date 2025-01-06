# Personal Profile Builder

This Python script is a simple personal profile builder that collects your details, such as name, date of birth, education, and life goals, and then generates a personalized profile summary. You also have the option to save the profile to a text file.

## Features
- **User Input**: Collects user input such as name, date of birth, education level, and life goals.
- **Age Calculation**: Automatically calculates your age based on the date of birth provided.
- **Personalized Output**: Displays a custom profile summary with motivational messages based on your age and education.
- **Save Profile**: Saves the generated profile to a text file, with a personalized filename based on your name.

## Symbols Used
- `🎂 Date of Birth`: Displays your date of birth in a readable format.
- `📅 Age`: Displays your calculated age and a motivational message based on your age.
- `🎓 Education`: Displays your highest level of education and a corresponding message.
- `🎯 Life Goal`: Displays your life goal with an inspiring message.
- `💫`: The final motivational message to encourage you to pursue your goals.

## Code Breakdown

### 1. **Age Calculation**
   - The `calculate_age()` function calculates the user's age by comparing their birth year, month, and day with the current date.

### 2. **Input Validation**
   - The `get_valid_date()` function ensures that the user enters a valid birth date, checking for correct year, month, and day ranges.

### 3. **Profile Summary**
   - After gathering the user's input, the script generates a personalized profile summary and displays it, including motivational comments based on the user's age and education level.

### 4. **Saving the Profile**
   - The user is asked if they would like to save the generated profile. If they choose "yes", the profile is saved in a `.txt` file with a filename based on their name.

## Example Output

```plaintext
=== Personal Details Form ===

Enter your name: John Doe

Enter your date of birth:
Enter your birth year: 1995
Enter your birth month (1-12): 5
Enter your birth day (1-31): 15

Select your highest education level:
1. High School
2. Bachelor's
3. Master's
4. PhD
5. Other

Enter the number of your choice: 2

What is your aim in life? To become a software engineer

==================================================
🌟 PERSONAL PROFILE SUMMARY 🌟
==================================================

📌 Name: John Doe
    Hello John! Great to meet you!

🎂 Date of Birth: May 15, 1995
📅 Age: 29 years
    The perfect age to chase your dreams!

🎓 Education: Bachelor's
    Excellent academic achievement!

🎯 Life Goal: To become a software engineer
    That's an inspiring ambition!

--------------------------------------------------
💫 Remember: Every great achievement begins with the
decision to try! 💫
--------------------------------------------------

Would you like to save your profile? (yes/no): yes
Profile saved as 'john_doe_profile.txt'!

Thank you for sharing your details! Have a great day! 👋
