import uuid
from urllib.parse import urlparse

def generate_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname
    unique_name = f"{domain}_{uuid.uuid1()}.png"
    return unique_name