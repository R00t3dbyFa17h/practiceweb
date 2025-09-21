def enumerate_paths(domain, paths):
    for path in paths:
        url = f"http://{domain}/{path}"
        print(f"Testing: {url}")

target = input("Enter target domain:")
common_paths = ["admin", "login", "uploads", "config", "backup"]

enumerate_paths(target, common_paths)