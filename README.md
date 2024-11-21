<div align="center">
  <img src="assets/logoo.png" alt="SQUID-SQUID!" width="200"/>
  
  # SQUID-SQUID!
  
  [![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
  [![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0+-orange.svg)](https://docs.pyrogram.org)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  A powerful and modular Telegram userbot focused on simplicity and extensibility
</div>

---

<div align="center">
  <img src="assets/prev.gif" alt="Demo" width="600"/>
</div>

## ✨ Features

- 🚀 **Fast & Lightweight** - Built for speed and efficiency
- 📦 **Modular System** - Easy to extend with custom modules
- ⚡ **Simple Installation** - Quick setup process
- 🛠 **User Friendly** - Intuitive commands and interface
- 🔒 **Secure** - Safe and reliable operation
- 🔄 **Regular Updates** - New official modules released frequently

## 🚀 Installation
```
git clone https://github.com/NotKiwy/Squid-Squid.git && cd Squid-Squid && pip install -r requirements.txt && python main.py
```

## 📚 Commands

| Command | Description |
|---------|-------------|
| `#mdl` | List installed modules |
| `#mdl/[name]` | Module information |
| `#mdl/[name]/run` | Start module |
| `#mdl/[name]/stop` | Stop module |
| `#mdl/[name]/delete` | Delete module |
| `#mdl/install` | Install module from file |
| `#mdl/import` | Import official module |

## 🛠 Development

Create your own module:
```
# [MODULE NAME]
# [VERSION]
# [DEVELOPER NICKNAME]
# [MODULE DESCRIPTION]
from pyrogram import Client, filters

@Client.on_message(filters.command("cmd", prefixes="#") & filters.me)
async def cmd(client, message):
    await message.edit("It works!")
```

<div align="center">
  
  ## 🦑 Created by SQUID-SQUID LLC
  
-> [Telegram](https://t.me/example) <- 
</div>
