import asyncio
import datetime
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config_reader import config
from aiogram.client.default import DefaultBotProperties
import asyncio
import logging
import aioschedule
from multiprocessing import Process
import random

from aiogram import Bot, Dispatcher, types, F

def mk_ch():
    f = open('/home/uliana/Downloads/_D0_B6_D0_B8_D0_B2_D0_BE_D1_82_D0_BD_D1_8B_D0_B5.txt', 'r')
    ls = list([i.strip() for i in f])
    if len(ls)!=0:
        choice=random.choice(ls)
        ls.remove(choice)
        f = open('/home/uliana/Downloads/_D0_B6_D0_B8_D0_B2_D0_BE_D1_82_D0_BD_D1_8B_D0_B5.txt', 'w')
        f.write('')
        f=open('/home/uliana/Downloads/_D0_B6_D0_B8_D0_B2_D0_BE_D1_82_D0_BD_D1_8B_D0_B5.txt','a')
        for i in ls:
            f.write('\n'+i)
        f.close()
        if choice in ['овца', "собака", "курица", "коза", "корова", "лось", "лох", "муха", "жук навозник"]:
            return f'Cегодня ты: {choice} xD x) :O\n{'https://ru.wikipedia.org/wiki/' + choice}'
        else:
            return f'Cегодня ты: {choice}\n{'https://ru.wikipedia.org/wiki/'+choice}'
    else:
        return f"Животные закончились :'(\n\nПрощальная записка свиньи на мясокомбинате:\nменя колбасит"
choice=mk_ch()

user='1036668682'
logging.basicConfig(level=logging.INFO)
bot=Bot(token=config.bot_token.get_secret_value(),default=DefaultBotProperties(
    parse_mode=ParseMode.HTML
))
dp=Dispatcher()


@dp.message()
async def thing():
    await bot.send_message(chat_id=user,text=choice)
async def sch():
    pt=['16:56']
    while True:
        if datetime.datetime.now().strftime('%H:%M') in pt:
            await thing()
        await asyncio.sleep(60)
def w():
    asyncio.run((sch()))
async def main():
    process=Process(target=w)
    process.start()
    await dp.start_polling(bot)
    process.join()
if __name__=='__main__':
    asyncio.run(main())
# async def main():
#     await dp.start_polling(bot, on_startup=on_startup)
# if __name__=='__main__':
#     asyncio.run(main())