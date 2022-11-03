"""An app that displays a Kanye West quote using Kanye Rest API and tkinter GUI"""

import requests
from tkinter import *


def get_quote():
    """Generates a new Kanye West quote and displays it to the GUI if it is below 70 characters"""
    quote_api = requests.get(url="https://api.kanye.rest")
    quote_api.raise_for_status()
    quote_json = quote_api.json()
    quote = quote_json["quote"]
    if len(quote) <= 70:
        canvas.itemconfigure(quote_text, text=quote)
    else:
        get_quote()


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="images/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="images/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

icon = PhotoImage(file="images/kanye.png")
window.iconphoto(False, icon)

get_quote()

window.mainloop()
