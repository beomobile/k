import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the OpenAI API
openai.api_key = "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"
model_engine = "davinci" # or any other model you prefer

# Set up the Telegram bot
bot = telegram.Bot(token="5855839274:AAHZfIvPkGVkiX7OR8Vd3tosjhTKE2CpGoM")

# Define a function to handle incoming messages
def handle_message(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Set up the Telegram updater and handlers
updater = Updater(token="5855839274:AAHZfIvPkGVkiX7OR8Vd3tosjhTKE2CpGoM", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()