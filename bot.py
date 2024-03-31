import telebot
from telebot import types

# -----------------#
Token = "7053339447:AAHzZVEAqEEMokhZTPdJ947fC38MT9nPwFQ"
bot = telebot.TeleBot(Token)
# ------------------#


def getfile(filename):
    myfile = open(filename, "r+")
    return myfile.read()
    myfile.close()
# -------------------#


def putfile(filename, filedate):
    myfile = open(filename, "w+")
    return myfile.write(filedate)
    myfile.close()
# ------------------#


@bot.message_handler(commands=['salam'])
def startcmd(user):
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.lastname
    dokmeha = types.ReplyKeyboardMarkup(row_width=1)
    dokme1 = types.KeyboardButton("Take a Screen Shot")
    dokme2 = types.KeyboardButton("Power Options")
    dokme3 = types.KeyboardButton("Play Sound")
    dokme4 = types.KeyboardButton("File Managere")
    dokmeha.add(dokme1 , dokme2 , dokme3 , dokme4)

    bot.send_message(userchatid, "hello to OS Remoter of ALI ESTAJI bot" , reply_markup=dokmeha)
    print("User :" + str(userchatid) + "started the bot")
# -------------------#


@bot.message_handler(content_types=['text'])
def BotMain(user):
    admin = "IMALIEST"
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.lastname
    # -----------------#

    if (userusername == admin):
        if (usertext == "/salam"):
            startcmd(user)
    else:
        pass

    # -------------------#
bot.polling(True)
