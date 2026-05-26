import sys
import os
from PIL import Image

app_dir = 'app'

if os.path.exists(f'{app_dir}/build/icon_1024.png'):
    import shutil
    shutil.copy(f'{app_dir}/build/icon_1024.png', f'{app_dir}/assets/icon.png')
    print('Used icon_1024.png directly')
elif os.path.exists(f'{app_dir}/build/icon.png'):
    img = Image.open(f'{app_dir}/build/icon.png').convert('RGBA')
    img = img.resize((1024, 1024), Image.LANCZOS)
    os.makedirs(f'{app_dir}/assets', exist_ok=True)
    img.save(f'{app_dir}/assets/icon.png', 'PNG')
    print('Icon resized to 1024x1024')
else:
    print('ERROR: No icon found!')
    sys.exit(1)

img = Image.open(f'{app_dir}/assets/icon.png')
print('Final icon size:', img.size)
