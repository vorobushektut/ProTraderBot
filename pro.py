import asyncio
import pathlib
import json
from datetime import datetime
from pyrogram import Client
from aiogram import *
from aiogram.dispatcher.filters import Command
import time

bot_token = "6407840853:AAH99LMxEE-7R5OvKUjKYV7fMvwbSwjZ3Ls"
bot = Bot(token=bot_token)
api_id = 27847255
api_hash = "408e80faac6395c78a5051e4e40d956a"
SKABARYCH_ID = 1115914984
VIP_CHANNEL_ID = -1001977785674
dp = Dispatcher(bot=bot)
x = [1000, 2600, 4500]
flag_of_check = {}
flag_of_education = {}
members = []


async def n_sec_falser():
    time.sleep(1)
    return False


async def get_chat_members(chat_id):
    app = Client("ProTraderMakesMoneyBot", api_id=api_id, api_hash=api_hash, bot_token=bot_token, in_memory=True)
    chat_members = []
    await app.start()
    async for member in app.get_chat_members(chat_id):
        # print(member, end="\n\n------------\n\n")
        chat_members.append(member)
    await app.stop()
    return chat_members


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Обучение💼')
    btn2 = types.KeyboardButton('ProTrader VIP🎩')
    btn3 = types.KeyboardButton('Личный кабинет👨‍💻')
    markup.add(btn1, btn2, btn3)
    await message.answer("""👋 Привет, я ProTraderBot.
Расскажу о наших продуктах и помогу оформить подписку в VIP-клуб.
1. Чтобы пройти 3-х месячный курс обучения трейдингу нажмите “Обучение”
2. Чтобы попасть в закрытый vip клуб нажмите “ProTrader VIP” 
3. Чтобы посмотреть период своей подписки в vip клубе нажмите “Личный кабинет”""", reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def get_message(message: types.Message):
    global flag_of_check
    global flag_of_education
    if message.text == 'Обучение💼':
        new_markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(f'Начать обучение', callback_data='3')
        new_markup.add(btn1)
        await message.answer("""Описание курса:
<b> 📚Курс “Трейдинг: от новичка до профиссионала”</b>
-это комплексное обучение, охватывающее широкий спектор тем, связанных с успешной торговлей на финансовых рынках. 
    <b>24 обучающих видео </b> 
Ученик сам продумывает расписание в удобном формате - материалы для обучения доступны в формате видео <b>(высылаются Вам в личные сообщения через ProTraderBot 2 раза в неделю)</b>
    <b>Чему научитесь?</b>
1. Вы изучите основы технического анализа, научитесь работать с графиками и индикаторами, изучите и проверите на практике различные торговые стратегии.
2. Курс включает волновую теорию Эллиота, Вульфа и метод Вайкоффа
3. Вы научитесь основам риск-менеджмента, фундаментальному анализу, реверсной торговле.
4. Курс предлагает ресурсы для обучения торговле фьючерсами,облигациями, а также ребалансировки портфеля и работы с ордер-блоками.
5. Дополнительные материалы включают исторические кейсы, такие как Великая Депрессия, кризис доткомов и недвижимости 2008 года, Рецессия в связи с пандемией COVID-19

<b>Не упустите шанс стать профессионалом в мире трейдинга!

И помните: “Инвестиции в знания дают самые высокие дивиденды” Б.Франклин</b>

✅ <b>Вместе с обучающими материалами, Вам доступны:</b>
1) Еженедельные прямые эфиры с ответами на вопросы и консультацией по курсу
2) Постоянная поддержка наставника
3) Список профильной литературы
4) Доступ к обучающим материалам НАВСЕГДА
5) <b>БЕСПЛАТНЫЙ ДОСТУП В VIP КАНАЛ НА 3 МЕСЯЦА</b>""", parse_mode='html', reply_markup=new_markup)

    elif message.text == 'ProTrader VIP🎩':
        new_markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(f'1 месяц - {x[0]} рублей', callback_data='0')
        btn2 = types.InlineKeyboardButton(f'3 месяца - {x[1]} рублей (-13,3%)', callback_data='1')
        btn3 = types.InlineKeyboardButton(f'5 месяцев - {x[2]} рублей (-19%)', callback_data='2')
        new_markup.add(btn1, btn2, btn3)
        await message.answer("""<b>ProTrader VIP</b> - это клуб с эксклюзивными торговым идеям и стратегиями. Мы предлагаем уникальные прогнозы по российским акциям, аналитические материалы, а также регулярные обзоры финансовых инструментов (фьючерсы, валютные пары)

<b>! VIP-клуб ориентирован на трейдеров и инвесторов с депозитом (капиталом) от 20.000 рублей, которые хотят стабильно зарабатывать на фондовом рынке.</b>

✅ <b>В подписку входит:</b>
1. Углубленный анализ акций с конкретными целями и стоп-лоссами
2. Доступ к среднесрочному портфелю ProTrader VIP  (с указанием цены покупки, доли в общей структуре портфеля)
3. Уникальные спекулятивные торговые идеи каждую неделю
4. Анализ сырьевых товаров и валют
<b>Пожалуйста, выберите интересующий Вас тариф👇👇👇</b>""", parse_mode='html', reply_markup=new_markup)

    elif (message.from_user.id in flag_of_check and flag_of_check[message.from_user.id]) or (
            message.from_user.id in flag_of_education and flag_of_education[message.from_user.id]):
        flag_of_check[message.from_user.id] = False
        flag_of_education[message.from_user.id] = False
        await message.answer('Надо прислать скриншоты для подтверждения!')

    elif message.text == 'Личный кабинет👨‍💻':
        # members = await get_chat_members(VIP_CHANNEL_ID)
        user_id = message.from_user.id
        isInChannel = False
        joined_date = 0
        for member in members.values():
            if (member[0]['id'] == user_id):
                isInChannel = True
                joined_date = datetime.strptime(member[1]['joined_date'], "%Y-%m-%d %H:%M:%S")
        if isInChannel:
            days_in_channel = datetime.now().date() - joined_date.date()
            await message.answer(f'Вы находитесь в VIP клубе 👉  {days_in_channel.days} дн.', parse_mode='Markdown')
        else:
            await message.answer(
                'У вас нет активных подписок! \nВы можете приобрести подписку, нажав на кнопку ProTrader VIP🎩',
                parse_mode='Markdown')


@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    global flag_of_check
    global flag_of_education
    if message.from_user.id in flag_of_check and flag_of_check[message.from_user.id]:
        user_nickname = message.from_user.username
        await bot.send_message(SKABARYCH_ID, f"Пользователь: @{user_nickname}")
        await bot.send_photo(chat_id=SKABARYCH_ID, photo=message.photo[0].file_id)
        flag_of_check[message.from_user.id] = n_sec_falser()
        await message.answer("""Квитанция отправлена
После проверки платежа у Вас активируется подписка!
Ожидайте)""")
    elif flag_of_education[message.from_user.id]:
        user_nickname = message.from_user.username
        await bot.send_message(SKABARYCH_ID, f"Пользователь: @{user_nickname}")
        await bot.send_photo(chat_id=SKABARYCH_ID, photo=message.photo[0].file_id)
        flag_of_education[message.from_user.id] = n_sec_falser()
        await message.answer("""Квитанция отправлена
После проверки платежа Вы приступите к обучению!
Ожидайте)""")


@dp.callback_query_handler(lambda callback_query: True)
async def handle_callback_query(callback_query: types.CallbackQuery):
    global flag_of_check
    global flag_of_education
    if '0' <= callback_query.data <= '2':
        user_id = callback_query.from_user.id
        flag_of_check[user_id] = True
        await bot.send_message(callback_query.from_user.id, f"""Оплатить доступ Вы можете по следующим реквизитам:
Реквизиты

Номер счета получателя
40817 810 5 0110 2281398

БИК банка получателя
044525700

Фамилия, имя и отчество получателя
Скабаро Даниил Владимирович

Назначение платежа
Доступ в закрытый канал в телеграмм канал 

ПОСЛЕ СОВЕРШЕНИЯ ОПЛАТЫ, ОТПРАВЬТЕ БОТУ СКРИНШОТ. На скрине ОБЯЗАТЕЛЬНО должны указываться:
Сумма перевода
Дата и время
Счет поступления

К оплате: {x[int(callback_query.data)]} р.""")

    elif callback_query.data == '3':
        user_id = callback_query.from_user.id
        flag_of_education[user_id] = True
        await bot.send_message(callback_query.from_user.id, f"""Оплатить обучение Вы можете по следующим реквизитам:
Реквизиты
Номер счета получателя
40817 810 5 0110 2281398
БИК банка получателя
044525700
Фамилия, имя и отчество получателя
Скабаро Даниил Владимирович
Назначение платежа
Обучение трейдингу
ПОСЛЕ СОВЕРШЕНИЯ ОПЛАТЫ, ОТПРАВЬТЕ БОТУ СКРИНШОТ. На скрине ОБЯЗАТЕЛЬНО должны указываться:
Сумма перевода
Дата и время
Счет поступления

К оплате: 25 000 рублей""")


async def main():
    global members
    if (
            datetime.now().hour == 9 and datetime.now().minute == 0 or datetime.now().hour == 21 and datetime.now().minute == 0):
        members = await get_chat_members(VIP_CHANNEL_ID)
        members_dict = {}
        cwd = pathlib.Path(__file__).parent.resolve()
        for member in members:
            # print(member)
            members_dict[member.user.username] = []
            members_dict[member.user.username].append({"id": member.user.id})
            members_dict[member.user.username].append({"joined_date": str(member.joined_date)})
        with open(str(cwd) + '/members.json', 'w', encoding='utf-8') as file:
            print(members_dict)
            json.dump(members_dict, file)
    else:
        with open('members.json') as file:
            members = json.load(file)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
