import streamlit as st
from PIL import Image, ImageDraw
import base64

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to make an image circular and resize it
def make_circle(image_path, size=(100, 100)):
    img = Image.open(image_path).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)

    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)

    result = Image.new('RGBA', img.size, (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    return result

# Function to place circular image further to the right in the first column
def make_circle_in_column(image_path, circle_size=(200, 200),
                          canvas_width_multiplier=3, right_shift_factor=0.5):
    img = Image.open(image_path).convert("RGBA")
    img = img.resize(circle_size, Image.LANCZOS)

    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)

    circular_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
    circular_img.paste(img, (0, 0), mask)

    canvas_size = (circle_size[0] * canvas_width_multiplier, circle_size[1])
    final_result = Image.new('RGBA', canvas_size, (255, 255, 255, 0))

    x_position = ((circle_size[0] // 2) - (circular_img.width // 2)
                  + int(circle_size[0] * right_shift_factor))
    y_position = (canvas_size[1] // 2) - (circular_img.height // 2)

    final_result.paste(circular_img, (x_position, y_position), circular_img)
    return final_result

# Function to add space
def add_space(n):
    for _ in range(n):
        st.write("")