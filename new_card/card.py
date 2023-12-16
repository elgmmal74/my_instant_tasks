import os
import random


def generate_card(card_amount):
    amount_prefix = ""
    if card_amount == "10":
        amount_prefix = "10"
    elif card_amount == "50":
        amount_prefix = "50"
    elif card_amount == "100":
        amount_prefix = "100"

    if amount_prefix:
        card_number = amount_prefix + "".join(random.choices("0123456789", k=13))
        return card_number
    else:
        return None


def save_to_file(card_number, file_path):
    with open(file_path, "a") as file:
        file.write(card_number + "\n")


def main():
    card_amount = input("Enter the card amount (10, 50, 100): ")

    if card_amount not in ["10", "50", "100"]:
        print("Invalid card amount.")
        return

    card_number = generate_card(card_amount)
    if card_number:
        print(f"Generated card number: {card_number}")

        file_name = "generated_cards_all.txt"
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        save_to_file(card_number, file_path)
        print(f"Card number saved to {file_name}")
    else:
        print("Invalid card amount.")


if __name__ == "__main__":
    main()
