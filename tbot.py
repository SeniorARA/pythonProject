from typing import Final
from telegram import Update
from telegram.ext import Application, filters, CommandHandler, MessageHandler, ContextTypes

#Bot information
token: Final = '5195207128:AAFcw60NxAeR5sn-ZkzxpxgRJVSmXR4KWuc'
bot_username: Final = 'hello_miderBot'










#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello , Im a Master Robot! I am your assistant')

async def template_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    has_context: list = []

    if len(context.args) > 0:
        has_context = context.args

        link: str = has_context[0]
        name: str = has_context[1]
        criticize: str = has_context[2]
        time: str = has_context[3]

        text_template: str = '''Ваша заявка зарегистрирована. \nСсылка: {} \nИсполнитель: {} \nКритичность: {} \nВремя решения: {}'''

        edited_text_template: str = text_template.format(link, name, criticize, time)

        await update.message.reply_text(edited_text_template)
    else:
        await update.message.reply_text('Please enter a incident type : /template [Link] [Name] [Criticality] [Time]')











#Handle responses (to Messages)
def handle_response(text: str) -> str:
    #Message(Update) text to lowercase for correct response
    processed: str = text.lower()

    #Handle Responses
    response: str = 'I do not understand what you wrote'
    if 'hello' in processed:
        response = 'Hey there'
        return response
    if 'tell' in processed:
        response = 'I am a Master Robot. I progress everyday and one day i will become an AI!'
        return response
    if '1 1 1 1' in processed:
        response = template_response(processed)
        return response
    return response

def template_response(text: str) -> str:
    processed: str = text.lower()

    processed_list: list = processed.split()

    text_template: str = '''Ваша заявка зарегистрирована. \nСсылка: {} \nИсполнитель: {} \nКритичность: {} \nВремя решения: {}'''

    edited_text_template: str = text_template.format(processed_list[0], processed_list[1], processed_list[2], processed_list[3])

    return edited_text_template










#Handle Messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #Message objects
    message_type: str = update.message.chat.type
    message_text: str = update.message.text
    message_user_id: str = update.message.chat.id
    message_user_name: str = update.message.chat.first_name

    print(f'User ({message_user_id}) - ({message_user_name}) in {message_type}: {message_text}')

    if message_type =='group':
        if bot_username in message_text:
            new_text: str = message_text.replace(bot_username, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(message_text)


    print('Bot: ', response)
    await update.message.reply_text(response)









# Error Handler
def error_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {Update} caused Error : {context.error}')










if __name__ == '__main__':
    #Application
    print('Application is started')
    app = Application.builder().token(token=token).build()

    #add CommandHandlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('t', template_command))

    #add MessageHandlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #add ErrorHandler
    app.add_error_handler(error_handle)

    #Polling...
    print('Polling started')
    app.run_polling(3)


