from PIL import Image
import os

src = 'UI-design/assets/suowei_icon.png'
img = Image.open(src).convert('RGBA')
w, h = img.size
crop = img.crop((0, int(h*0.28), int(w*0.72), h))

sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

base = 'app/src/main/res'
for folder, size in sizes.items():
    os.makedirs(f'{base}/{folder}', exist_ok=True)
    icon = crop.resize((size, size), Image.LANCZOS)
    icon.save(f'{base}/{folder}/ic_launcher.png')
    icon.save(f'{base}/{folder}/ic_launcher_round.png')
    print(f'生成 {folder}/{size}px')

print('图标生成完成！')
