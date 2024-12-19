from aiogram import Bot, Dispatcher
from data import config
from baza.sqlite import Database
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
db = Database(path_to_db="main.db")
dp = Dispatcher()

hokim_list = ["Navoiy shahri hokimi Dilmurod Ergashev", "Nurota tumani hokimi Azamat Fayziyev", 
                  "Navbahor tumani hokimi Azamat O'roqov", "Qiziltepa tumani hokimi Bekzod Bobomurodov", 
                  "Zarafshon shahri hokimi Nazirbek Raxmanov", "Xatirchi tumani hokimi Umidjon Adizov", 
                  "Uchquduq tumani hokimi Uchqun Elmuratov", "Karmana tumani hokimi Valijon Adizov", 
                  "Konimex tumani hokimi Ruslan Ro'ziyev", "Tomdi tumani hokimi Orzumurod Umarov", 
                  "G'ozg'on shahri hokimi Nurali Jo'rayev"]
    
bank_list = ["O'zbekiston milliy banki", "Xalq banki", "Ipoteka bank", "Sanoat Qurilish bank", 
                 "Agrobank", "Hamkor bank", "Asaka bank", "Biznesni rivojlantirish banki", 
                 "Turon bank", "Mikrokreditbank", "Infinbank", "Aloqabank", "Kapital bank", 
                 "Ipak yo'li bank", "Anor bank", "Uzum bank", "Orient finans bank", "TBC bank"]
    
boshqarma_list = ["Maktab va maktabgacha ta'lim boshqarmasi", "Milliy gvardiya viloyat bo'yicha boshqarmasi", 
                      "Ichki ishlar boshqarmasi", "Avtomobil yo'llari Bosh boshqarmasi", 
                      "Oliy ta'lim, fan va inovatsiyalar boshqarmasi", "'Navoiy Hududgaz' boshqarmasi", 
                      "'Hududiy elektr tarmoqlari' boshqarmasi", "'Navoiy suv ta'minot' boshqarmasi", 
                      "Qurilish va uy-joy kommunal xo'j. boshqarmasi", "Sport boshqarmasi", 
                      "Turizm boshqarmasi", "Faqulodda vaziyatlar boshqarmasi", "Soliq boshqarmasi", 
                      "Bojxona boshqarmasi", "Moliya boshqarmasi"]
    
quruvchi_list = ["Zarafshan Golden Group", "ART HOUSE", "Tinchlik", "Yangi Hayot", "Xonsaroy", 
                     "Iskandar Buildings", "Alisher quruvchi", "Ashraf", "Sharq Qurilish", 
                     "G'olib Javohir qurilish montaj", "Bektosh", "Muzaffar Shahribonu poydevori"]

erkak_tadbirkor_list = ["Ulug'bek Fayziyev - 'Zarafshan Golden Group'", 
                        "Abdukarim Saksonov - 'Yangi Hayot'", 
                        "Jo'rabek Xoliqov - 'Tinchlik'",
                        "Sefa Mengi - 'Mengi tekstil'",
                        "Husniddin Gapparov - 'Muhtasham mebellar'",
                        "Hasanbek Sohibov - 'Ashraf' MCHJ",
                        "Husniddin Normurodov -'Ishonch Feruz' XK",
                        "G'olibjon Karimov - 'REGAL HOTEL BY GRAND'",
                        "Davron Pirmuhammedov - 'PREMIER TEXTILE'",
                        "Diyor Ismatov - 'Modern traiding servis' MCHJ"]

ayol_tadbirkor_list = ["Shaxnoza Karimova - 'BARAKA NON-NAVOIY'",
                       "Zebo Qalandarova - Navbahor t. 'Dress making'",
                       "Munira Xudoyqulova Nurota t. 'Munira new brend'",
                       "Saodat Elova - Uchquduq t. 'Choco Life'",
                       "Shohista Axmedova - Karmana t. 'Samo yulduzi'",
                       "Marxabo Raxmanova - 'Marxabo ziyo'"]

yangilik_list = ["Navoiy Pedagogika instituti Navoiy Davlat Universitetiga aylantirildi.",
                 "Zarafshon Golden Group kompaniyasi Turkiyaning DEDEMAN mehmonxonalar brendi bilan hamkorlikni yo'lga qo'ydi",
                 "Yangi Navoiy shaharchasi qurilishi boshlandi.",
                 "Navoiy shahrida eng zamonaviy tipdagi yirik Axborot kutubxona markazi qurilyapti.",
                 "Navoiy viloyatining 'Turon' yoshlar teatr gruppasi Respublika jamoalari orasida birinchilikni qo'lga kiritdi.",
                 "Navoiy shahrida Tinchlik Plazaning 2-tarmog'i ochildi.",
                 "Elbek Sultonov Paralimpiya o'yinlari chempioni bo'ldi."]
