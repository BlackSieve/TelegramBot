import telebot
from secret import TOKEN, money
from extensions import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start','help'])
def start(massage: telebot.types.Message):
    text = ('Чтобы начать работать введите комманду боту в следующем формате:'
            '\n<имя валюты> <в какую валюту перевести> <количество переводимой валюты> '
            '\n Чтобы увидеть список доступных валют напишите команду: /values  ')
    bot.reply_to(massage,text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = '!БУДЬ ВНИМАТЕЛЬНЫМ: вводи валюту также как указано ниже!\nДоступная валюта:'
    for key in money.keys():
        text = '\n'.join((text,key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(massage: telebot.types.Message):
    try:
        values = massage.text.split(' ')
        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, amount, base)

    except ConvertionException as e:
        bot.reply_to(massage, f'Ошибка пользователя,обратитесь к команде /help или /values.\n{e}')
    except Exception as e:
        bot.reply_to(massage, f'Не удалось обработать команду.\n{e}')

    else:
        t = float(round(total_base) * int(amount))
        text = (f'Цена {amount} {quote} в {base} - {t}')
        bot.send_message(massage.chat.id, text)




bot.polling(none_stop=True)
