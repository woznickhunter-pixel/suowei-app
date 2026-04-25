from PIL import Image, ImageDraw, ImageFont
import os

sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

for folder, size in sizes.items():
    os.makedirs(f'app/src/main/res/{folder}', exist_ok=True)
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([0, 0, size-1, size-1], radius=size//5, fill=(28, 28, 32, 255))
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', int(size*0.55))
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), 'S', font=font)
    x = (size - (bbox[2]-bbox[0])) // 2 - bbox[0]
    y = (size - (bbox[3]-bbox[1])) // 2 - bbox[1]
    draw.text((x, y), 'S', fill=(255, 255, 255, 255), font=font)
    img.save(f'app/src/main/res/{folder}/ic_launcher.png')
    img.save(f'app/src/main/res/{folder}/ic_launcher_round.png')

print("Icons generated successfully!")
