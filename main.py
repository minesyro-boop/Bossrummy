import os
import re
from telethon import TelegramClient, events

# 🔑 API DETAILS
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# 📢 Separate source channels
source_channel_1 = int(os.getenv("SOURCE_CHANNEL_1"))
source_channel_2 = int(os.getenv("SOURCE_CHANNEL_2"))

# 🎯 Target channel
target_channel = int(os.getenv("TARGET_CHANNEL"))

# 🚀 Client
client = TelegramClient("session", api_id, api_hash)

# 🎯 Event listener (2 channels)
@client.on(events.NewMessage(chats=[source_channel_1, source_channel_2]))
async def handler(event):
    text = event.raw_text

    # 🔍 Code detect
    match = re.search(r'500-CashCode-\d+', text)

    if match:
        code = match.group()

        # ⚡ 6 rows monospace format
        final_msg = "\n".join([f"`{code}`" for _ in range(6)])

        # 🚀 instant send
        await client.send_message(target_channel, final_msg)

        print(f"✅ Sent: {code}")

# ▶️ Run
client.start()
print("🚀 Bot Running...")
client.run_until_disconnected()