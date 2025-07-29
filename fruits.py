# Initial list of fruits
fruits = ["apple", "banana", "cherry"]

# Display total number of fruits
print(f"Total fruits in the list: {len(fruits)}\n")

# Loop with index and value
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit.title()}")

    # Check if the fruit name contains the letter 'a'
    if 'a' in fruit:
        print(f"   → '{fruit}' contains the letter 'a'.")
    else:
        print(f"   → '{fruit}' does NOT contain the letter 'a'.")

    # Suggest a juice
    print(f"   → You can make fresh {fruit} juice!\n")

# Ask the user if they want to add another fruit
new_fruit = input("Would you like to add another fruit? Type it here: ").strip().lower()

if new_fruit:
    if new_fruit in fruits:
        print(f"'{new_fruit}' is already in the list.")
    else:
        fruits.append(new_fruit)
        print(f"'{new_fruit}' has been added to the list!")

# Display updated list
print("\nUpdated fruit list:")
for f in fruits:
    print(f"🍉 {f.capitalize()}")

