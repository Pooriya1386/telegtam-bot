import os
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")  # توکن رو از محیط می‌گیره

keyboard = [["📦 سفارش ممبر"], ["💳 پرداخت و ارسال رسید"], ["📞 پشتیبانی"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! خوش اومدی به فروشگاه ممبر فیک 👋", reply_markup=markup)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📦 سفارش ممبر":
        await update.message.reply_text("💡 پلن‌ها:\n100 ممبر = 15 هزار تومان\n500 ممبر = 60 هزار تومان\n\nبرای پرداخت، دکمه «💳 پرداخت و ارسال رسید» رو بزن.")
    elif text == "💳 پرداخت و ارسال رسید":
        await update.message.reply_text("💳 لطفاً مبلغ رو کارت به کارت کن به:\n`6037-9911-xxxx-xxxx`\nسپس رسید رو همینجا ارسال کن.")
    elif text == "📞 پشتیبانی":
        await update.message.reply_text("📞 برای پشتیبانی با @YourUsername در ارتباط باش.")
    else:
        await update.message.reply_text("✅ رسید دریافت شد. سفارش شما در حال ثبت است.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message_handler))
app.run_polling()
