from PIL import Image
import os

def resize_image(image_path, output_dir, index):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        img = img.resize((800, 800))
        output_path = os.path.join(output_dir, 'image' + str(index) + '.jpg')
        img.save(output_path, 'JPEG')

if __name__ == '__main__':
    input_dir = 'D:\AI Generated Images\Ai Season 5' # Replace with the path of your input directory containing the image files
    output_dir = 'E:\VS porj\AI Gallery\Resizeds5' # Replace with the path of your output directory for the resized images
    os.makedirs(output_dir, exist_ok=True) # create the output directory if it doesn't exist
    index = 1
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.bmp') or filename.endswith('.pdf'): # Add more file extensions if needed
            resize_image(os.path.join(input_dir, filename), output_dir, index)
            index += 1
