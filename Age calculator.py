from datetime import datetime, date

while True:
    dob = input("Enter your Date of Birth (DD-MM-YYYY): ")

    try:
        birthdate = datetime.strptime(dob, "%d-%m-%Y").date()

        if birthdate > date.today():
            print("❌ Date of birth cannot be in the future. Try again.\n")
            continue

        today = date.today()
        age = today.year - birthdate.year

        # If birthday not yet reached this year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        print(f"🎉 You are {age} years old.")

        # Optional: check for birthday
        if today.day == birthdate.day and today.month == birthdate.month:
            print("🎂 Happy Birthday! 🥳")

    except ValueError:
        print("❌ Invalid format! Please enter as DD-MM-YYYY.\n")
        continue

    again = input("\nDo you want to check another age? (yes/no): ").lower()
    if again not in ("yes", "y"):
        print("Goodbye 👋")
        break