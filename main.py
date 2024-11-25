# Step 1: Upload Pictures
# Step 2: Add Text or Logo for watermark
# Step 3: Apply watermark
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Watermark Me")
window.minsize(width=800, height=500)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR)


window.mainloop()