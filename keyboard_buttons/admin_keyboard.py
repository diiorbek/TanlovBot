from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

diagram_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hokim"),
            KeyboardButton(text="Boshqarma"),
        ],
        [
            KeyboardButton(text="Bank"),
            KeyboardButton(text="Quruvchi")
        ]
    ],
    resize_keyboard=True
)