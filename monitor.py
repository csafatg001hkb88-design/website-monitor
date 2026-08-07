import requests
import json
import os

BOT_TOKEN = "8831943364:AAHKaZEYWo0RKi3YJtNW_rfW9uo0vC1Em8E"
CHAT_ID = "7844730036"

WEBSITES = [
    {
        "nama": "afatogel",
        "url": "https://domain-test-123456789.com"
    },
    {
        "nama": "afatogelvvip",
        "url": "https://afatogelvvip.com"
    }
]

STATUS_FILE = "status.json"

if os.path.exists(STATUS_FILE):
    with open(STATUS_FILE, "r") as f:
        status_lama = json.load(f)
else:
    status_lama = {}

status_baru = {}

for site in WEBSITES:
    try:
        response = requests.get(
            site["url"],
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code == 200:

            print(f'{site["nama"]} ONLINE')
            status_baru[site["nama"]] = "ONLINE"

            if status_lama.get(site["nama"]) == "DOWN":

                pesan = f"""🟢 DOMAIN ONLINE KEMBALI

Website : {site["nama"]}
Domain  : {site["url"]}

✅ Website sudah dapat diakses kembali.
"""

                r = requests.get(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    params={
                        "chat_id": CHAT_ID,
                        "text": pesan
                    }
                )

                print(r.text)

        else:

            print(f'{site["nama"]} DOWN')
            status_baru[site["nama"]] = "DOWN"

            pesan = f"""🔴 DOMAIN DOWN

Website : {site["nama"]}
Domain  : {site["url"]}

Status : {response.status_code}
"""

            r = requests.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                params={
                    "chat_id": CHAT_ID,
                    "text": pesan
                }
            )

            print(r.text)

    except Exception as e:

        print(e)
        status_baru[site["nama"]] = "DOWN"

        pesan = f"""🔴 DOMAIN DOWN

Website : {site["nama"]}
Domain  : {site["url"]}

Error :
{e}
"""

        r = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": CHAT_ID,
                "text": pesan
            }
        )

        print(r.text)

with open(STATUS_FILE, "w") as f:
    json.dump(status_baru, f)
