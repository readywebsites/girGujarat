import os
import sys
import time
import shutil
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image, ImageOps

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / 'scripts' / 'raw_images'
BACKUP_DIR = BASE_DIR / 'assets' / 'backup_original'
IMAGES_DIR = BASE_DIR / 'assets' / 'images'
CROPS_DIR = BASE_DIR / 'assets' / 'crops'

RAW_DIR.mkdir(parents=True, exist_ok=True)
BACKUP_DIR.mkdir(parents=True, exist_ok=True)

# 1. Backup original images
print("--- 1. Backing up original images ---")
for folder in [IMAGES_DIR, CROPS_DIR]:
    target_bak = BACKUP_DIR / folder.name
    if not target_bak.exists():
        shutil.copytree(folder, target_bak)
        print(f"Backed up {folder} to {target_bak}")
    else:
        print(f"Backup already exists at {target_bak}")

# 2. Source definitions from Wikimedia Commons
SOURCES = {
    'hero_lion': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/3/38/Portrait_of_an_Asiatic_lion_at_Gir_National_Park_02.jpg',
        'file': 'hero_lion.jpg',
        'title': 'Portrait of an Asiatic lion at Gir National Park 02',
        'author': 'A. J. T. Johnsingh',
        'license': 'CC BY-SA 4.0'
    },
    'lion_walk': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/1/19/Asiatic_Lion_Royal_Walk_at_Gir_National_Park%2C_Gujrat%2C_India.jpg',
        'file': 'lion_walk.jpg',
        'title': 'Asiatic Lion Royal Walk at Gir National Park, Gujrat, India',
        'author': 'Shaunak Modi',
        'license': 'CC BY-SA 4.0'
    },
    'lion_family': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/d/db/A_lioness_with_cubs_in_gir_forest.jpg',
        'file': 'lion_family.jpg',
        'title': 'A lioness with cubs in gir forest',
        'author': 'Asim Patel',
        'license': 'CC BY-SA 4.0'
    },
    'dwarkadhish': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Dwarkadhish_Temple%2C_Dwarka%2C_Gujarat.JPG',
        'file': 'dwarkadhish.jpg',
        'title': 'Dwarkadhish Temple, Dwarka, Gujarat',
        'author': 'Scaleval',
        'license': 'CC BY-SA 3.0'
    },
    'somnath': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/0/0e/%22_Somnath_Temple%2C_Gujarat_%22.jpg',
        'file': 'somnath.jpg',
        'title': 'Somnath Temple, Gujarat',
        'author': 'Anhilwara',
        'license': 'CC BY-SA 4.0'
    },
    'nageshwar': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/2/29/Lord_Shiva_uniting_heaven_%26_hell.jpg',
        'file': 'nageshwar.jpg',
        'title': 'Lord Shiva uniting heaven & hell (Nageshwar Jyotirling)',
        'author': 'Shravan Prajapati',
        'license': 'CC BY-SA 4.0'
    },
    'deer': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/e/e4/Chital_in_Gir_Forest_National_Park_in_2020_DSCN9920_02.jpg',
        'file': 'deer.jpg',
        'title': 'Chital in Gir Forest National Park',
        'author': 'Dineshkannambadi',
        'license': 'CC BY-SA 4.0'
    },
    'peacock': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/c/c4/Indian_peafowl_%28Pavo_cristatus%29_dancing_male.jpg',
        'file': 'peacock.jpg',
        'title': 'Indian peafowl (Pavo cristatus) dancing male',
        'author': 'Davidvraju',
        'license': 'CC BY-SA 4.0'
    },
    'safari_gypsy': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/e/e2/The_jungle_safari_in_Jhirna_Zone%2C_Jim_Corbett_National_Park.jpg',
        'file': 'safari_gypsy.jpg',
        'title': 'The jungle safari Gypsy in forest',
        'author': 'Pradeep717',
        'license': 'CC BY-SA 4.0'
    },
    'bus': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/8/88/Scania_Metrolink_HD_14.5_M_Ashwamedh.jpg',
        'file': 'bus.jpg',
        'title': 'Scania Metrolink HD Luxury Tour Coach',
        'author': 'MSRTC',
        'license': 'CC BY-SA 4.0'
    },
    'innova': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/8/87/Toyota_Innova_Crysta_2.4_Z_front_right.jpg',
        'file': 'innova.jpg',
        'title': 'Toyota Innova Crysta Tourist Fleet',
        'author': 'Vibhanshu.bansal',
        'license': 'CC BY-SA 4.0'
    },
    'sunset': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/5/57/Sunset_in_Dwarka.jpg',
        'file': 'sunset.jpg',
        'title': 'Sunset in Dwarka over Arabian Sea',
        'author': 'Radhika Gandhi',
        'license': 'CC BY-SA 4.0'
    },
    'aarti': {
        'url': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Ganga_Aarti_Varanasi.jpg',
        'file': 'aarti.jpg',
        'title': 'Maha Aarti brass lamp ceremony',
        'author': 'Dennis Jarvis',
        'license': 'CC BY-SA 4.0'
    }
}

