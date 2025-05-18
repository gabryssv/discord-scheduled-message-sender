import json
import asyncio
import aiohttp
import re

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']
MESSAGES = config['messages']

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

def parse_interval(interval):
    match = re.match(r"(\d+)([smhd])", interval)
    if not match:
        raise ValueError(f"Invalid interval format: {interval}")
    value, unit = int(match.group(1)), match.group(2)
    if unit == "s":
        return value
    elif unit == "m":
        return value * 60
    elif unit == "h":
        return value * 3600
    elif unit == "d":
        return value * 86400
    else:
        raise ValueError(f"Unknown time unit: {unit}")

async def send_and_delete_message(channel_id, message, delete):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        try:
            async with session.post(url, json={"content": message}) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    message_id = data['id']
                    print(f"[{channel_id}] Wiadomość wysłana (ID: {message_id})")

                    if delete:
                        await asyncio.sleep(2)
                        delete_url = f"{url}/{message_id}"
                        async with session.delete(delete_url) as delete_response:
                            if delete_response.status == 204:
                                print(f"[{channel_id}] Wiadomość usunięta.")
                            else:
                                print(f"[{channel_id}] Błąd przy usuwaniu wiadomości: {delete_response.status}")
                else:
                    print(f"[{channel_id}] Błąd przy wysyłaniu wiadomości: {response.status}")
        except Exception as e:
            print(f"[{channel_id}] Wyjątek: {e}")

async def message_loop(channel_id, message, interval, delete):
    while True:
        await send_and_delete_message(channel_id, message, delete)
        await asyncio.sleep(interval)

async def main():
    tasks = [
        message_loop(
            entry['channel_id'],
            entry['message'],
            parse_interval(entry['interval']),
            entry.get('delete', False)
        )
        for entry in MESSAGES
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())