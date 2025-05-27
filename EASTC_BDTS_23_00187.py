import subprocess
import sys

def install_if_missing(package):
    try:
        __import__(package)
        print(f"{package} is already installed")
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = ['pandas', 'requests', 'bs4', 'lxml']

for pkg in packages:
    install_if_missing(pkg)
    
import requests
from bs4 import BeautifulSoup
import pandas as pd

print("✅ Libraries imported successfully")

# NECTA CSEE 2024 main results page (example URL)
url = "https://www.necta.go.tz/results/2023/csee/index.htm"  
headers = {"User-Agent": "Mozilla/5.0"}

print(f"✅ Target URL: {url}")
  
response = requests.get(url, headers=headers)
print(f"✅ HTTP status code: {response.status_code}")

# Print first 500 characters of the page for quick check
print("Page preview:")
print(response.text[:500])

soup = BeautifulSoup(response.text, 'html.parser')
print("✅ Parsed HTML with BeautifulSoup")

    
# Get all <a> tags
links = soup.find_all('a')

# Filter to get only .htm links (assuming school result pages end with .htm)
school_links = [link.get('href') for link in links if link.get('href') and link.get('href').endswith('.htm')]

print(f"✅ Found {len(school_links)} links ending with '.htm'")
print("Sample links:", school_links[:5])

base_url = "https://www.necta.go.tz/results/2023/csee/"

try:
    tables = pd.read_html(res.text)
    print(f"✅ Found {len(tables)} table(s) in school page")
    print("First few rows of the first table:")
    print(tables[0].head())
except Exception as e:
    print("❌ Failed to read tables on this page:", e)


















