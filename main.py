import sys
import re
import shutil
import requests
import ddddocr
from staticres import *

# Terminal colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
BROWN = "\033[38;5;130m"
CYAN = "\033[96m"
DARK_BLUE = "\033[34m"

BANNER = r"""  ____  __  __ ____
 / ___||  \/  / ___|
 \___ \| |\/| \___ \
  ___) | |  | |___) |
 |____/|_|  |_|____/"""

# Initialize OCR once globally
ocr = ddddocr.DdddOcr(beta=True, show_ad=False)

def verify_ocr(img_bytes):
    if not img_bytes or not (img_bytes.startswith(b'GIF') or img_bytes.startswith(b'\x89PNG') or img_bytes.startswith(b'\xff\xd8')):
        return None
    try:
        return ocr.classification(img_bytes)
    except Exception:
        return None

def send_sms(region_id, full_phone, sms="update+validation"):
    # Fresh session created per attempt to avoid session locking (-29 / -19)
    session = requests.Session()
    session.headers.update(header)

    try:
        verify = session.get(imgurl, timeout=10)
        if verify.status_code != 200:
            return None

        code = verify_ocr(verify.content)
        if not code:
            return None

        payload_str = f"id={region_id}&phone={full_phone}&content={sms}&vcode={code}"
        
        headers = header.copy()
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"

        res = session.post(shiyongurl, headers=headers, data=payload_str, timeout=10)
        return res.text
    except requests.RequestException:
        return None

def check(rst):
    if not rst or not isinstance(rst, str):
        return False
    
    match = re.search(r'status=(-?\d+)', rst)
    if match:
        try:
            status_val = int(match.group(1))
            if status_val > 80000:
                return True
        except ValueError:
            pass
    return False

def print_banner():
    terminal_width = shutil.get_terminal_size((80, 24)).columns

    for line in BANNER.splitlines():
        left_padding = max((terminal_width - len(line)) // 2, 0)
        colored_line = [RED, " " * left_padding]
        for character in line:
            if character in "()":
                colored_line.append(f"{ORANGE}{character}{RED}")
            else:
                colored_line.append(character)
        colored_line.append(RESET)
        print("".join(colored_line))

def format_response_line(rst):
    response = str(rst)
    match = re.search(r"status=-?\d+", response)
    if not match:
        return f"{YELLOW}Server response: {response}.{RESET}"

    status_text = match.group(0)
    before = response[:match.start()]
    after = response[match.end():]

    if status_text in {"status=-29", "status=-19"}:
        return (
            f"{YELLOW}Server response: {before}"
            f"{RED}{status_text}{YELLOW}{after}.{RESET}"
        )

    return (
        f"{YELLOW}Server response: {before}"
        f"{GREEN}{status_text}{YELLOW}{after}.{RESET}"
    )

def main():
    print_banner()
    print()

    if len(sys.argv) < 3:
        print("Usage: python main.py <region_code> <phone_number>")
        return

    region, phone = sys.argv[1], sys.argv[2]
    
    region_item = next((element for element in regionlist if element["CountryCode"] == region), None)
    if not region_item:
        print(f"[!] Invalid region code: '{region}'.")
        return

    region_id = region_item['Id']
    full_phone = f"{region}{phone}"
    terminal_width = shutil.get_terminal_size((80, 24)).columns
    target_line = f"Target: +{full_phone} (Region ID: {region_id})"
    print(f"{DARK_BLUE}{target_line.center(terminal_width)}{RESET}")
    print()
    print()

    max_retries = 5
    for attempt in range(1, max_retries + 1):
        print(f"{CYAN}Attempt {attempt}/{max_retries}...{RESET}")
        rst = send_sms(region_id, full_phone)
        
        if check(rst):
            print("OK! SMS Sent Successfully.")
            return
        else:
            print(format_response_line(rst))

if __name__ == '__main__':
    main()