import re
from aiogram import Router, F, types
from services.ai_service import get_ai_answer
from services.google_service import gs_service
from keyboards.main_menu import main_kb

router = Router()
user_contexts = {}

@router.message(F.text == "/start")
async def start_cmd(message: types.Message):
    print("!!! ВЫЗВАН START !!!")
    
    welcome_text = (
        "💣 **Салон BEAUTYBOMB приветствует тебя!**\n\n"
        "Мы — пространство смелых образов и безупречного стиля. "
        "Наши мастера готовы воплотить в жизнь любую твою идею!\n\n"
        "**НАШИ УСЛУГИ:**\n"
        "🔸 **Тело:** Татуировка, пирсинг любой сложности и сплит языка.\n"
        "🔸 **Волосы:** Стрижки, сложное окрашивание, дреды, афро-косы.\n"
        "🔸 **Лицо:** Наращивание ресниц и ламинирование бровей.\n"
        "🔸 **Уход:** Маникюр, педикюр и бережная депиляция.\n\n"
        "Я — твой персональный ИИ-ассистент. Могу подробно рассказать о каждой процедуре, "
        "сориентировать по ценам или записать тебя прямо сейчас.\n\n"
        "**О чем хочешь узнать?**"
    )

    await message.answer(
        welcome_text,
        reply_markup=main_kb,
        parse_mode="Markdown"  # Добавили, чтобы жирный шрифт отображался красиво
    )

@router.message(F.text == "📍 Контакты")
async def contacts_btn(message: types.Message):
    print("!!! НАЖАТЫ КОНТАКТЫ !!!")
    
    contacts_text = (
        "📍 **Где нас найти?**\n"
        "Мы находимся в самом сердце столицы: \n"
        "г. Москва, ул. Арбат, д. 15.\n\n"
        
        "⏰ **Режим работы:**\n"
        "Ежедневно с 10:00 до 22:00\n"
        "*(Принимаем по предварительной записи)*\n\n"
        
        "📞 **Связаться с администратором:**\n"
        "Тел: +7 (999) 000-11-22\n\n"
        
        "🌐 **Мы в социальных сетях:**\n"
        "🔹 [Наш Telegram-канал](https://t.me/your_channel_link)\n"
        "🔹 [Группа ВКонтакте](https://vk.com/your_group_link)\n"
        "🔹 [Канал в MAX](https://max.com/your_link)\n\n"
        
        "🗺 **Построить маршрут:**\n"
        "📍 [Яндекс Карты](https://yandex.ru/maps/your_link)\n"
        "📍 [2ГИС](https://2gis.ru/moscow/your_link)\n\n"
        
        "Заглядывай в гости на кофе и крутые преображения! 💣"
    )

    await message.answer(
        contacts_text, 
        reply_markup=main_kb,
        parse_mode="Markdown",
        disable_web_page_preview=True  # Чтобы ссылки не раздували сообщение огромными превью
    )

@router.message(F.text == "💎 О салоне")
async def about_btn(message: types.Message):
    print("!!! НАЖАТО О САЛОНЕ !!!")
    
    about_text = (
        "💎 **BEAUTYBOMB — Твоя территория эстетического бунта**\n\n"
        "Мы создали не просто салон, а бьюти-коворкинг нового поколения в самом сердце Москвы. "
        "Это место, где высокое искусство татуировки встречается с премиальным сервисом классического ухода.\n\n"
        
        "✨ **Почему выбирают нас?**\n"
        "● **Смелость без границ:** Мы одинаково идеально сделаем как нюдовый маникюр, так и экстремальный сплит языка.\n"
        "● **Стерильность и безопасность:** Медицинские стандарты гигиены в каждом кабинете — от депиляции до пирсинга.\n"
        "● **Топ-мастера:** В нашей команде работают художники, колористы и стилисты с уникальным почерком.\n"
        "● **Атмосфера:** Кофе, правильная музыка и сообщество людей, которые не боятся проявлять себя.\n\n"
        
        "🔥 **Наша философия:**\n"
        "Мы верим, что внешность — это твой манифест. Наша задача — дать тебе инструменты для его воплощения. "
        "От кончиков ресниц до контура тату, от афро-плетения до идеальной стрижки — мы создаем твою уверенность.\n\n"
        
        "*Приходи за переменами. Приходи за собой.* 💣"
    )

    await message.answer(
        about_text, 
        reply_markup=main_kb,
        parse_mode="Markdown"
    )

