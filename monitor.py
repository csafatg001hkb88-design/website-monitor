import requests
from datetime import datetime

BOT_TOKEN = "8831943364:AAHKaZEYWo0RKi3YJtNW_rfW9uo0vC1Em8E"
CHAT_ID = "7844730036"

WEBSITES = [
    {
        "nama": "afatogel",
        "url": "https://afatogel.com"
    },
    {
        "nama": "afatogelvvip",
        "url": "https://afatogelvvip.com"
    }
]

for site in WEBSITES:

    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    try:
        response = requests.get(
            site["url"],
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code == 200:

            print(f'{site["nama"]} ONLINE')

            pesan = f"""🟢 DOMAIN ONLINE

Website : {site["nama"]}
Domain  : {site["url"]}

Status  : ONLINE

🕒 Waktu : {waktu}
"""

        else:

            print(f'{site["nama"]} DOWN')

            pesan = f"""🔴 DOMAIN DOWN

Website : {site["nama"]}
Domain  : {site["url"]}

HTTP Status : {response.status_code}

🕒 Waktu : {waktu}
"""

        r = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": CHAT_ID,
                "text": pesan
            },
            timeout=10
        )

        print(r.text)

    except Exception as e:

        print(f'{site["nama"]} DOWN')
        print(e)

        pesan = f"""🔴 DOMAIN DOWN

Website : {site["nama"]}
Domain  : {site["url"]}

Error :
{str(e)}

🕒 Waktu : {waktu}
"""

        r = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": CHAT_ID,
                "text": pesan
            },
            timeout=10
        )

        print(r.text)