USER_AGENT = 'TravelFirstHolidays/1.0 (Gujarat Spiritual Tour; contact@travelfirstholidays.com)'

def download_file(key, info):
    dest = RAW_DIR / info['file']
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"  [Cache hit] {key} already downloaded ({dest.stat().st_size // 1024} KB)")
        return dest
        
    url = info['url']
    print(f"  Downloading {key} from {url}...")
    
    max_retries = 4
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                dest.write_bytes(data)
                print(f"  Successfully downloaded {key} ({len(data) // 1024} KB)")
                time.sleep(2.5) # Polite delay
                return dest
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_sec = 5 * (attempt + 1)
                print(f"    HTTP 429 (Rate limit) on {key}. Sleeping {wait_sec}s before retry {attempt+1}/{max_retries}...")
                time.sleep(wait_sec)
            else:
                print(f"    HTTP error {e.code} on {key}: {e}")
                time.sleep(2)
        except Exception as e:
            print(f"    Error downloading {key}: {e}")
            time.sleep(2)
            
    print(f"  FAILED to download {key} after {max_retries} attempts.")
    return None

# Download all sources
print("\n--- 2. Downloading high-resolution open-source assets ---")
downloaded = {}
for k, info in SOURCES.items():
    p = download_file(k, info)
    if p and p.exists():
        downloaded[k] = p
    else:
        print(f"Warning: Missing source {k}")

print(f"\nDownloaded {len(downloaded)} / {len(SOURCES)} source assets.")

# 3. Processing and sizing functions
def smart_crop_and_save(src_path, dest_path, width, height, centering=(0.5, 0.5), fmt='JPEG', quality=92):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src_path) as img:
        # Convert RGBA/P to RGB if JPEG
        if fmt == 'JPEG' and img.mode in ('RGBA', 'P', 'LA'):
            img = img.convert('RGB')
        elif fmt == 'PNG' and img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGBA')
            
        cropped = ImageOps.fit(img, (width, height), method=Image.Resampling.LANCZOS, centering=centering)
        if fmt == 'JPEG':
            cropped.save(dest_path, format='JPEG', quality=quality, optimize=True)
        else:
            cropped.save(dest_path, format='PNG', optimize=True)
    print(f"  Generated {dest_path.name} [{width}x{height}, {fmt}] ({dest_path.stat().st_size // 1024} KB)")

# 4. Generate all Retina images in assets/images/
print("\n--- 3. Generating Retina images in assets/images/ ---")
if 'hero_lion' in downloaded:
    smart_crop_and_save(downloaded['hero_lion'], IMAGES_DIR / 'hero_lion_retina.jpg', 1200, 811, centering=(0.5, 0.35))
    
