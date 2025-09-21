# def build_urls(domain, paths): - defines a function, 
# a function is reusable
# for path in paths: - loops through the +
#  list passed into functions

def build_urls(domain, paths):
    for path in paths:
        print(f"https://{domain}/{path}")

target = "example.com"
wordlist = ["admin", "api", "config", "backup"]

build_urls(target, wordlist)

### print(f"https://{domain}/{path}") - prints the full URL ###
# build_urls(target, wordlist) - calls the function with the target and wordlist variables ###