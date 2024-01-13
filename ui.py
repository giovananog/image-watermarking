from tkinter import *
from functions import open_image, watermark_img, select_color, save_img, show_img

# constants to color and fonts
BLACK = "#1C1C1C"
GRAY = "#DCDCDC"
FONT_NAME = "Courier"

# start a new TK window to the application
window = Tk()
window.title("Image Watermarking")
window.config(padx=20, pady=16, bg=GRAY)

title_label = Label(text="Watermarking App", fg=BLACK, bg=GRAY, font=(FONT_NAME, 30))
title_label.grid(column=1, row=0)

# new canvas to manipulate the images
canvas = Canvas(width=320, height=224, bg=BLACK, highlightthickness=0)
canvas.grid(column=1, row=1)
show_img(canvas, "images/default.png")

# this frame contains all options that should be choosen by the user before watermarking the image
frame = Frame(window, padx=10, pady=10, bd=1, relief='solid') 
frame.grid(column=0, row=1) 

text_entry = Entry(frame)
text_entry.insert(0, 'WATERMARK TEXT')
text_entry.grid(column=0, row=2)

upload_button = Button(frame, text="Upload Image", highlightthickness=0, command=lambda: open_image(canvas))
upload_button.grid(column=0, row=3, pady=6)

# button and label to choose and show color
selext_color_button = Button(frame, text="Pick a color", command=lambda: select_color(label_color))
selext_color_button.grid(column=1, row=1, pady=6)

label_color = Label(frame, text=f"{GRAY}", width=10, height=2, relief="solid", bg=GRAY)
label_color.grid(column=0, row=1, pady=6)


# button out of frame 
watermark_button = Button(text="Watermark Image", highlightthickness=0, command=lambda: watermark_img(text_entry.get(), label_color.cget("bg"), canvas ))
watermark_button.grid(column=0, row=2)


# save button 
save_button = Button(text="Save Image", highlightthickness=0, command=save_img)
save_button.grid(column=2, row=4)

# keeps the app running all the time until it gets manually closed
window.mainloop()
