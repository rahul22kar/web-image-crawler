import os
import json
import hashlib
import requests

from urllib.parse import urlparse

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None


def get_image_filename(img_url, default_extension='.jpg'):
    parsed_url = urlparse(img_url)
    basename = os.path.basename(parsed_url.path)
    if not os.path.splitext(basename)[1]:
        basename += default_extension
    # Use a hash to avoid filename conflicts
    hash_digest = hashlib.md5(img_url.encode('utf-8')).hexdigest()
    return f"{hash_digest}_{basename}"