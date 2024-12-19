from filters.check_sub_channel import IsCheckSubChannels
from loader import bot,db,dp,CHANNELS,ADMINS
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message,InlineKeyboardButton, FSInputFile
from aiogram.filters import Command
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts
from aiogram.fsm.context import FSMContext #new
from keyboard_buttons import admin_keyboard, user_keyboard
import time 
from aiogram import F
from .utils import create_statistics_images

@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Statistika",IsBotAdminFilter(ADMINS))
async def statistics(message: Message):
    await message.answer(text="Qaysi biri bo'yicha statistikani tanlamoqchisiz?", reply_markup=admin_keyboard.diagram_button)

@dp.message(F.text.in_(["Hokim", "Boshqarma", "Bank", "Quruvchi"]), IsBotAdminFilter(ADMINS))
async def send_statistics(message: Message):
    create_statistics_images()
    stats = create_statistics_images()
    txt = ""
    img = FSInputFile('statistics/hokim_statistics.png')
    
    if message.text == "Hokim":
        txt += stats['hokim']
        img = FSInputFile('statistics/hokim_statistics.png')
        
    elif message.text == "Boshqarma":
        txt += stats['boshqarma']
        img = FSInputFile('statistics/boshqarma_statistics.png')
        
    elif message.text == "Bank":
        txt += stats['bank']
        img = FSInputFile('statistics/bank_statistics.png')
        
    elif message.text == "Quruvchi":
        txt += stats['quruvchi']
        img = FSInputFile('statistics/quruvchi_statistics.png')
    
    await message.answer_photo(photo=img, caption=txt)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")
    

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

@dp.message(F.text == "Guruhlarga yuborish")
async def send_to_groups(message: Message):
    for channel in CHANNELS:
        await bot.send_message(chat_id=channel, text="Yil davomida eng samarali faoliyat olib borgan hudud hokimi", reply_markup=user_keyboard.create_hokim_keyboard())
        await bot.send_message(chat_id=channel, text="Viloyat aholisiga 2024 yil davomida eng yaxshi xizmat ko'rsatgan bank", reply_markup=user_keyboard.create_bank_keyboard())
        await bot.send_message(chat_id=channel, text="Yilning eng samarali faoliyat yuritgan boshqarmasi", reply_markup=user_keyboard.create_boshqarma_keyboard())
        await bot.send_message(chat_id=channel, text="Yil quruvchisi", reply_markup=user_keyboard.create_quruvchi_keyboard())
        
    await message.answer(text="Ovoz berish guruhlarga yuborildi!")