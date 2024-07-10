import os
import sys

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.request import urlretrieve

from utils import create_folder, save_json, is_valid_url, get_image_filename, fetch_page

def extract_images(soup, page_url, depth, images_folder):
    images = []
    for img in soup.find_all('img'):
        img_url = img.get('src')
        if img_url:
            img_url = urljoin(page_url, img_url)
            if is_valid_url(img_url):
                try:
                    img_filename = get_image_filename(img_url)
                    img_filepath = os.path.join(images_folder, img_filename)
                    urlretrieve(img_url, img_filepath)
                    images.append({"url": img_url, "page": page_url, "depth": depth, "filename": img_filename})
                    print(f"Downloaded image {img_url} to {img_filepath}")
                except Exception as e:
                    print(f"Failed to download image {img_url}: {e}")
    return images


def extract_links(soup, page_url):
    links = []
    for a in soup.find_all('a', href=True):
        link = a['href']
        link = urljoin(page_url, link)
        link, _ = urldefrag(link)  # Remove URL fragment
        if is_valid_url(link):
            links.append(link)
    return links


def crawl_page(url, depth, max_depth, seen_urls, images, images_folder):
    if depth > max_depth or url in seen_urls:
        return
    seen_urls.add(url)

    page_content = fetch_page(url)
    if not page_content:
        return

    soup = BeautifulSoup(page_content, 'html.parser')
    images.extend(extract_images(soup, url, depth, images_folder))

    if depth < max_depth:
        links = extract_links(soup, url)
        for link in links:
            crawl_page(link, depth + 1, max_depth, seen_urls, images, images_folder)


def main(start_url, depth):
    parsed_url = urlparse(start_url)
    site_name = parsed_url.netloc.replace('.', '_')
    images_folder = f'images_{site_name}'
    create_folder(images_folder)

    seen_urls = set()
    images = []

    crawl_page(start_url, 1, depth, seen_urls, images, images_folder)

    index_path = os.path.join(images_folder, 'index.json')
    save_json({"images": images}, index_path)
    print(f"Crawling finished. Results saved to {index_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: crawl <start_url> <depth>")
        sys.exit(1)

    start_url = sys.argv[1]
    depth = int(sys.argv[2])

    if not is_valid_url(start_url):
        print("Invalid start URL.")
        sys.exit(1)

    main(start_url, depth)
