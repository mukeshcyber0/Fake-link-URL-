import re


def check_link(url):
    suspicious_keywords = ["login", "verify", "secure", "update"]

    print("\n🔍 Checking URL:", url)

    if not url.startswith("https://"):
        print("⚠️ Warning: Not a secure (HTTPS) link")

    if any(word in url.lower() for word in suspicious_keywords):
        print("⚠️ Suspicious keyword detected in URL")

    if re.search(r"\d{1,3}(\.\d{1,3}){3}", url):
        print("⚠️ IP address used instead of domain")

    if "@" in url:
        print("⚠️ '@' symbol found (possible redirection trick)")

    print("✅ Scan complete\n")


url = input("Enter a URL to analyze: ")
check_link(url)
