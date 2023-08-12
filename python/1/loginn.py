
users = {'Ahmed': '1394', 'Ali': '6078', 'Amr': '9345'}  
  
username = str(input("Enter your username: "))  
password = str(input("Enter your password: "))

if username in users and users[username] == password:  
    print("Welcome")  
else:  
    print("Invalid username or password. Please try again.")  
  
