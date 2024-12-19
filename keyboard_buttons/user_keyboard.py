from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.users.utils import get_statistics
from loader import hokim_list, bank_list, boshqarma_list, quruvchi_list, erkak_tadbirkor_list, ayol_tadbirkor_list, yangilik_list

category_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="category_1"),
            InlineKeyboardButton(text="2", callback_data="category_2"),
        ],
        [
            InlineKeyboardButton(text="3", callback_data="category_3"),
            InlineKeyboardButton(text="4", callback_data="category_4"),
        ],
        [
            InlineKeyboardButton(text="5", callback_data="category_5"),
            InlineKeyboardButton(text="6", callback_data="category_6")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="category_7")
        ]
    ],
)

def create_hokim_keyboard():
    builder = InlineKeyboardBuilder()
    
    for i, hokim in enumerate(hokim_list):
        hokim_stats = get_statistics(hokim, "hokim", hokim_list)
        builder.button(text=f"{hokim} - {hokim_stats}    ", callback_data=f"hokim_{hokim}")
        
    
    builder.adjust(1)
    return builder.as_markup()

def create_bank_keyboard():
    builder = InlineKeyboardBuilder()
    
    
    for i, bank in enumerate(bank_list):
        bank_stats = get_statistics(bank, "bank", bank_list)
        builder.button(text=f"{bank} - {bank_stats}", callback_data=f"bank_{bank}")
    
    builder.adjust(1)
    return builder.as_markup()

def create_boshqarma_keyboard():
    builder = InlineKeyboardBuilder()
    for i, boshqarma in enumerate(boshqarma_list):
        boshqarma_stats = get_statistics(boshqarma, "boshqarma", boshqarma_list)
        builder.button(text=f"{boshqarma} - {boshqarma_stats}      ", callback_data=f"boshqarma_{boshqarma}")
        
    builder.adjust(1)
    return builder.as_markup()

def create_quruvchi_keyboard():
    builder = InlineKeyboardBuilder()
    for i, quruvchi in enumerate(quruvchi_list):
        quruvchi_stats = get_statistics(quruvchi, "quruvchi", quruvchi_list)
        builder.button(text=f"{quruvchi} - {quruvchi_stats}", callback_data=f"quruvchi_{quruvchi}")
        
    builder.adjust(1)
    return builder.as_markup()

orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga 🔙")]
    ]
)

def create_erkak_tadbirkor_keyboard():
    builder = InlineKeyboardBuilder()
    for i, erkak_tadbirkor in enumerate(erkak_tadbirkor_list):
        erkak_tadbirkor_stats = get_statistics(erkak_tadbirkor, "erkak-tadbirkor", erkak_tadbirkor_list)
        builder.button(text=f"{erkak_tadbirkor} - {erkak_tadbirkor_stats}   ", callback_data=f"erkak-tadbirkor_{i+1}")
        
    builder.adjust(1)
    return builder.as_markup()

orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga 🔙")]
    ]
)

def create_ayol_tadbirkor_keyboard():
    builder = InlineKeyboardBuilder()
    for i, ayol_tadbirkor in enumerate(ayol_tadbirkor_list):
        ayol_tadbirkor_stats = get_statistics(ayol_tadbirkor, "ayol-tadbirkor", ayol_tadbirkor_list)
        if ayol_tadbirkor == "Munira Xudoyqulova Nurota t. 'Munira new brend'":
            builder.button(text=f"{ayol_tadbirkor}-{ayol_tadbirkor_stats}   ", callback_data=f"ayol-tadbirkor_{i+1}")
        
        else:
            builder.button(text=f"{ayol_tadbirkor} - {ayol_tadbirkor_stats}   ", callback_data=f"ayol-tadbirkor_{i+1}")
        
    builder.adjust(1)
    return builder.as_markup()

def create_yangilik_keyboard():
    builder = InlineKeyboardBuilder()
    for i, yangilik in enumerate(yangilik_list):
        yangilik_stats = get_statistics(yangilik, "yangilik", yangilik_list)
        builder.button(text=f"{i+1} - {yangilik_stats}", callback_data=f"yangilik_{i+1}")
        
        
    builder.adjust(1)
    return builder.as_markup()

orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Orqaga 🔙")]
    ]
)