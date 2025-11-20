from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut, envoie-moi ton mp3 pour cloner")

if __name__ == "__main__":
    app = ApplicationBuilder().token("8332101808:AAFtvQEsjgNAR2jxw1FKboMHupOTnmrYMIk").build()

    # On déclare la commande /start
    app.add_handler(CommandHandler("start", start))

    # Lancement du bot
    app.run_polling()
