oldpassword=input("What is your current password?: ")
def new_password():
    newpassword=input("What do you want your new password to be?: ")
    if newpassword != oldpassword and len(newpassword) > 5:
        print("Your password has been changed")
    else:
        print("The password you chose is similar to your old password or too short")
new_password()