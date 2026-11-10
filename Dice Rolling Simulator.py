import random


def roll_dice():
    print("--- Dice Rolling Simulator ---")

    while True:
        try:
            num_dice = int(input("\nHow many dice do you want to roll? "))
            num_sides = int(
                input("How many sides per die? (e.g., 6, 12, 20): ")
            )

            if num_dice <= 0 or num_sides <= 1:
                print(
                    "Please enter at least 1 die and a minimum of 2 sides."
                )
                continue

            # Generate random rolls using a list comprehension
            rolls = [random.randint(1, num_sides) for _ in range(num_dice)]

            print(f"\nResults: {rolls}")
            print(f"Total: {sum(rolls)}")

        except ValueError:
            print("Invalid input. Please enter whole numbers only.")
            continue

        again = input("\nRoll again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    roll_dice()
