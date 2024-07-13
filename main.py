import os, telebot, xml, requests
from xml.dom.minidom import parseString


BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    message_to_user = """
    /start - Start bot
    /projects - Get all current projects
    """
    bot.reply_to(message, message_to_user)
    
@bot.message_handler(commands=['projects'])
def send_projects(message):
    website = "https://artchsh.kz/"
    response = requests.get(website)
    if response.status_code == 200:
        contents = response.content.decode("utf-8")
        document = parseString(contents)
        all_li = document.getElementsByTagName("li")
        all_projects_li = all_li[4:-1]
        new_msg = "Projects: \n"
        for project_li in all_projects_li:
            new_msg += f"{project_li.getAttribute('status')} - {project_li.getAttribute('name')}\n"
        new_msg += """---
        ✅ - Source code of project is available, and it works/worked
        ⚠️ - Maybe broken
        ⏳ - Currently working on it
        ❌ - I decided to not do this project
        🗓 - Planned project
        """
        bot.reply_to(message, new_msg)
    bot.reply_to(message, "Website is not working right now. Try later.")
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()