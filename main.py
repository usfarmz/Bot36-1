from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ton token Telegram
TOKEN = "8532082529:AAHCiDhoHsPzp43m5tX4fPsZFFwRqeRTTAw"

# Ton URL de mini-app
WEBAPP_URL = "https://clope36.42web.io/?i=1#"

# Fonction de démarrage
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text="Ouvrir la Mini-App 🚀", url=WEBAPP_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Bienvenue dans Clope36 Bot !\nAppuie sur le bouton ci-dessous 👇",
        reply_markup=reply_markup
    )

# Création de l'application
app = ApplicationBuilder().token(TOKEN).build()

# Ajout du handler pour /start
app.add_handler(CommandHandler("start", start))

# Démarrage du bot
app.run_polling()
