from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8532082529:AAHCiDhoHsPzp43m5tX4fPsZFFwRqeRTTAw"
WEBAPP_URL = "https://clope36.42web.io/?i=1#"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text="Ouvrir la Mini-App 🚀", url=WEBAPP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Bienvenue dans Clope36 Bot !\nAppuie sur le bouton ci-dessous 👇",
        reply_markup=reply_markup
    )

# Application compatible Python 3.13
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Lance le bot
app.run_polling()
