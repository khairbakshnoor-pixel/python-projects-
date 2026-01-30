# =========================
# Digital Pet Tracker
# =========================

import datetime

# --- Stat change dictionary (CORE REQUIREMENT) ---
ACTIONS = {
    "feed": {"hunger": -20, "happiness": 5, "energy": 0},
    "play": {"hunger": 10, "happiness": 20, "energy": -15},
    "sleep": {"hunger": 5, "happiness": 0, "energy": 30}
}

# --- Initial stats ---
hunger = 50
happiness = 50
energy = 50

# --- Action history ---
action_history = []


# --- Utility Functions ---
def clamp_stat(value):
    if value < 0:
        return 0
    if value > 100:
        return 100
    return value


def display_status():
    print("\n Pet Status:")
    print(f"Hunger: {hunger}")
    print(f"Happiness: {happiness}")
    print(f"Energy: {energy}")
 


# --- Action Functions ---
def feed_pet():
    global hunger, happiness, energy
    hunger += ACTIONS["feed"]["hunger"]
    happiness += ACTIONS["feed"]["happiness"]

    hunger = clamp_stat(hunger)
    happiness = clamp_stat(happiness)

    action_history.append("Fed Pet")
    print("\nYou fed your pet! Hunger decreased by 20.")
    display_status()


def play_pet():
    global hunger, happiness, energy
    hunger += ACTIONS["play"]["hunger"]
    happiness += ACTIONS["play"]["happiness"]
    energy += ACTIONS["play"]["energy"]

    hunger = clamp_stat(hunger)
    happiness = clamp_stat(happiness)
    energy = clamp_stat(energy)

    action_history.append(("Played with Pet", datetime.datetime.now()))
    print("\nYou played with your pet!")
    display_status()


def sleep_pet():
    global hunger, happiness, energy
    hunger += ACTIONS["sleep"]["hunger"]
    energy += ACTIONS["sleep"]["energy"]

    hunger = clamp_stat(hunger)
    energy = clamp_stat(energy)

    action_history.append(("Pet Slept", datetime.datetime.now()))
    print("\nYour pet went to sleep.")
    display_status()


# --- History ---
def view_history():
    print("\n Action History:")
    if not action_history:
        print("No actions taken yet.")
    else:
        for action, timestamp in action_history:
            formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            print(f"- {action} at {formatted_time}")


# --- File I/O ---
def save_pet():
    with open("pet_save.txt", "w") as file:
        file.write(f"{hunger}\n")
        file.write(f"{happiness}\n")
        file.write(f"{energy}\n")


def load_pet():
    global hunger, happiness, energy
    try:
        with open("pet_save.txt", "r") as file:
            hunger = int(file.readline())
            happiness = int(file.readline())
            energy = int(file.readline())
    except FileNotFoundError:
        hunger = happiness = energy = 50


# --- Main Program ---
def main():
    load_pet()
    print(" Welcome to Your Digital Pet!")
    display_status()

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed Pet")
        print("2. Play with Pet")
        print("3. Put Pet to Sleep")
        print("4. Exit")
        print("5. View History")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            feed_pet()
        elif choice == "2":
            play_pet()
        elif choice == "3":
            sleep_pet()
        elif choice == "4":
            save_pet()
            print("\nGoodbye! Your pet has been saved. 🐾")
            break
        elif choice == "5":
            view_history()
        else:
            print("Invalid choice. Please try again.")


# --- Run Program ---
main()