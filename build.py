#!/usr/bin/env python3
import os
import shutil
import zipfile
from pathlib import Path

print('Building Elasticsearch Head Chrome Extension(Custom)...')

build_dir = 'build'
if os.path.exists(build_dir):
    shutil.rmtree(build_dir)
os.makedirs(build_dir)

files_to_copy = [
    'manifest.json',
    'src/background.js',
    'elasticsearch-head/index.html',
    'elasticsearch-head/app.js',
    'elasticsearch-head/app.css',
    'elasticsearch-head/vendor.js',
    'elasticsearch-head/vendor.css',
    'elasticsearch-head/i18n.js',
    'elasticsearch-head/onload.js',
    'elasticsearch-head/base/favicon.png',
    'elasticsearch-head/base/jquery.min.js',
    'elasticsearch-head/base/loading.gif',
    'elasticsearch-head/base/purecss.css',
    'elasticsearch-head/base/reset.css',
    'elasticsearch-head/fonts/fontawesome-webfont.eot',
    'elasticsearch-head/fonts/fontawesome-webfont.svg',
    'elasticsearch-head/fonts/fontawesome-webfont.ttf',
    'elasticsearch-head/fonts/fontawesome-webfont.woff',
    'elasticsearch-head/fonts/FontAwesome.otf',
    'elasticsearch-head/lang/en_strings.js',
    'elasticsearch-head/lang/fr_strings.js',
    'elasticsearch-head/lang/ja_strings.js',
    'elasticsearch-head/lang/pt_strings.js',
    'elasticsearch-head/lang/tr_strings.js',
    'elasticsearch-head/lang/zh_strings.js',
    'elasticsearch-head/lang/zh-TW_strings.js',
    'icons/esmhead_16x16.png',
    'icons/esmhead_32x32.png',
    'icons/esmhead_48x48.png',
    'icons/esmhead_128x128.png'
]

for file in files_to_copy:
    source_path = file
    dest_path = os.path.join(build_dir, file)
    
    if os.path.exists(source_path):
        dest_dir = os.path.dirname(dest_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)

        shutil.copy2(source_path, dest_path)
        print(f"✓ Copied: {file}")
    else:
        print(f"✗ Missing: {file}")

print('\nBuild completed successfully!')
print('Extension files are ready in the "build" directory.')
print('You can now load the extension in Chrome from the build directory.')

create_zip = input('\nDo you want to create a ZIP file for distribution? (y/n): ').lower().strip()
if create_zip == 'y':
    zip_filename = 'elasticsearch-head-custom-v0.4.4.zip'
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, build_dir)
                zipf.write(file_path, arcname)
                print(f"✓ Added to ZIP: {arcname}")
    
    print(f'\nZIP file created: {zip_filename}')
    print('This ZIP file can be uploaded to the Chrome Web Store or distributed manually.')
