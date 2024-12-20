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
            canvas.create_image(400, 300, image=photo)
            canvas.grid(column=1, row=1)
            # image_label.config(image=photo)
            # image_label.image = photo
            # add_text.pack()
            # add_img.pack()
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Could not open image: {e}")

def add_text():
    pass

def add_img():
    pass



# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Watermark Me")
# window.minsize(width=800, height=500)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR)

# Image placeholder
image_label = Label(window, text="No Image Selected")
# image_label.pack()

# target_image = canvas.itemconfig(image_label, image=image_label)
# canvas.grid(column=0, row=0)

# Button to select image
button = Button(window, text="Select Image", command=open_img)
button.grid(column=0, row=0)
# button.pack(pady=20)

# Button to add text as watermark
add_text = Button(window, text="Add Text", command=add_text)


# Button to add image as watermark
add_img = Button(window, text="Add Image", command=add_img)


window.mainloop()