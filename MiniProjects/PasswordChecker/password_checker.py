special = "!@#$%^&*()_-+=<>?/"

while True:
    password = input("\nEnter Password: ")

    # Check for space
    if " " in password:
        print("\n❌ Invalid Password")
        print("Reason: Password cannot contain spaces.")
        continue

    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    score = 0

    # Check password characters
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_number = True
        elif char in special:
            has_special = True

    # Calculate score
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15

    if has_upper:
        score += 20

    if has_lower:
        score += 20

    if has_number:
        score += 20

    if has_special:
        score += 15

    print("\n==============================")
    print(f"Password Score: {score}/100")

    # Password strength
    if (
        len(password) >= 12
        and has_upper
        and has_lower
        and has_number
        and has_special
    ):
        print("🟢 Excellent Password")
        print("Your password is highly secure.")
        break

    elif (
        len(password) >= 8
        and has_upper
        and has_lower
        and has_number
        and has_special
    ):
        print("🟢 Strong Password")
        print("Your password is secure.")
        break

    elif len(password) >= 8:
        print("🟡 Medium Password")
    else:
        print("🔴 Weak Password")

    print("\nSuggestions:")

    if len(password) < 8:
        print("✔ Use at least 8 characters.")
    elif len(password) < 12:
        print("✔ Use 12 or more characters for better security.")

    if not has_upper:
        print("✔ Add at least one uppercase letter (A-Z).")

    if not has_lower:
        print("✔ Add at least one lowercase letter (a-z).")

    if not has_number:
        print("✔ Add at least one number (0-9).")

    if not has_special:
        print("✔ Add at least one special character (!@#$%^&*...).")

    print("\nPlease try again.")