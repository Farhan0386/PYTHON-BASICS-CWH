print("HOSPITAL APPOINTMENT SYSTEM ")
print()
# Using dictionary to store user data
user_data = {}
user_data["name"] = input("Enter Name: ")
user_data["age"] = input("Enter Age: ")
user_data["gender"] = input("Enter Gender: ")
user_data["dob"] = input("Enter Date of Birth: ")
user_data["mobile"] = input("Enter Mobile Number: ")
user_data["email"] = input("Enter Email: ")
user_data["doctor"] = input("Enter Doctor Name: ")
user_data["date"] = input("Enter Appointment Date: ")
user_data["time"] = input("Enter Time: ")
print()
print(f"\n{user_data['name']} User data collected!")
available_doctors = ["Dr abc", "Dr rahul", "Dr xyz"]
if user_data["doctor"] in available_doctors:
    print("Doctor is available!")
else:
    print("Doctor not available. Choose from:", available_doctors)
    user_data["doctor"] = input("Enter new doctor: ")
print()
print("Payment: Rs. 500")
upi_id = input("Enter your UPI ID: ")
if upi_id != "":
    print("Processing payment...\nDo not close app\nopen upi app to confirm payment")
    print("Payment successful!")
    payment_done = "yes"
else:
    print("Payment failed.")
print()
token_number = 1
if payment_done == "yes":
    token = token_number
    print(f"You are token number: {token}")
    print(f"SMS sent to {user_data['mobile']}")
    print(f"Email sent to {user_data['email']}")
    print("Appointment confirmed!")
    token_number = token_number + 1  # Next patient will get token 2, 3, 4, and so on.