from aiogram.types import Message
from loader import dp,db,bot,CHANNELS, erkak_tadbirkor_list, ayol_tadbirkor_list, yangilik_list
from aiogram.filters import CommandStart
from aiogram.filters import Command
from filters.check_sub_channel import IsCheckSubChannels
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message,InlineKeyboardButton, CallbackQuery
from keyboard_buttons import user_keyboard
from aiogram import F
from .utils import add_vote, create_statistics_images, write_probel

@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message:Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index,channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal",url=ChatInviteLink.invite_link))
    inline_channel.adjust(1,repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga azo bo'ling",reply_markup=button)

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"""Assalomu alaykum, {full_name}! 👋  

So'rovnomada qatnashing:

1. Yil davomida eng samarali faoliyat olib borgan hudud hokimi.
2. Viloyat aholisiga 2024 yil davomida eng yaxshi xizmat ko'rsatgan bank.
3. Yilning eng samarali faoliyat yuritgan boshqarmasi
4. Yil quruvchisi
5. Yilning eng yaxshi tadbirkori (erkaklar o'rtasida)
6. Yilning eng yaxshi tadbirkori (ayollar o'rtasida)
7. YIL YANGILIGI

Siz ushbu toifalarga ovoz bering!
""", reply_markup=user_keyboard.category_button)
    except:
        await message.answer(text=f"""Assalomu alaykum, {full_name}! 👋  

So'rovnomada qatnashing:

1. Yil davomida eng samarali faoliyat olib borgan hudud hokimi.
2. Viloyat aholisiga 2024 yil davomida eng yaxshi xizmat ko'rsatgan bank.
3. Yilning eng samarali faoliyat yuritgan boshqarmasi
4. Yil quruvchisi
5. Yilning eng yaxshi tadbirkori (erkaklar o'rtasida)
6. Yilning eng yaxshi tadbirkori (ayollar o'rtasida)
7. YIL YANGILIGI

Siz ushbu toifalarga ovoz bering!

""", reply_markup=user_keyboard.category_button)

@dp.callback_query(F.data == "category_1")
async def send_category_1(callback: CallbackQuery):
    await callback.message.edit_text(text="Yil davomida eng samarali faoliyat olib borgan hudud hokimi", reply_markup=user_keyboard.create_hokim_keyboard())
    
@dp.callback_query(F.data == "category_2")
async def send_category_2(callback: CallbackQuery):
    await callback.message.edit_text(text="Viloyat aholisiga 2024 yil davomida eng yaxshi xizmat ko'rsatgan bank", reply_markup=user_keyboard.create_bank_keyboard())

    
@dp.callback_query(F.data == "category_3")
async def send_category_3(callback: CallbackQuery):
    await callback.message.edit_text(text="Yilning eng samarali faoliyat yuritgan boshqarmasi", reply_markup=user_keyboard.create_boshqarma_keyboard())

    
@dp.callback_query(F.data == "category_4")
async def send_category_4(callback: CallbackQuery):
    await callback.message.edit_text(text=write_probel("Yil quruvchisi"), reply_markup=user_keyboard.create_quruvchi_keyboard())

    
@dp.callback_query(F.data == "category_5")
async def send_category_5(callback: CallbackQuery):
    await callback.message.edit_text(text="Yilning eng yaxshi tadbirkori (erkaklar o'rtasida)", reply_markup=user_keyboard.create_erkak_tadbirkor_keyboard())

    
@dp.callback_query(F.data == "category_6")
async def send_category_6(callback: CallbackQuery):
    await callback.message.edit_text(text="Yilning eng yaxshi tadbirkori (ayollar o'rtasida)", reply_markup=user_keyboard.create_ayol_tadbirkor_keyboard())

    
@dp.callback_query(F.data == "category_7")
async def send_category_7(callback: CallbackQuery):
    await callback.message.edit_text(text="""YIL YANGILIGI
1. Navoiy Pedagogika instituti Navoiy Davlat Universitetiga aylantirildi.
2. Zarafshon Golden Group kompaniyasi Turkiyaning DEDEMAN  mehmonxonalar brendi bilan hamkorlikni yo'lga qo'ydi
3. Yangi Navoiy shaharchasi qurilishi boshlandi.
4. Navoiy shahrida eng zamonaviy tipdagi yirik Axborot kutubxona markazi qurilyapti.
5. Navoiy viloyatining 'Turon' yoshlar teatr gruppasi Respublika jamoalari orasida birinchilikni qo'lga kiritdi.
6. Navoiy shahrida Tinchlik Plazaning 2-tarmog'i ochildi.
7. Elbek Sultonov Paralimpiya o'yinlari chempioni bo'ldi.
                                  
                                  """, reply_markup=user_keyboard.create_yangilik_keyboard())

