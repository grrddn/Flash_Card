from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice, randint
import pandas as pd

try:
    continue_progress = pd.read_csv(r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\31_Day_31_Flash_Card_V2\flash-card-project-start\data\to_learn.csv")
    data_dict = continue_progress.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv(r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\31_Day_31_Flash_Card_V2\flash-card-project-start\data\french_words.csv")  
    data_dict = data.to_dict(orient="records")




# ---------------- CONSTANTES ----------------#

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Consolas", 40, "bold")
WORD_FONT = ("Consolas", 60, "bold")
RIGHT_BUTTON = r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\31_Day_31_Flash_Card_V2\flash-card-project-start\images\right.png"
LEFT_BUTTON = r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\31_Day_31_Flash_Card_V2\flash-card-project-start\images\wrong.png"
HORIZONTAL = "horizontal"
CURRENT_CARD = {}

# ---------------- FUNCTIONS ----------------#

def random_word(language="French"):
    global CURRENT_CARD
    CURRENT_CARD = choice(data_dict)
    return CURRENT_CARD[language]

def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    random_word("French")
    canvas.itemconfig(card_front, image=card_front_img)
    canvas.itemconfig(upper_label, text="French", fill="black")
    canvas.itemconfig(lower_label, text=CURRENT_CARD["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_front, image=card_back_img)
    canvas.itemconfig(upper_label, text="English", fill="white")
    canvas.itemconfig(lower_label, text=CURRENT_CARD["English"], fill="white")

def is_known():
    global data_dict
    data_dict.remove(CURRENT_CARD)
    print(len(data_dict))
    to_learn = pd.DataFrame(data_dict)
    to_learn.to_csv(r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\31_Day_31_Flash_Card_V2\flash-card-project-start\data\to_learn.csv", index=False)
    next_card()


# ---------------- UI SETUP ----------------#

# Window
window = Tk()
window.title("Flashy Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\31_Day_31_Flash_Card_V2\flash-card-project-start\images\card_front.png")
card_front = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file=r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\31_Day_31_Flash_Card_V2\flash-card-project-start\images\card_back.png")
canvas.grid(row=0, column=0, columnspan=2)
upper_label = canvas.create_text(400, 150, text="French", font= TITLE_FONT)
lower_label = canvas.create_text(400, 263, text="", font=WORD_FONT)

# Separator
separator_line = ttk.Separator(window, orient=HORIZONTAL)
separator_line.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

# Button
right_button_img = PhotoImage(file=RIGHT_BUTTON)
left_button_img = PhotoImage(file=LEFT_BUTTON)
right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.grid(row=2, column=0)
left_button = Button(image=left_button_img, highlightthickness=0, command=is_known)
left_button.grid(row=2, column=1)

next_card()

window.mainloop()

