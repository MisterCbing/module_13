from imports import *


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! Я бот, помогающий твоему здоровью.")

@dp.message(or_f(F.text.lower().contains('hi'), F.text.lower().contains('hello')))
async def no_english(message: Message):
    await message.answer("Sorry, I'm just newbie, I don't speak English.")

@dp.message(F.text.lower().contains('жирный'), F.text.lower().contains("ты"))
async def fat_shaming(message: Message):
    await message.answer('Я не жирный, у меня просто кость широкая')

@dp.message()
async def default_answer(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    bot = Bot(token=TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())