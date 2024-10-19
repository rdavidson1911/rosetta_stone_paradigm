import requests
import os

def download_sample_pcap(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename} successfully.")
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")

# Example usage
url = "https://wiki.wireshark.org/SampleCaptures?action=AttachFile&do=get&target=http.cap"
filename = "sample_data/http_sample.pcapng"

download_sample_pcap(url, filename)