if 'dwarkadhish' in downloaded:
    smart_crop_and_save(downloaded['dwarkadhish'], IMAGES_DIR / 'dwarka_retina.jpg', 1200, 800, centering=(0.5, 0.45))
    
if 'somnath' in downloaded:
    smart_crop_and_save(downloaded['somnath'], IMAGES_DIR / 'somnath_retina.jpg', 1200, 800, centering=(0.5, 0.5))
    
if 'lion_walk' in downloaded:
    smart_crop_and_save(downloaded['lion_walk'], IMAGES_DIR / 'gir_safari_retina.jpg', 1200, 800, centering=(0.5, 0.5))
elif 'hero_lion' in downloaded:
    smart_crop_and_save(downloaded['hero_lion'], IMAGES_DIR / 'gir_safari_retina.jpg', 1200, 800, centering=(0.5, 0.5))
    
if 'lion_family' in downloaded:
    smart_crop_and_save(downloaded['lion_family'], IMAGES_DIR / 'lion_family_retina.jpg', 1200, 800, centering=(0.5, 0.45))
    
if 'deer' in downloaded:
    smart_crop_and_save(downloaded['deer'], IMAGES_DIR / 'deer_retina.jpg', 800, 600, centering=(0.5, 0.45))
    
if 'peacock' in downloaded:
    smart_crop_and_save(downloaded['peacock'], IMAGES_DIR / 'peacock_retina.jpg', 800, 600, centering=(0.5, 0.4))
    
if 'bus' in downloaded:
    smart_crop_and_save(downloaded['bus'], IMAGES_DIR / 'scenic_highway_bus.jpg', 1200, 800, centering=(0.5, 0.5))
    
if 'sunset' in downloaded:
    smart_crop_and_save(downloaded['sunset'], IMAGES_DIR / 'temple_sunset_retina.jpg', 1200, 800, centering=(0.5, 0.45))

# 5. Generate all crops in assets/crops/
print("\n--- 4. Generating UI card crops in assets/crops/ ---")

# Hero Montage (244x385 - vertical hero portrait)
if 'hero_lion' in downloaded:
    smart_crop_and_save(downloaded['hero_lion'], CROPS_DIR / 'hero_montage.png', 488, 770, centering=(0.5, 0.35), fmt='PNG')

# Package Vehicles (224x220 - tour transport fleet)
if 'innova' in downloaded:
    smart_crop_and_save(downloaded['innova'], CROPS_DIR / 'package_vehicles.png', 448, 440, centering=(0.5, 0.5), fmt='PNG')
elif 'bus' in downloaded:
    smart_crop_and_save(downloaded['bus'], CROPS_DIR / 'package_vehicles.png', 448, 440, centering=(0.5, 0.5), fmt='PNG')

# Destination Cards (220x120 -> 440x240 for 2x retina)
if 'dwarkadhish' in downloaded:
    smart_crop_and_save(downloaded['dwarkadhish'], CROPS_DIR / 'dest_dwarka.png', 440, 240, centering=(0.5, 0.45), fmt='PNG')
    smart_crop_and_save(downloaded['dwarkadhish'], CROPS_DIR / 'dwarka_spotlight.png', 450, 330, centering=(0.5, 0.45), fmt='PNG')

if 'somnath' in downloaded:
    smart_crop_and_save(downloaded['somnath'], CROPS_DIR / 'dest_somnath.png', 440, 240, centering=(0.5, 0.5), fmt='PNG')
    smart_crop_and_save(downloaded['somnath'], CROPS_DIR / 'somnath_spotlight.png', 450, 330, centering=(0.5, 0.5), fmt='PNG')

if 'lion_walk' in downloaded:
    smart_crop_and_save(downloaded['lion_walk'], CROPS_DIR / 'dest_gir.png', 440, 240, centering=(0.5, 0.5), fmt='PNG')
elif 'hero_lion' in downloaded:
    smart_crop_and_save(downloaded['hero_lion'], CROPS_DIR / 'dest_gir.png', 440, 240, centering=(0.5, 0.5), fmt='PNG')

