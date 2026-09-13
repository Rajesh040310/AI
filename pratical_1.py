# Print welcome messages
print("Hello! I am Python.")
print("Today we will build a cleaning robot together.")

# D = Dirty, C = Clean

# Initial state of the room
room = ["D", "D", "D", "D", "C"]


# Function to display the room
def show_room(room):
    print(room)


# Function to clean a single spot
def clean_spot(spot):

    # If the spot is dirty, make it clean
    if spot == "D":
        return "C"

    # If already clean, keep it clean
    else:
        return "C"


# Display room before cleaning
print("\nRoom before cleaning:")
show_room(room)


# Loop through every position in the room
for i in range(len(room)):

    # Clean the current spot
    room[i] = clean_spot(room[i])

    # Display which spot was cleaned
    print("After cleaning spot number", i + 1, ":")

    # Show the updated room
    show_room(room)

    print()
