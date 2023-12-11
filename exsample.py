firstName=input("Enter Your First Name: ").strip().capitalize()
midName=input("Enter Your Mid Name: ").strip().capitalize()
lastName=input("Enter Your Last Name: ").strip().capitalize()
email=input("Enter Your Email: ").strip()
country=input("Enter Your Country: ").strip().capitalize()
if country == "Palitine" :
      print(f"Welcome {firstName} {midName:.1s} {lastName} palstine")
      print(f"Your Domain is: {email[:email.index('@')]} and website is {email[email.index('@')+1:]}")
elif country == "Jordan":
      print(f"Welcome {firstName} {midName:.1s} {lastName} Joradan")
      print(f"Your Domain is: {email[:email.index('@')]} and website is {email[email.index('@')+1:]}")
else:
      print("hiiiii")