@router.message(F.text == "💅 Услуги и цены")
async def prices_btn(message: types.Message):
    print("!!! НАЖАТЫ ЦЕНЫ !!!")
    
    prices_text = (
        "💅 **Прайс-лист BEAUTYBOMB**\n\n"
        "Цены указаны 'ОТ', итоговая стоимость зависит от сложности работы и материалов.\n\n"
        
        "🎨 **ТАТУ И МОДИФИКАЦИИ:**\n"
        "— Татуировка (мини): от 5 000 ₽\n"
        "— Тату (сложная/сеанс): от 12 000 ₽\n"
        "— Пирсинг (с украшением): от 3 500 ₽\n"
        "— Сплит языка: от 20 000 ₽\n\n"
        
        "💇‍♀️ **ВОЛОСЫ:**\n"
        "— Стрижка (женская/мужская): от 3 000 ₽\n"
        "— Окрашивание (в 1 тон): от 6 000 ₽\n"
        "— Сложное окрашивание (Airtouch/Shatush): от 12 000 ₽\n"
        "— Дреды (натуральные/D.E.): от 15 000 ₽\n"
        "— Афро-косы (полное плетение): от 10 000 ₽\n\n"
        
        "👁 **ЛИЦО:**\n"
        "— Наращивание ресниц (Классика/2D): от 3 500 ₽\n"
        "— Наращивание ресниц (3D/Hollywood): от 5 000 ₽\n"
        "— Ламинирование бровей + коррекция: от 2 500 ₽\n\n"
        
        "✨ **МАНИКЮР И УХОД:**\n"
        "— Маникюр с покрытием: от 2 800 ₽\n"
        "— Педикюр с покрытием: от 3 800 ₽\n"
        "— Депиляция (одна зона): от 1 500 ₽\n\n"
        
        "💡 *Хотите точный расчет? Просто опишите свою идею в чате, и я помогу сориентироваться!*"
    )

    await message.answer(
        prices_text, 
        reply_markup=main_kb,
        parse_mode="Markdown"
    )

@router.message(F.text == "📅 Записаться")
async def book_btn(message: types.Message):
    print("!!! НАЖАТА ЗАПИСЬ !!!")
    
    booking_text = (
        "📅 **Онлайн-запись в BEAUTYBOMB**\n\n"
        "Я готов забронировать для тебя лучшее время! Чтобы я смог создать запись, "
        "просто напиши мне в одном сообщении:\n\n"
        "✅ **Что хочешь сделать?** (Услуга)\n"
        "✅ **Как тебя зовут?** (Имя)\n"
        "✅ **Твой номер телефона?**\n"
        "✅ **Когда тебе удобно?** (Дата и время)\n\n"
        "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
        "📝 *Пример: «Я Оксана, хочу на тату 15 апреля в 14:00, мой номер 89991112233»*\n\n"
        "Жду твои данные, и сразу подтвержу запись! 👇"
    )

    await message.answer(
        booking_text, 
        reply_markup=main_kb,
        parse_mode="Markdown"
    )

@router.message()
async def chat_handler(message: types.Message):
    if message.text in ["📍 Контакты", "💎 О салоне", "💅 Услуги и цены", "📅 Записаться"]:
        print("!!! СРАБОТАЛ ПРЕДОХРАНИТЕЛЬ КНОПОК !!!")
        await message.answer("Пожалуйста, нажмите кнопку еще раз.", reply_markup=main_kb)
        return

    print(f"!!! ТЕКСТ ПОШЕЛ В ИИ: {message.text} !!!")
    uid = message.from_user.id
    if uid not in user_contexts:
        user_contexts[uid] = []

    await message.bot.send_chat_action(message.chat.id, "typing")
    ai_response = await get_ai_answer(message.text, user_contexts[uid])

    # Защита от дурака: ищем тег бронирования
    if "[BOOKING:" in ai_response:
        match = re.search(r"\[BOOKING:\s*(.*?)\]", ai_response)
        if match:
            data_str = match.group(1)
            parts = [p.strip() for p in data_str.split('|')]
            
            # Проверяем, что ИИ выдал 5 параметров, и первое слово НЕ равно слову "Имя"
            if len(parts) == 5 and parts[0].lower() != "имя":
                data = {"name": parts[0], "phone": parts[1], "service": parts[2], "date": parts[3], "time": parts[4]}
                await gs_service.add_booking(data)
                clean_text = ai_response.split("[BOOKING:")[0].strip()
                await message.answer(f"✅ {clean_text}\n\nВаша запись успешно оформлена!", reply_markup=main_kb)
                user_contexts[uid] = []
                return

    # Если это обычный ответ или кривой тег — просто выводим текст (очищенный от кривых тегов)
    ai_response_clean = re.sub(r"\[BOOKING:.*?\]", "", ai_response).strip()
    await message.answer(ai_response_clean, reply_markup=main_kb)
    
    user_contexts[uid].append({"role": "user", "content": message.text})
    user_contexts[uid].append({"role": "assistant", "content": ai_response_clean})
    user_contexts[uid] = user_contexts[uid][-6:]