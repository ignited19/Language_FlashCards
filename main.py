from tkinter import *
import FlashCardData as FD

BACKGROUND_COLOR = "#B1DDC6"



def get_card():
    FD.FlashCardData.AcquireNewFlashCardData(data)
    canvas.itemconfig(label_title, text="French")
    canvas.itemconfig(label_word, text=data.current_french_word)

def get_answer():
    canvas.itemconfig(label_title, text="Enlish")
    canvas.itemconfig(label_word, text=data.current_english_word)



#Based upon the dimensions of card_front.png
print("Let's Rock!")
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526

#Init data
data = FD.FlashCardData()
data.load_data()

#TK and background setup
session = Tk()
session.title("FlashCards!")
session.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas = Canvas(session, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
flashCard_img = PhotoImage(file="Resources/images/card_front.png")
canvas.create_image(400,263, image=flashCard_img)

#Buttons
button_right_img = PhotoImage(file="Resources/images/right.png")
button_wrong_img = PhotoImage(file="Resources/images/wrong.png")

button_right = Button(image=button_right_img, command=get_card)
button_right.grid(row=4, column=3)
button_wrong = Button(image=button_wrong_img, command=get_answer)
button_wrong.grid(row=4, column=2)

#Labels
label_title = canvas.create_text(400,150, text="Tile", font=("Ariel", 40, "italic"))
label_word = canvas.create_text(400,263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=2, columnspan= 2)


get_card()

session.mainloop()




