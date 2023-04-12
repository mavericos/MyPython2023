from PIL import Image

def resize_image(image_path):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        img = img.resize((800, 800))
        img.save('image24.jpg', 'JPEG')

if __name__ == '__main__':
    resize_image('')
    # Replace with the path of your PDF or JPG image file
