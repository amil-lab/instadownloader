from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from instadownloader import download_instagram_post
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("Bot token not found in environment variables!")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Instagram Media Downloader Bot!\n"
        "Send me an Instagram post URL, and I'll download the media for you."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 How to use:\n"
        "1. Copy an Instagram post URL\n"
        "2. Send it to me\n"
        "3. Wait for the media to be downloaded\n\n"
        "Example URL format:\n"
        "https://www.instagram.com/p/xyz123/"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    # Check if the message contains "instagram.com"
    if "instagram.com" in text.lower():
        await update.message.reply_text("📥 Processing your request...")
        
        try:
            # Create a unique download directory for each user
            user_id = update.message.from_user.id
            output_path = f"downloads/{user_id}"
            
            # Download the Instagram post
            download_instagram_post(text, output_path)
            
            # Find the downloaded files
            post_folder = os.path.join(output_path, os.listdir(output_path)[-1])
            media_files = [f for f in os.listdir(post_folder) if not f.endswith('.txt')]
            
            # Send each media file
            for media_file in media_files:
                file_path = os.path.join(post_folder, media_file)
                if media_file.endswith(('.jpg', '.jpeg', '.png')):
                    await update.message.reply_photo(photo=open(file_path, 'rb'))
                elif media_file.endswith('.mp4'):
                    await update.message.reply_video(video=open(file_path, 'rb'))
            
            # Clean up downloaded files
            for file in media_files:
                os.remove(os.path.join(post_folder, file))
            os.rmdir(post_folder)
            os.rmdir(output_path)
            
        except Exception as e:
            await update.message.reply_text(f"❌ Error: {str(e)}")
    else:
        await update.message.reply_text("Please send a valid Instagram post URL.")

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    await update.message.reply_text("❌ Sorry, something went wrong.")

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3) 
