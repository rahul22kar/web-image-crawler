
---

# Web Image Crawler

This is a simple command-line web crawler that downloads images from a specified URL up to a given depth and saves them in a folder named with the site's name. It also generates a JSON file containing the URLs and depths of the downloaded images.

## Setup Instructions

### Step 1: Clone the Repository

First, clone the repository to your local machine. If you haven't done so already:

```sh
git clone https://github.com/your-repository/web-image-crawler.git
cd web-image-crawler
```

### Step 2: Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Follow these steps to set up a virtual environment:

1. **Install `virtualenv`** (if you don't have it installed):
   ```sh
   pip install virtualenv
   ```

2. **Create a virtual environment**:
   ```sh
   virtualenv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

### Step 3: Install Required Packages

Install the required packages using the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

### Step 4: Running the Crawler

Run the crawler by providing the start URL and depth as command-line arguments:

```sh
python crawler.py <start_url> <depth>
```

- `<start_url>`: The URL where the crawling starts.
- `<depth>`: The crawl child pages depth, where 1 is only the page given in `start_url`.

### Example

To start crawling from `https://example.com` with a depth of 2:

```sh
python crawler.py https://example.com 2
```

## Output

The crawler will create a folder named `images_<sitename>`, where `<sitename>` is derived from the start URL's hostname. This folder will contain:

- Downloaded images.
- `index.json`: A JSON file listing the collected images with their URLs, the page URL where they were found, and the depth.

## Deactivating the Virtual Environment

Once you are done, you can deactivate the virtual environment by running:

```sh
deactivate
```

---

### Notes

- Ensure that the start URL is valid and accessible.
- The script is designed to handle relative URLs and image URLs without extensions by appending a default `.jpg` extension.