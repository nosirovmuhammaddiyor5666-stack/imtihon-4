import asyncio 
from  aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message ,BotCommand,FSInputFile,CallbackQuery,ReplyKeyboardRemove
from buttons import start_bottons,Kurslar_buttons,Contact_yu,Kurslar_buttons2,Back
from states import RegistrState

bot = Bot(token="8795474224:AAEoEIxkcqCqC-Let2M2_ehZPuxqJftM5Vw")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message:Message):
    name = message.chat.full_name
    await message.answer(f"Botga hush kelibsiz {name}!",reply_markup=await start_bottons())

@dp.message(F.text == "Bekor qilish")
async def Back_m(message:Message):
    await message.answer("Bosh menyuga qaytdingiz!",reply_markup=await start_bottons())

@dp.message(F.text == "Kurslar")
async def Kurslar(message: Message):
    await message.answer("Kurslar haqida malumotlar kerakli yonalishni tanlang",reply_markup=await Kurslar_buttons())

@dp.callback_query(F.data.endswith("Pyt"))
async def Python(calback:CallbackQuery):
    file = FSInputFile("file/python.txt")
    await calback.message.answer_document(file)

@dp.callback_query(F.data.endswith("Web"))
async def Web(calback:CallbackQuery):
    file = FSInputFile("file/web.txt")
    await calback.message.answer_document(file)

@dp.callback_query(F.data.endswith("Grafik"))
async def Grafik(calback:CallbackQuery):
    file = FSInputFile("file/grafik.txt")
    await calback.message.answer_document(file)

@dp.callback_query(F.data.endswith("Fron"))
async def Fron(calback:CallbackQuery):
    file = FSInputFile("file/frontent.txt")
    await calback.message.answer_document(file)

@dp.message(F.text.endswith("yozilish"))
async def Kursga_yozilish(message:Message,state:FSMContext):
    await state.set_state(RegistrState.name)
    await message.answer("Ismingizni toliq kiritng",reply_markup=await Back())

@dp.message(RegistrState.name)
async def reaction_name(message:Message,state:FSMContext):
    await state.update_data(name= message.text)
    await state.set_state(RegistrState.phone)
    await message.answer("Kontaktingizni yuboring!",reply_markup=await Contact_yu())

@dp.message(RegistrState.phone, F.contact)
async def reaction_phone(message:Message,state:FSMContext):
    await state.update_data(phone = message.contact.phone_number)
    await state.set_state(RegistrState.kurs_tanlash)
    await message.answer("Telefon raqamingiz qabul qilindi",reply_markup=await Back())
    await message.answer("Kursni tanlang!",reply_markup=await Kurslar_buttons2())

@dp.callback_query(RegistrState.kurs_tanlash,F.data)
async def Tanlash(calback:CallbackQuery,state:FSMContext):
    await state.update_data(kurs = calback.data)
    data = await state.get_data()
    info = f"Ismingiz: {data.get('name')}\nPhone: {data.get('phone')}\nTanlangan kursingiz: {data.get('kurs')}"
    await calback.message.answer(info)

@dp.message(F.text == "Markaz haqida")
async def Markaz(message: Message):
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6Vi9txdqnJvqOumftjN6SHRnvT2xWZU2Yn1X02eHd9g&s=10")
    await message.answer("Markazimizda oqitiladi \nFullstack \nKibr hafsizlik\nGrafik dizayn\nMobilgraft",reply_markup=await Back())

@dp.message(F.text == "Aloqa")
async def Aloqa(message:Message):
    await message.answer("Aloqa uchun: +998*********\nIsh vaqt 8:00 - 20:00\n",reply_markup=await Back())




async def main():
    await bot.set_my_commands(commands=[BotCommand(command="start",description="botni ishga tushirish")])
    await dp.start_polling(bot)

asyncio.run(main())