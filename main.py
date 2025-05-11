
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Сәлем! Бұл GosZakup Komek бот.")

app = ApplicationBuilder().token("7593204522:AAG2VW4lLgeK3y_XKoPoaMJsaACVp30vj2w"
).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
