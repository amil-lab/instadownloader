# instadownloader
Instagram Video  Downloader+ Telegram Bot

Python Requirements: Python 3.7 or higher

You can create virtual enviroment for this code to run or just do it locally:
   # Create a virtual environment (recommended)
   python -m venv venv

   # Activate virtual environment
   
   On Windows:
   
   venv\Scripts\activate
   
   On macOS/Linux:
   
   source venv/bin/activate

   # Install required packages

   pip install python-telegram-bot
   
   pip install instaloader

   pip install python-dotenv

   Or just run this code after getting the Requirements.txt

   pip install -r requirements.txt


# Telegram Future
For the telegram future you have to go to the @BotFather,create a new bot then take this api paste into the token section.

Keep the Token secure we have to create enviorement.Create a '.env' file and place the token that you got from the @BotFather.Add .env to your .gitignore file to prevent it from being committed.

Both of those code should be on the same directory(If you wanna make it globally accessible by telegram bot )

Make sure you have a directory structure where the bot can create a 'downloads' folder

You have to go to the @BotFather,create a new bot then take this api paste into the token section



#   Additional Notes:
The bot needs permissions to create and delete directories/files in its working directory
Make sure your system has proper media codec support if you plan to handle video files
The Instagram API access is done through instaloader, which doesn't require authentication for public posts


# To run the bot:
python telegram_bot.py







# DISCLAIMER: 
 This code is provided "as is" without warranty of any kind, express or implied. 
 
 The author(s) are not responsible for any damages, losses, or consequences that may arise from the use or misuse of this code.
 
 Use at your own risk.
