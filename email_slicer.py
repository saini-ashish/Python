while True:
    print()
    email = input("Enter Your Email: ").strip()
    print()

    if email.count('@') == 1 and len(email[:email.index('@')]) > 0 and len(email[email.index('@') + 1:]) > 3:
        print("Username: ", email[:email.index('@')])
        print("Domain:   ", email[email.index('@') + 1:].upper())
    else:
        print("Invalid email!")