if 'nageshwar' in downloaded:
    smart_crop_and_save(downloaded['nageshwar'], CROPS_DIR / 'dest_nageshwar.png', 440, 240, centering=(0.5, 0.3), fmt='PNG')

# Gir Showcase Video & Thumbs
if 'lion_family' in downloaded:
    smart_crop_and_save(downloaded['lion_family'], CROPS_DIR / 'gir_video_thumb.png', 430, 400, centering=(0.5, 0.45), fmt='PNG')

if 'peacock' in downloaded:
    smart_crop_and_save(downloaded['peacock'], CROPS_DIR / 'gir_thumb_1.png', 130, 90, centering=(0.5, 0.35), fmt='PNG')

if 'safari_gypsy' in downloaded:
    smart_crop_and_save(downloaded['safari_gypsy'], CROPS_DIR / 'gir_thumb_2.png', 140, 90, centering=(0.5, 0.5), fmt='PNG')

if 'deer' in downloaded:
    smart_crop_and_save(downloaded['deer'], CROPS_DIR / 'gir_thumb_3.png', 140, 90, centering=(0.5, 0.4), fmt='PNG')

# Itinerary Day Thumbnails (45x45 -> 90x90 for 2x retina)
# Day 1: Dwarka arrival & temple
if 'dwarkadhish' in downloaded:
    smart_crop_and_save(downloaded['dwarkadhish'], CROPS_DIR / 'day1_thumb.png', 90, 90, centering=(0.5, 0.4), fmt='PNG')

# Day 2: Somnath ocean temple
if 'somnath' in downloaded:
    smart_crop_and_save(downloaded['somnath'], CROPS_DIR / 'day2_thumb.png', 90, 90, centering=(0.5, 0.5), fmt='PNG')

# Day 3: Gir resort / arrival / lion walk
if 'lion_walk' in downloaded:
    smart_crop_and_save(downloaded['lion_walk'], CROPS_DIR / 'day3_thumb.png', 90, 90, centering=(0.5, 0.5), fmt='PNG')
elif 'hero_lion' in downloaded:
    smart_crop_and_save(downloaded['hero_lion'], CROPS_DIR / 'day3_thumb.png', 90, 90, centering=(0.5, 0.5), fmt='PNG')

# Day 4: Morning Gypsy Safari
if 'safari_gypsy' in downloaded:
    smart_crop_and_save(downloaded['safari_gypsy'], CROPS_DIR / 'day4_thumb.png', 90, 90, centering=(0.5, 0.5), fmt='PNG')

# Moments Strip (Through the Lens)
# lens 1: Temple Aarti / Lamp ceremony
if 'aarti' in downloaded:
    smart_crop_and_save(downloaded['aarti'], CROPS_DIR / 'lens_photo_1.png', 114, 200, centering=(0.5, 0.5), fmt='PNG')

# lens 2: Lion family / cubs
if 'lion_family' in downloaded:
    smart_crop_and_save(downloaded['lion_family'], CROPS_DIR / 'lens_photo_2.png', 150, 200, centering=(0.5, 0.5), fmt='PNG')

# lens 3: Somnath temple ocean view
if 'somnath' in downloaded:
    smart_crop_and_save(downloaded['somnath'], CROPS_DIR / 'lens_photo_3.png', 120, 200, centering=(0.5, 0.5), fmt='PNG')

# Footer Banner (215x120 -> 430x240 for retina)
if 'sunset' in downloaded:
    smart_crop_and_save(downloaded['sunset'], CROPS_DIR / 'footer_banner.png', 430, 240, centering=(0.5, 0.5), fmt='PNG')
elif 'somnath' in downloaded:
    smart_crop_and_save(downloaded['somnath'], CROPS_DIR / 'footer_banner.png', 430, 240, centering=(0.5, 0.5), fmt='PNG')

print("\n--- Asset generation complete! ---")

