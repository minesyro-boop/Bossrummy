import os
import re
from telethon import TelegramClient, events

# 🔑 ENV VARIABLES
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

source_channel_1 = int(os.getenv("SOURCE_CHANNEL_1"))
source_channel_2 = int(os.getenv("SOURCE_CHANNEL_2"))

target_channel = int(os.getenv("TARGET_CHANNEL"))

# 🚀 Client
client = TelegramClient("session", api_id, api_hash)

# 🧠 Duplicate रोकने के लिए
last_code = None

# 🎯 Event listener
@client.on(events.NewMessage(chats=[source_channel_1, source_channel_2]))
async def handler(event):
    global last_code

    # ❌ अगर message में text नहीं है तो skip
    if not event.raw_text:
        return

    text = event.raw_text

    # 🔍 Code detect
    match = re.search(r'500-CashCode-\d+', text)

    if match:
        code = match.group()

        # 🚫 duplicate रोकना
        if code == last_code:
            return

        last_code = code

        # ⚡ 6 rows monospace format
        final_msg = "\n".join([f"`{code}`" for _ in range(6)])

        # 🚀 सिर्फ text भेजेगा (photo नहीं)
        await client.send_message(target_channel, final_msg)

        print(f"✅ Sent: {code}")

# ▶️ Run
client.start()
print("🚀 Bot Running...")
client.run_until_disconnected()
