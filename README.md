# █ PBR NUKER █

A high-intensity Discord server nuker you will love it

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&logoColor=white)
---

## 🚀 Features
- **Parallel Execution**: Utilizes `asyncio.gather` for maximum speed during mass channel deletion and creation.
- **Aggressive Spammer**: Integrated background loop that posts content every 0.8 seconds across all new channels.
- **Dynamic Input**: Supports custom local image paths and custom nuke messages via terminal prompts.
- **Application ID Optional**: Flexible login logic to support various bot configurations.

---

## 🛠️ Installation & Setup

### Python Version
1. **Requirements**: Python 3.8 or higher.
2. **Install Dependencies**:
   ```bash
   pip install discord.py colorama
Run:
python main.py
Binary Version (If applicable)
Navigate to the directory containing the executable.

Run the binary via terminal/command prompt:
./pbr_nuker.exe

⌨️ Usage Instructions

Configuration: Follow the terminal prompts to enter:

Bot Token: Your unique Discord bot token.

Application ID: (Optional) press y to enter or n to skip.

Server ID: The ID of your target VM/Server.

Image Path: The full path to the .png or .jpg you wish to spam.

Message: Choose the default "PBR" message or type your own.

Execution: Once the bot status shows "Online," go to your Discord server and type:

Plaintext
.execute
⚙️ Technical Specifications
Channel Limit: Hardcoded to 50 channels (Adjustable in main.py).

Spam Interval: 0.8 seconds (Synchronized via tasks.loop).

Library: Powered by discord.py and colorama.

🛑 Disclaimer
This tool is provided for educational purposes only. The developers are not responsible for any misuse or damage caused by this software.
