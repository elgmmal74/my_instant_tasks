import os
import tkinter as tk
from tkinter import messagebox


def load_generated_cards(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return set(file.read().splitlines())
    else:
        return set()


def load_charged_cards(file_path):
    try:
        with open(file_path, "r") as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()


def save_to_charged_cards(card_number, file_path):
    with open(file_path, "a") as file:
        file.write(card_number + "\n")


def charge_card():
    card_number = card_entry.get()

    if card_number == "":
        messagebox.showerror("Error", "Please enter a card number.")
        return

    generated_cards = load_generated_cards(generated_cards_path)
    charged_cards = load_charged_cards(charged_cards_path)

    if card_number in generated_cards:
        if card_number in charged_cards:
            messagebox.showinfo("Information", "Card already charged.")
        else:
            save_to_charged_cards(card_number, charged_cards_path)
            messagebox.showinfo("Success", "Card charged successfully.")

            # جزء التعديل ليظهر رسالة بناءً على قيمة البطاقة المشحونة
            card_amount = None
            if card_number.startswith("10"):
                card_amount = "10"
            elif card_number.startswith("50"):
                card_amount = "50"
            elif card_number.startswith("100"):
                card_amount = "100"

            if card_amount:
                messagebox.showinfo(
                    "Information", f"Charged card of amount {card_amount}."
                )
            else:
                messagebox.showerror("Error", "Invalid card amount.")

    else:
        messagebox.showerror("Error", "Invalid card number.")


root = tk.Tk()
root.title("Card Charging System")

folder_path = os.path.dirname(__file__)
generated_cards_name = "generated_cards_all.txt"
charged_cards_name = "charged_cards.txt"

generated_cards_path = os.path.join(folder_path, generated_cards_name)
charged_cards_path = os.path.join(folder_path, charged_cards_name)

card_label = tk.Label(root, text="Enter the card number:")
card_label.pack()

card_entry = tk.Entry(root, width=30)
card_entry.pack()

charge_button = tk.Button(root, text="Charge", command=charge_card)
charge_button.pack()

root.mainloop()
