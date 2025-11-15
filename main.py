from PIL import Image
import os

input_folder = r"input_folder"
output_folder = r"output_folder"
os.makedirs(output_folder, exist_ok=True)

# Sadece en-boy oranı giriliyor (örn. 4/3)
aspect_ratio = 4 / 5  

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(os.path.join(input_folder, filename))
        
        # Orijinal boyutları al
        orig_width, orig_height = img.size
        
        # En büyük kenarı bul
        max_side = max(orig_width, orig_height)
        
        # Yeni boyutları hesapla
        if orig_width >= orig_height:
            new_width = max_side
            new_height = int(max_side / aspect_ratio)
        else:
            new_height = max_side
            new_width = int(max_side * aspect_ratio)
        
        # Siyah arka plan oluştur
        new_img = Image.new("RGB", (new_width, new_height), (0, 0, 0))
        
        # Oranlı boyutlandır (resim küçültülür ama büyütülmez)
        img.thumbnail((new_width, new_height), Image.LANCZOS)
        
        # Ortala
        x = (new_width - img.width) // 2
        y = (new_height - img.height) // 2
        new_img.paste(img, (x, y))
        
        # Kaydet
        new_img.save(os.path.join(output_folder, filename))
