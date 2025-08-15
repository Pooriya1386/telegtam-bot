from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive

TOKEN = "7760952360:AAES7XvPAD5SThbahJWmjCCsX3wYqJk0sbE"
ADMIN_ID = 7279296900

CARD_NUMBER = "6037-6975-9035-0176"
CARD_NAME = "وحید مرباغی"
BANK_NAME = "بانک صادرات"

keyboard = [["📦 سفارش ممبر"], ["💳 پرداخت و ارسال رسید"], ["📞 پشتیبانی"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام Pooriya! خوش اومدی به فروشگاه ممبر فیک 👋", reply_markup=markup)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📦 سفارش ممبر":
        await update.message.reply_text("💡 پلن‌ها:\n100 ممبر = 15 هزار تومان\n500 ممبر = 60 هزار تومان\n\nبرای پرداخت، دکمه «💳 پرداخت و ارسال رسید» رو بزن.")
    elif text == "💳 پرداخت و ارسال رسید":
        await update.message.reply_text(
            f"💳 لطفاً مبلغ رو کارت به کارت کن به:\n`{CARD_NUMBER}`\nبه نام {CARD_NAME} ({BANK_NAME})\n\nسپس رسید رو همینجا ارسال کن."
        )
    elif text == "📞 پشتیبانی":
        await update.message.reply_text("📞 برای پشتیبانی با @YourUsername در ارتباط باش.")
    else:
        await update.message.reply_text("✅ رسید دریافت شد. سفارش شما در حال بررسی است.")
        await context.bot.forward_message(chat_id=ADMIN_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

keep_alive()

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT | filters.PHOTO, message_handler))
app.run_polling()
