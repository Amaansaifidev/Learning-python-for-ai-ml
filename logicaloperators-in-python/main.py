is_drunk = input("Are you drunk? (true/false): ").strip().lower() == "true"
knows_driving = input("Do you know driving? (true/false): ").strip().lower() == "true"

if knows_driving and not is_drunk:
    print("You can drive")
elif not knows_driving or is_drunk:
    print("You cannot drive")
