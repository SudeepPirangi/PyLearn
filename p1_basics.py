print("Hello World")
print("20 days are " + str(20 * 24 * 60) + " minutes")
print(f"20 days are {20 * 24 * 60} minutes")

# variables
print("------ variables -------")
to_minutes = 24 * 60
print(f"20 days are {20 * to_minutes * 60} seconds")

# functions with parameters
print("------ functions -------")
def days_to_minutes(days):
    print(f"{days} days are {days * to_minutes} minutes")

days_to_minutes(10)
days_to_minutes(20)

# accepting inputs
print("------ inputs -------")
def input_days_to_minutes():
    days = int(input("Enter number of days to be converted to minutes\n"))
    return f"{days} days are {days * to_minutes} minutes"

print(input_days_to_minutes())