# Aiogram-telegram-bot
---

## How to 

1) Clone repo
```bash
git clone https://github.com/Innsmouth-trip/aiogram-telegram-bot.git
cd aiogram-telegram-bot
```

2) Bot settings
```bash
chmod +x bot.sh
./bot.sh --setup
```

### Welcome text

Add your text to `src/welcome_text.txt

**WARNING**

structure `<a href="tg://user?id={}">{}</a>` is required.

### Rules text

Add your text to  `src/rules_text.txt`

###  Run 
```bash
./bot.sh --start
```

