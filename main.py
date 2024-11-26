# Step 1: Upload Pictures
# Step 2: Add Text or Logo for watermark
# Step 3: Apply watermark
from tkinter import *
from tkinter import filedialog

import tkinter.messagebox
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"

def open_img():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.png *.jpeg"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Could not open image: {e}")



# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Watermark Me")
window.minsize(width=800, height=500)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=800, height=00, bg=BACKGROUND_COLOR)

# Button to select image
button = Button(window, text="Select Image", command=open_img)
button.pack(pady=20)

# Image placeholder
image_label = Label(window, text="No Image Selected")
image_label.pack()


window.mainloop()