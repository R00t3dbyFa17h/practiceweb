target = "www.example.com"
print(f"target domain: {target}")
print(f"http://{target}/robots.txt")
print(f"https://{target}/.git/")

# target = "www.example.com" - the target domain
# print(f"...") - prints the full URL
# f ".." an f-string allows you to drop varibles into strings
# http://{target}/robots.txt - builds a URL dynamically. if you change target, all URLS update automatically