@dp.callback_query(
    (F.data.startswith("hokim_")) |
    (F.data.startswith("bank_")) |
    (F.data.startswith("boshqarma_")) |
    (F.data.startswith("quruvchi_")) |
    (F.data.startswith("erkak-tadbirkor_")) |
    (F.data.startswith("ayol-tadbirkor_")) |
    (F.data.startswith("yangilik"))
)
async def vote_to_category(callback: CallbackQuery):
    user_choice = callback.data.split("_")
    stats = create_statistics_images()
    if user_choice[0] == "hokim":
        text = add_vote(callback.from_user.full_name, callback.from_user.id, user_choice[0], callback.data.split("_")[1])
        await callback.message.edit_text(text="yil davomida eng samarali faoliyat olib borgan hudud hokimi", reply_markup=user_keyboard.create_hokim_keyboard()) 
        
    elif user_choice[0] == "bank":
        text = add_vote(callback.from_user.full_name, callback.from_user.id, user_choice[0], callback.data.split("_")[1])
        await callback.message.edit_text(text="viloyat aholisiga 2024 yil davomida eng yaxshi xizmat ko'rsatgan bank", reply_markup=user_keyboard.create_bank_keyboard())
        
    elif user_choice[0] == "boshqarma":
        
        text = add_vote(callback.from_user.full_name, callback.from_user.id, user_choice[0], callback.data.split("_")[1])
        await callback.message.edit_text(text="yilning eng samarali faoliyat yuritgan boshqarmasi", reply_markup=user_keyboard.create_boshqarma_keyboard()) 
        
    elif user_choice[0] == "quruvchi":
        text = add_vote(callback.from_user.full_name, callback.from_user.id, user_choice[0], callback.data.split("_")[1])
        await callback.message.edit_text(text=write_probel("yil quruvchisi"), reply_markup=user_keyboard.create_quruvchi_keyboard())
        
    elif user_choice[0] == "erkak-tadbirkor":
        choice = erkak_tadbirkor_list[int(callback.data.split("_")[1]) - 1]
        text = add_vote(callback.from_user.full_name, callback.from_user.id, user_choice[0], choice)
        await callback.message.edit_text(text="yilning eng yaxshi tadbirkori (erkaklar o'rtasida)", reply_markup=user_keyboard.create_erkak_tadbirkor_keyboard())
        
    elif user_choice[0] == "ayol-tadbirkor":     
        choice = ayol_tadbirkor_list[int(callback.data.split("_")[1]) - 1]
        text = add_vote(callback.from_user.full_name, callback.from_user.id, user_choice[0], choice)
        await callback.message.edit_text(text="yilning eng yaxshi tadbirkori (ayollar o'rtasida)", reply_markup=user_keyboard.create_ayol_tadbirkor_keyboard())
        
    elif user_choice[0] == "yangilik":
        choice = yangilik_list[int(callback.data.split("_")[1]) - 1]
        text = add_vote(callback.from_user.full_name, callback.from_user.id, user_choice[0], choice)
        await callback.message.edit_text(text="""yil yangiligi
1. Navoiy Pedagogika instituti Navoiy Davlat Universitetiga aylantirildi.
2. Zarafshon Golden Group kompaniyasi Turkiyaning DEDEMAN  mehmonxonalar brendi bilan hamkorlikni yo'lga qo'ydi
3. Yangi Navoiy shaharchasi qurilishi boshlandi.
4. Navoiy shahrida eng zamonaviy tipdagi yirik Axborot kutubxona markazi qurilyapti.
5. Navoiy viloyatining 'Turon' yoshlar teatr gruppasi Respublika jamoalari orasida birinchilikni qo'lga kiritdi.
6. Navoiy shahrida Tinchlik Plazaning 2-tarmog'i ochildi.
7. Elbek Sultonov Paralimpiya o'yinlari chempioni bo'ldi.""", reply_markup=user_keyboard.create_yangilik_keyboard())
         
    await callback.answer(text=text)
    
    await callback.message.answer(text=f"""So'rovnomada qatnashing:

1. Yil davomida eng samarali faoliyat olib borgan hudud hokimi.
2. Viloyat aholisiga 2024 yil davomida eng yaxshi xizmat ko'rsatgan bank.
3. Yilning eng samarali faoliyat yuritgan boshqarmasi
4. Yil quruvchisi
5. Yilning eng yaxshi tadbirkori (erkaklar o'rtasida)
6. Yilning eng yaxshi tadbirkori (ayollar o'rtasida)
7. YIL YANGILIGI

Siz ushbu toifalarga ovoz bering!

""", reply_markup=user_keyboard.category_button)
