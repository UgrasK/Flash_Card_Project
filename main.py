from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# create window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create canvas
canvas = Canvas(width=800, height=526)
# use an image to show image on canvas
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
# create text to show on canvas
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
# config canvas bg color and border
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# set canvas grid
canvas.grid(row=0, column=0, columnspan=2)

# create buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)





window.mainloop()
