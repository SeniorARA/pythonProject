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
    args: list = context.args
    args_count: int = len(context.args)

    match args_count:
        case 0:
            await update.message.reply_text('This is a /t command. For correct operation give an arguments ["URL", "Name", "Importance", "Time"]')

        case 1:
            await update.message.reply_text('Need 3 more arguments!')

        case 2:
            await update.message.reply_text('Need 2 more arguments!')

        case 3:
            await update.message.reply_text('Need 1 more arguments!')

        case 4:
            response: str = template_response(args)
            await update.message.reply_text(response
                                            )
        case _:
            await update.message.reply_text('You inputted more than 4 arguments or Unexpected Error!')













#Handle responses (to Messages)
def handle_response(text: str) -> str:
    #Message(Update) text to lowercase for correct response
    processed: str = text.lower()

    #Template variables
    response: str = 'I do not understand what you wrote'
    helpText_list: Final = ['help', 'h', 'hp', 'he']

    #Handle Responses
    if processed in helpText_list:
        return 'This Bot works only with commands. Please input a command like [/t or /w] with arguments!'

    return response

def template_response(args: list) -> str:
    template_of_message: str = '''Ваша заявка зарегистрирована. \nСсылка: {} \nИсполнитель: {} \nКритичность: {} \nВремя решения: {}'''
    processed_list: list = []
    result: str = ''

    for i in args:
        i_lowercase: str = i.lower()
        processed_list.append(i_lowercase)

    url: str = processed_list[0]
    name: str = name_of_executor_handler(processed_list[1])
    importance: str = template_importance_handler(processed_list[2])
    time:str = processed_list[3]

    result = template_of_message.format(url, name, importance, time)

    return result


def name_of_executor_handler(name: str) -> str:
    result: str = ''
    dict_of_executors: dict = {
        'эш': 'Эдуард Шнабель',
        'рс': 'Руслан Сабитов',
        'вг': 'Владимир Гуржий',
        'аа': 'Алихан Аллаяров',
        'тм': 'Темирлан Мырзатаев'
    }
    for u, n in dict_of_executors.items():
        if u == name:
            result = n
            break
        else:
            result = 'None'

    return result

def template_importance_handler(importance: str) -> str:
    result: str = ''
    dict_of_importance: dict = {
        'б': 'Блокирующая',
        'к': 'Критическая',
        'з': 'Значительная',
        'н': 'Незначительная',
        'т': 'Тривиальная'
    }

    for u, n in dict_of_importance.items():
        if u == importance:
            result = n
            break
        else:
            result = 'None'

    return result



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










def main():
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

