from telegram.ext import ApplicationBuilder
application= ApplicationBuilder().token("8332101808:AAFtvQEsjgNAR2jxw1FKboMHupOTnmrYMIk").build()
async def start(update,context): await update.message.reply_text("Salut, envoie-moi ton mp3 pour cloner")
application.add_handler(CommandHandler(start,start))
application.run_polling()
