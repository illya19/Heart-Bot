
import logging
import asyncio
from aiogram import Bot, Dispatcher, types


logging.basicConfig(level=logging.INFO)

TOKEN = '6457610909:AAGGgcxkr_ErAVWWXs1VYcPp0Q1D8pv2BQs'
bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def starti_handler(message: types.Message):
    chat_id = message.chat.id
    await message.reply("Запускаю отправку сердечек!")
    await send_heartbeats(chat_id)

async def send_heartbeats(chat_id):
    count = 1
    while True:
        if count == 1:
            await bot.send_message(chat_id=chat_id, text=f'{count}❤️ сердечко')
        elif count % 10 == 1 and count % 100 != 11:
            await bot.send_message(chat_id=chat_id, text=f'{count}❤️ сердечко')
        elif count % 10 in [2, 3, 4] and count % 100 not in [12, 13, 14]:
            await bot.send_message(chat_id=chat_id, text=f'{count}❤️ сердечка')
        else:
            await bot.send_message(chat_id=chat_id, text=f'{count}❤️ сердечек')
        count += 1
        await asyncio.sleep(3)  # задержка в 1 секунду

if __name__ == '__main__':
    dp.register_message_handler(starti_handler, commands=['starti'])
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(dp.start_polling())
    finally:
        loop.run_until_complete(bot.close())
        loop.close()

