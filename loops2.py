target = "example.com"
paths = ["admin", "login", "dashboard", "uploads" ]

for path in paths:
    print(f"http://{target}/{path}")

# paths = [...] a list of common directories
# for path in paths: - loops through the list
# print(f"http://{target}/{path}") - prints the full URL
# target = "example.com" - the target domain
