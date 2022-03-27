from telegram.ext.updater import Updater  
from telegram.update import Update  
from telegram.ext.callbackcontext import CallbackContext  
from telegram.ext.commandhandler import CommandHandler  
from telegram.ext.messagehandler import MessageHandler  
from telegram.ext.filters import Filters  
   
the_updater = Updater("5260280548:AAHfjz_xgKKsQtiK1TAT95qaFE9xJw4jenQ",  
                use_context = True)  
  
def the_start(update: Update, context: CallbackContext):  
    update.message.reply_text(  
        "Hello sir, Welcome to the Carrerbudddy. Please write /help to see the commands available."  
        )  
  
def the_help(update: Update, context: CallbackContext):  
    update.message.reply_text(  
        """Available Commands :  
        /Carrercouncelling - To get the Carrer cOuncelling From Best Mentors  
        /Carrerchoices - To get the Carrer Choices  
        /gmail - To get gmail URL""")  
  
def gmailURL(update: Update, context: CallbackContext):  
    update.message.reply_text("carrerbuddy6@gmail.com")  
  
def Carrercouncelling(update: Update, context: CallbackContext):  
    update.message.reply_text(  
        "Link for the YouTube => https://www.youtube.com/"  
        )  
  
def Carrerchoices(update: Update, context: CallbackContext):  
    update.message.reply_text(  
        "1. Charted Accountant \n 2. Finance/Export Manager \n 3. Computer / Software Engineer \n 4. Doctor \n 5.  IAS/IPS \n 6. Lawyers/ Advocate \n 7. Lecturer \n 8. Businessmen \n 9. Sports Person \n 10.  Army"  
        )  
  
def jtpURL(update: Update, context: CallbackContext):  
    update.message.reply_text(  
        "URL to the official website => https://www.javatpoint.com/"  
        )  
  
def unknownCommmand(update: Update, context: CallbackContext):  
    update.message.reply_text(  
        "Sorry '%s' is an invalid command" % update.message.text  
        )  
  
def unknownText(update: Update, context: CallbackContext):  
    update.message.reply_text(  
        "Unfortunately, the system cannot recognize you, you said '%s'" % update.message.text  
        )  
  
# adding the handler to handle the messages and commands  
the_updater.dispatcher.add_handler(CommandHandler('start', the_start))  
the_updater.dispatcher.add_handler(CommandHandler('Carrercouncelling', Carrercouncelling))  
the_updater.dispatcher.add_handler(CommandHandler('help', the_help))  
the_updater.dispatcher.add_handler(CommandHandler('Carrerchoices', Carrerchoices))  
the_updater.dispatcher.add_handler(CommandHandler('gmail', gmailURL))  
the_updater.dispatcher.add_handler(CommandHandler('jtp', jtpURL))  
the_updater.dispatcher.add_handler(MessageHandler(Filters.text, unknownCommmand))  
 # Filtering out unknown commands  
the_updater.dispatcher.add_handler(MessageHandler(Filters.command, unknownCommmand))  
  
# Filtering out unknown messages  
the_updater.dispatcher.add_handler(MessageHandler(Filters.text, unknownText))  
  
# running the bot  
the_updater.start_polling()
