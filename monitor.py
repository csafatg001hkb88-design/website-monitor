import requests

BOT_TOKEN = "8831943364:AAHKaZEYWo0RKi3YJtNW_rfW9uo0vC1Em8E";
CHAT_ID = "7844730036";

websites = [
    {
        "nama": "afatogel",
        "url": "https://afatogel.com"
    },
    {
        "nama": "afatogelvvip",
        "url": "https://afatogelvvip.com"
    }
]

for site in websites:
    try:
        response = requests.get(site["url"], timeout=10)

        if response.status_code == 200:
            print(f'{site["nama"]} ONLINE')
        else:
            print(f'{site["nama"]} DOWN')

            pesan = (
                f"🔴 Domain DOWN\n\n"
                f"Website: {site['nama']}\n"
                f"Domain: {site['url']}"
            )

            requests.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                params={
                    "chat_id": CHAT_ID,
                    "text": pesan
                }
            )

    except Exception:
        print(f'{site["nama"]} DOWN')

        pesan = (
            f"🔴 Domain DOWN\n\n"
            f"Website: {site['nama']}\n"
            f"Domain: {site['url']}"
        )

        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={
                "chat_id": CHAT_ID,
                "text": pesan
            }
        )
