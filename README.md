# Image Watermarking App

## Overview
This Python application allows users to watermark images with custom text and color. The user interface is built using Tkinter, and the image manipulation is performed with the Pillow (PIL) library.

## Files
- **main.py**: Contains the main execution code and Tkinter UI setup.
- **ui.py**: Imports the main function and executes the application.
- **functions.py**: Includes functions for image manipulation, such as opening an image, watermarking, selecting colors, and saving the final result.
- **images**: Folder containing sample images used by the application.

## Dependencies
- Python 3
- Pillow (PIL)
- Tkinter (should be available with Python)

## How to Run
1. Ensure you have Python 3 installed on your system.
2. Install the required libraries using:
   ```bash
   pip install pillow

Run the application by executing `main.py`.

## Functionality

### User Interface
- The main window displays the title "Image Watermarking" and a canvas to show images.
- Users can input watermark text, upload an image, pick a text color, and watermark the image.

### Buttons
- **Upload Image**: Allows users to open a local image file.
- **Pick a color**: Opens a color picker to choose the text color.
- **Watermark Image**: Applies the entered text as a watermark with the chosen color to the uploaded image.
- **Save Image**: Saves the watermarked image to a local file.

## Code Structure
- **main() (main.py)**: Initializes the Tkinter UI and sets up the main window, canvas, and input elements.
- **show_img(canvas, path) (functions.py)**: Resizes and displays an image on the Tkinter canvas.
- **open_image(canvas) (functions.py)**: Opens a local image file using a file dialog and displays it on the canvas.
- **watermark_img(text, text_color, canvas) (functions.py)**: Watermarks the image with the provided text and color.
- **select_color(label) (functions.py)**: Opens a color picker dialog and updates the label with the selected color.
- **save_img() (functions.py)**: Saves the watermarked image to a user-specified file.

## Sample Usage
1. Run the application using `main.py`.
2. Upload an image using the "Upload Image" button.
3. Enter watermark text and choose a text color.
4. Click "Watermark Image" to apply the watermark.
5. Save the watermarked image using the "Save Image" button.

;; Feel free to explore and enhance the application as needed!