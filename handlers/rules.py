from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from loguru import logger

from utils.validations import Validations
from loader import dp

RULES = '<b>Приветствуем в Школе IT!</b>\n' \
        'Для того чтобы пройти дальше, нужно ознакомиться и согласиться с правилами Школы:\n\n' \
        '<b>1. Еженедельные встречи.</b>\n' \
        'Каждую пятницу с 19:00 - 20:00 по МСК, проходят очные встречи для жителей Москвы, территориально - в десяти' \
        ' минутах от станции метро "Деловой центр". ' \
        'Для жителей других городов встречи проходят удалённо' \
        ' (нужно подключиться к звонку в общей беседе "Школа IT")\n\n' \
        '<b>2. Личные карточки.</b>\n' \
        'При вступлении в Школу необходимо заполнить личную карточку и отправить боту в дальнейшей беседе в' \
        ' этом чате.\n\n' \
        '<b>3. Дедлайны</b>\n' \
        'В Школе введена система переносов дедлайнов. ' \
        'За день до дедлайна можно перенести дату. ' \
        'Переносы обсуждаются с тимлидом направления.\n' \
        'Пример: дедлайн на задачу 18.07. Перенести дедлайн этой задачи можно не позднее 17.07.'


@logger.catch
@dp.message_handler(commands='rules')
async def send_rules(message: types.Message, state: FSMContext):
    logger.info(f'Команда {message.text} от @{message.from_user.username} (id: {message.from_user.id})')
    if await Validations.moder_validation_for_supergroups(message):
        await message.answer(RULES, reply_markup=ReplyKeyboardRemove())
        await state.finish()
