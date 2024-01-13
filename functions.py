from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog, colorchooser, PhotoImage

def show_img(canvas, path):
    im = Image.open(path) 
    new_size = (320, 224)
    im_resized = im.resize(new_size)
    im_resized.save("images/resized_img.png")

    tk_image = PhotoImage(file="images/resized_img.png", width=new_size[0], height=new_size[1])

    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.image = tk_image  

def open_image(canvas):
    global img_tk
    path = filedialog.askopenfilename()

    if path:
        image = Image.open(path)
        img_tk = ImageTk.PhotoImage(image)
        image.save('images/original_img.png')
    
    show_img(canvas,'images/original_img.png')

def watermark_img(text, text_color, canvas):
    with Image.open("images/original_img.png").convert("RGBA") as base:

        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        fnt = ImageFont.truetype("fonts/arial.ttf", 80)
        d = ImageDraw.Draw(txt)
        
        d.text((600, 180), text, font=fnt, fill=text_color)

        new_img = Image.alpha_composite(base, txt)

        new_img.save("images/watermarked_img.png")
        show_img(canvas, "images/watermarked_img.png")


def select_color(label):
    color = colorchooser.askcolor(title="Choose a color")[1]
    label.config(text=f"{color}", bg=color)


def save_img():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

    if not file_path:
        return
    
    img = Image.open("images/watermarked_img.png")
    img.save(file_path)


