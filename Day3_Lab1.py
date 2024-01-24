
#make a def called heating_cooling
#it has two parameters actual temp and desired temp
#if actual temp is < disired temp you would run heat
#if actual temp is > disired temp you would run A/C
#Standby technically is when actual and desired temps are the same so in that case it can..
#..be put into "else"
#ask the user to put in actual temp and desired temp
#make it so after the user is done they get asked if they want to to it again

print("Hey your favorite thermostat here!")

def heating_cooling(actual_temp, desired_temp):

    if actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp < desired_temp:
        print("Run heat")
    else:
        print("Standby")

while True:
    # Test the function with different parameters
    # heating_cooling(72, 70)  # Run heat
    # heating_cooling(75, 80)  # Run A/C
    # heating_cooling(68, 68)  # Standby

    # Prompt the user for actual and desired temperatures
    user_actual_temp = float(input("Enter the actual temperature: "))
    user_desired_temp = float(input("Enter the desired temperature: "))

    # Call the function with user inputs
    heating_cooling(user_actual_temp, user_desired_temp)

    # Ask the user if they want to continue
    user_choice = input("Do you want to do another temperature suggestion? (yes/no): ").lower()
    if user_choice != 'yes':
        break