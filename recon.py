import requests

def enumerate_paths(domain, paths):
    for path in paths:
        url = f"http://{domain}/{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Found: {url}")
            elif response.status_code in [301, 302]:
                print(f"[>] Redirect: {url} redirected to {response.headers.get('Location')}")
            elif response.status_code == 403:
                print(f"[!] Forbidden: {url} (access denied)")
            else:
                print(f"[-] {url} {response.status_code}")
        except requests.RequestException:
            print(f"[x] Error connecting to {url}")

target = input("Enter target domain:")
common_paths = ["admin", "login", "uploads", "config", "backup"]

enumerate_paths(target, common_paths)
# This script enumerates common paths on a target web server and handles various HTTP responses.
# It uses the requests library to make HTTP GET requests and prints the results accordingly.
# It prompts the user for a target domain and checks a predefined list of common paths.
# It handles status codes 200 (found), 301/302 (redirect), 403 (forbidden), and other responses.
# Make sure to install the requests library if you haven't already: pip install requests
# Note: Use this script responsibly and only on domains you own or have permission to test.
# Remember to respect the target's robots.txt and terms of service.
# Always obtain proper authorization before conducting any form of web reconnaissance or testing.
# This script is for educational purposes only.
# Do not use it for malicious activities.
# The author is not responsible for any misuse of this script.
                