def build_url(path, domain="https://test.myshop.cz"):
    if path == "":
        return "500 error"
    return f"{domain}/{path}"

print(build_url("login"))
print(build_url("catalog"))
print(build_url("cart"))
print(build_url("checkout", domain="https://myshop.cz"))
print(build_url(""))