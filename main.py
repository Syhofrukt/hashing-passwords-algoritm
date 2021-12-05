from password_hashing import PasswordHandler


if __name__ == "__main__":

    user_password = str(input("Put your password: "))
    hash_algoritm = str(input("Put a hash algoritm for PasswordHandler: "))
    coding_algoritm = str(input("Put a coding algoritm for PasswordHandler: "))
    pepper = str(input("Put a pepper for PasswordHandler: "))

    ClassName = PasswordHandler(hash_algoritm, coding_algoritm, pepper)
    hashed_password = ClassName.hash_password_with_salt(user_password)
    verify = ClassName.verify_password(user_password, hashed_password)

    print("Hashed password: " + hashed_password)
    print("Password equal: " + str(verify))
