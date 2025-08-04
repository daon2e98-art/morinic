from PIL import Image, ImageDraw, ImageFont
import zipfile
import os

def translate_images(image_paths, output_zip_path):
    os.makedirs("temp", exist_ok=True)
    font = ImageFont.load_default()

    output_images = []
    for image_path in image_paths:
        img = Image.open(image_path).convert("RGB")
        draw = ImageDraw.Draw(img)
        # 예시 텍스트 위치 및 내용
        draw.text((10, 10), "자동 번역된 마케팅 문구", fill="black", font=font)
        output_path = os.path.join("temp", os.path.basename(image_path))
        img.save(output_path)
        output_images.append(output_path)

    with zipfile.ZipFile(output_zip_path, 'w') as zipf:
        for img_path in output_images:
            zipf.write(img_path, os.path.basename(img_path))
