import requests

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

        else:
            print(f'{site["nama"]} DOWN')

            pesan = f"""🔴 DOMAIN DOWN

Website : {site["nama"]}
Domain  : {site["url"]}
Status  : {response.status_code}
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

    print(f"{nama} DOWN")
    status_baru[nama] = "DOWN"

    pesan = (
        "🔴 DOMAIN DOWN\n\n"
        f"🌐 Website : {nama}\n"
        f"🔗 Domain : {url}\n\n"
        f"❌ HTTP Status : {response.status_code}"
    )

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": pesan
        }
    )

        print(r.text)
