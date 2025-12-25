import os, time, re
from typing import List
id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID = 25976192  # Your API ID here
    API_HASH = "8ba23141980539b4896e5adbc4ffd2e2"  # Your API Hash here
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # Your Bot Token here
   
    # database config
    DATABASE_NAME = "2gbfile_renam_bot"
    DATABASE_URL = os.environ.get("DATABASE_URL","")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = ["https://graph.org/file/0b0b88c82bf5bc8b1fe46-4f49971fcaee348ff2.jpg"]  # List of start pictures
    ADMIN = 6621572366  # Your Admin ID

    # channels
    IS_FSUB = False  # Set True to enable Force Subscribe
    AUTH_CHANNELS = []  # Add channel IDs as list like [-100123456789, -100987654321]
    LOG_CHANNEL = -1003350129581  # Your Log Channel ID
    BIN_CHANNEL = None  # Your Bin Channel ID (or None if not using)

    # web response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))  # Set True to enable Webhook


class Txt(object):
    # part of text configuration
    START_TXT = """{},

🔹 *Welcome to Rename Bot* 🔹

Using this bot you can rename and change thumbnail of your files. You can also convert video to file and file to video.

📌 **Note:** Adult Content is STRICTLY prohibited. Ban will be permanent.

━━━━━━━━━━━━━━━━━━━━━━━━
📁 **Features:**
✓ Rename files with custom names
✓ Set custom thumbnails
✓ Convert video to file & file to video
✓ Fast & efficient
✓ User-friendly interface
━━━━━━━━━━━━━━━━━━━━━━━━

🚀 *Start by sending me any file!*"""

    ABOUT_TXT = """🤖 **Bot Information**

┌───────────────┐
│ ✨ **Bot Name** │ : [Rename Bot](https://t.me/rs_woner)
├───────────────┤
│ 📚 **Library**  │ : [Pyrogram](https://docs.pyrogram.org/)
├───────────────┤
│ 🗄️ **Database** │ : [MongoDB](https://www.mongodb.com/)
├───────────────┤
│ 💻 **Language** │ : [Python 3](https://www.python.org/)
├───────────────┤
│ 🌐 **Server**   │ : [Koyeb](https://www.koyeb.com/)
├───────────────┤
│ 👨‍💻 **Creator**  │ : [RS](https://telegram.me/rs_woner)
└───────────────┘

💫 *A powerful file management bot for Telegram*"""

    HELP_TXT = """📚 **Help Guide**

**Rename Bot** is a handy tool that helps you rename and manage your files effortlessly.

━━━━━━━━━━━━━━━━━━━━━━━━

🔧 **Available Commands:**

┌─────────────────────┐
│ 📋 /start - Start bot
│ 📄 /help - This menu
│ ℹ️ /about - Bot info
│ 🖼️ /thumbnail - Thumbnail settings
│ 📝 /caption - Caption settings
│ 🔤 /prefix - Prefix settings
│ 🔚 /suffix - Suffix settings
│ 📊 /metadata - Metadata settings
│ 💰 /donate - Support bot
└─────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━
💡 **How to use:**
1. Send any file
2. Enter new name
3. Get renamed file!

📬 *Need more help? Contact @RS_WONER*"""

    THUMBNAIL_TXT = """🖼️ **Thumbnail Settings**

**To set custom thumbnail:**

✅ **Set Thumbnail:**
Send any photo to automatically set it as thumbnail.

✅ **Delete Thumbnail:**
Use `/delthumb` to delete your thumbnail.

✅ **View Thumbnail:**
Use `/viewthumb` to view your current thumbnail.

━━━━━━━━━━━━━━━━━━━━━━━━
📌 **Note:** If no thumbnail saved in bot, it will use thumbnail of the original file to set in renamed file."""

    CAPTION_TXT = """📝 **Caption Settings**

**To set custom caption and media type:**

📌 **Available Variables:**
• `{filesize}` - File size
• `{duration}` - Duration (for media)
• `{filename}` - File name

━━━━━━━━━━━━━━━━━━━━━━━━

🔧 **Commands:**
• `/set_caption` - Set custom caption
• `/see_caption` - View custom caption
• `/del_caption` - Delete custom caption

━━━━━━━━━━━━━━━━━━━━━━━━
💡 **Example:**
`/set_caption File Name: {filename}
Size: {filesize}
Duration: {duration}`"""

    PREFIX = """🔤 **Prefix Settings**

**To set custom prefix:**

🔧 **Commands:**
• `/set_prefix` - Set custom prefix
• `/see_prefix` - View custom prefix
• `/del_prefix` - Delete custom prefix

━━━━━━━━━━━━━━━━━━━━━━━━
💡 **Example:**
`/set_prefix @RS_WONER_`"""

    SUFFIX = """🔚 **Suffix Settings**

**To set custom suffix:**

🔧 **Commands:**
• `/set_suffix` - Set custom suffix
• `/see_suffix` - View custom suffix
• `/del_suffix` - Delete custom suffix

━━━━━━━━━━━━━━━━━━━━━━━━
💡 **Example:**
`/set_suffix _by_RS`"""

    PROGRESS_BAR = """━━━━━━━━━━━━━━━━━━━━━━━━
📊 **Progress:** {0}%
📦 **Size:** {1} | {2}
⚡ **Speed:** {3}/s
⏳ **ETA:** {4}
━━━━━━━━━━━━━━━━━━━━━━━━"""

    DONATE_TXT = """❤️ **Support & Donation**

Thank you for showing interest in supporting our bot development!

━━━━━━━━━━━━━━━━━━━━━━━━

💝 **Why donate?**
Donations help in:
• Server maintenance
• Feature development
• Bug fixes
• Continuous improvements

━━━━━━━━━━━━━━━━━━━━━━━━

💰 **Payment Methods:**
• **bKash:** `+8801957340327`
• **Nagad:** `+8801957340327`
• **Rocket:** `+8801957340327`

━━━━━━━━━━━━━━━━━━━━━━━━
🤝 *Your support keeps this bot running!*"""

    SEND_METADATA = """📋 **Metadata Settings**

**To set custom metadata:**

🔧 **Command:**
• `/metadata` - Set custom metadata

━━━━━━━━━━━━━━━━━━━━━━━━
💡 **How to use:**
1. Send `/metadata`
2. Send any text
3. It will be saved as your metadata

**Example:**
`@RS_WONER | Telegram Rename Bot`"""
