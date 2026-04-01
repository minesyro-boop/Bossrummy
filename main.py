import os
import re
from telethon import TelegramClient, events

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

source_channel_1 = int(os.getenv("SOURCE_CHANNEL_1"))
source_channel_2 = int(os.getenv("SOURCE_CHANNEL_2"))
target_channel = int(os.getenv("TARGET_CHANNEL"))

# ⚡ connection optimize
client = TelegramClient(
    "session",
    api_id,
    api_hash,
    connection_retries=None
)

pattern = re.compile(r'500-CashCode-\d+')

@client.on(events.NewMessage(chats=[source_channel_1, source_channel_2]))
async def handler(event):

    text = event.raw_text
    if not text:
        return

    match = pattern.search(text)
    if not match:
        return

    code = match.group()

    # ⚡ fastest string build
    msg = f"`{code}`\n" * 6

    await client.send_message(target_channel, msg[:-1])  # last newline हटाया

client.start()
print("⚡ ULTRA LOW LATENCY BOT RUNNING...")
client.run_until_disconnected()
