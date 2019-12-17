# Lei Shi
# 0985491
# MSITM6341
# Bonus Homework 1
# 12/16/2019

filename = 'emai_list.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("No stored information found.")
    input_email = input("Enter the email address you would like to store? ")
    with open(filename,"a") as f_obj:
        f_obj.write(input_email)
    if input_email != "":
        print("Information saved.")
else:
    print("Email address loaded: " + contents)