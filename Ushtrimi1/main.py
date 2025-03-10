import datetime

#Printo "Hello World"  
print("Hello World")


#Print daten aktuale 
current_datetime = datetime.datetime.now()
print(f"Data dhe koha aktuale: {current_datetime}")


#Perdormi i metodes 
def get_user_name():
    while True:
        try:
            #Merr emrin e perdoruesit 
            name = input("Please enter your name: ").strip()
            #Trajtimi i gabimeve
            if not name:
                raise ValueError("Name cannot be empty. Please try again.")
            elif not name.replace(" ", "").isalpha():
                raise ValueError("Name must contain only letters. Please try again.")
            return name
        except ValueError as e:
            print(f"Error: {e}")

#Pershendetni perdoruesin me emer
user_name = get_user_name()
print(f"Hello, {user_name}!")


