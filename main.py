
import telebot
from DDL import *
import nest_asyncio
nest_asyncio.apply()
from telegram import Update
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
api="...................................."
bot = telebot.TeleBot(api)  
from datetime import datetime
from datetime import datetime, timedelta

chanel_cid=..........................
admin=[......................]

command={
        'start' : 'your information and strt robat',
        'keybord': 'buttons ',
        'help':'instructions about keybord & /...',
        'ad_product':'add new product or update them',
        'rate_movie':'is not ready'

        }

genres = ['وحشت', 'علمی تخیلی','اکشن', 'کمدی', 'درام','وسترن ','فانتزی  ','جنگی','خانوادگی ','جنایی ',
          ' عاشقانه','انیمیشن','معمایی و رازآلود','حماسی و تاریخی ','ماجراجویی ','پیشنهاد برای شما']    


movies = {
    'وحشت': [
        {'title':  'smile', 'year': 2020,'description':'داستان','price':123,'photo_link':''},
        {'title': 'فیلم وحشتناک 2', 'year': 2021,'description':'داستان','price':1253,'photo_link':''},],
'علمی تخیلی': [
        {'title': 'فیلم علمی تخیلی 1', 'year': 2021,'description':'داستان','price':123,'photo_link':''},
        {'title': 'فیلم علمی تخیلی 2', 'year': 2022,'description':'داستان','price':123,'photo_link':''}],
    'کمدی': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123,'photo_link':''},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123,'photo_link':''}],
    'اکشن': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123,'photo_link':''},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123,'photo_link':''}
    ],
    'درام': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123,'photo_link':''},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123,'photo_link':''}
    ],
    'وسترن': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'فانتزی': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'جنگی': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'خانوادگی': [
        {'title': 'فیلم درام 1', 'year': 2018,'description':'داستان','price':123},
        {'title': 'فیلم درام 2', 'year': 2019,'description':'داستان','price':123}
    ],
    'جنایی': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'عاشقانه': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'انیمیشن': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'معمایی و رازآلود': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'حماسی و تاریخی ': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'ماجراجویی': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ],
    'پیشنهاد برای شما': [
        {'title': 'فیلم کمدی 1', 'year': 2019,'description':'داستان','price':123},
        {'title': 'فیلم کمدی 2', 'year': 2020,'description':'داستان','price':123}
    ]
}
    
            
            



# لیست کاربران شناخته شده
know_user=[]  #[id1,id2,.......]
# دیکشنری برای ذخیره تاریخ‌ها
first_act={}  #{id1:[time,time.change]}
def all_active(cid):
    if cid not in know_user: 
        created_at=datetime.now()
        know_user.append(cid)
        first_act[cid] = [created_at, created_at]  # ذخیره تاریخ ورود و تاریخ به‌روزرسانی اولیه
    else:
        first_act[cid][1] = datetime.now()  # به‌روزرسانی تاریخ آخرین فعالیت
        
        
def check_user_activity(user_id, updated_at):
    # فرض کنید که تابعی برای دریافت زمان آخرین فعالیت کاربر دارید
        last_activity = updated_at
        if last_activity:
            if datetime.now() - last_activity > timedelta(weeks=2):
                # اگر کاربر در طول دو هفته گذشته فعالیت نداشته باشد
                bot.send_message(user_id, "شما در طول دو هفته گذشته فعالیتی نداشته‌اید. لطفاً دوباره فعال شوید.")
                return 'inactive'
            else:
                return 'active'
        else:
            return 'new'  # اگر کاربر جدید باشد 
    
def inserttouser(message):#اطلاعات کاربرم با هر فعالیتی ذخیره بشه
    cid=message.chat.id
    user_id = message.from_user.id  # شناسه کاربر(message.chat.id)
    first_name = message.from_user.first_name  # نام
    last_name = message.from_user.last_name  # نام خانوادگی (اختیاری)
    username = message.from_user.username  # نام کاربری (اختیاری)
    created=first_act[cid][0]
    updated_at=first_act[cid][1]
    status = check_user_activity(user_id, updated_at)  # بررسی فعالیت کاربر
    insert_USER(cid,first_name,last_name,created,updated_at,status)
    
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
   cid = message.chat.id
   all_active(cid)
   inserttouser(message)
   bot.reply_to(message, "سلام! برای دریافت اطلاعات پروفایل خود، لطفاً یک پیام ارسال کنید.\nاگر بدنبال فیلم ها میگردید کلمه _(فیلم)_ رو تایپ کنید \n/help ",parse_mode= 'Markdown')

@bot.message_handler(commands=['help'])
def command_help(message):
    cid = message.chat.id
    help_text = "The following commands are available: \n"
    for key in command:  
        help_text += "/" + key + ": "
        help_text += command[key] + "\n"
        
    bot.send_message(cid, help_text)
    
    
@bot.message_handler(commands=['ad_product'])
def send_pho(message):
    cid=message.chat.id
    all_active(cid)
    inserttouser(message)
    print(message.chat.first_name)
    if cid in admin:
        bot.reply_to(message,"این متن رو کپی کرده و اطلاعات رو تغییر بدید\n")
        bot.send_message(cid,"name: smile-- discription: توضیحات-- category: وحشت -- price:120 -- point_p: 5")
    #bot.register_next_step_handler(message,photo_step)
    else:
        send_user_info(message)
        
@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    cid=message.chat.id
    all_active(cid)
    inserttouser(message)
    file_id=message.photo[-1].file_id
    caption=message.caption
    res=caption.split('--')
    try:
            product_name=res[0].split(':')[-1].strip()
            discription=res[1].split(':')[-1].strip()  
            cATEGORY=res[2].split(':')[-1].strip()
            price=float(res[3].split(':')[-1].strip())
            point_p=int(res[4].split(':')[-1].strip())
            
            text=f""" name:{product_name}
            """
            ress=bot.send_photo(chanel_cid,file_id,caption=text)
            MID=ress.message_id#محل قرار گیری عکس و محصول جدید داخل کانال ایجاد شده
           # print(MID,ress)
            insert_product(product_name,discription,MID,cATEGORY,price,point_p)
            print(" insert product")
    except Exception as e:
            bot.send_message(cid, "خطا در پردازش اطلاعات. لطفاً دوباره تلاش کنید.")
            print(f"Error: {e}")



 
    
@bot.message_handler(func=lambda message:message.text=='فیلم')
def inlinemarkup_command(message):
    cid = message.chat.id
    all_active(cid)
    inserttouser(message)
    markup = InlineKeyboardMarkup()
    #     for genre in genres:
#         markup.add(InlineKeyboardButton(genre, callback_data=genre))
    buttons = [InlineKeyboardButton(genre, callback_data=genre) for genre in genres]    # استفاده از حلقه برای اضافه کردن دکمه‌ها دوتا دوتا 
    for i in range(0, len(buttons), 2):
        markup.row(*buttons[i:i+2])
    bot.send_message(cid, 'ژانر مورد نظر خود را انتخاب کنید:', reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.data in genres)  #اگر ژانرم داخل genreبود
def callback_query(call):
    genre = call.data        #ژانر فیلم ارسال شده را دریافت میکنه
    global movie_list      #باعث میشه خارج ار تابع و در تابع دیگر قابل خواندن باشد
    movie_list = movies.get(genre, [])#حالا ژانر ارسال شده رو داخل مویز میگرده       movies= {جنگی:[{film1:nan,year:12},{fimme2:rar,years:156}]}
    markup = InlineKeyboardMarkup()
    response = "\n".join([f"\nعنوان: {movie['title']}\nسال: {movie['year']} خلاصه:{movie['description']}" for movie in movie_list])#برای فیلم های داخل ژانر جنگی
    buttons = [InlineKeyboardButton(movie['title'], callback_data=movie['title']) for movie in movie_list]
    for i in range(0, len(buttons), 2):
        markup.row(*buttons[i:i+2])
    bot.send_message(call.message.chat.id,response, reply_markup=markup)
    


@bot.callback_query_handler(func=lambda call: call.data in [movie['title'] for movie in movie_list])
def movie_detail_callback(call):
    movie_title = call.data
    print(movie_title)
    print(call.message.id)

    global movie
    movie = next((movie for movie in movie_list if movie['title'] == movie_title), None)
    if movie:
        bot.send_message(call.message.chat.id, f"جزئیات فیلم:\nعنوان: {movie['title']}\nسال: {movie['year']}\nخلاصه: {movie['description']}", reply_markup=get_markup(movie['price'], 1))
    else:
        bot.send_message(call.message.chat.id, "فیلم مورد نظر یافت نشد.")

def get_markup(price, qty):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('➖', callback_data=f"edit_{price}_{qty-1}" if qty > 1 else 'disabled'),
               InlineKeyboardButton(str(qty), callback_data=str(qty)),
               InlineKeyboardButton('➕', callback_data=f"edit_{price}_{qty+1}"))
    markup.add(InlineKeyboardButton('buy', callback_data=f"buy_{price}_{qty}"))
    markup.add(InlineKeyboardButton('cancel', callback_data='cancel'))
    return markup    

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    cid = call.message.chat.id
    mid = call.message.id
    data = call.data
    call_id = call.id
    if data.startswith('edit'):
        command, price, qty = data.split('_')  # تغییر نام code به price
        price = int(price)  # قیمت را تبدیل به عدد صحیح کنید
        qty = int(qty)
        if qty == 0:
            bot.answer_callback_query(call_id, 'quantity can not be zero')
            return
        else:
            bot.answer_callback_query(call_id, f'increased to {qty}')  
            bot.edit_message_text(f'total cost: {price * qty}', cid, mid, reply_markup=get_markup(price, qty))  # استفاده از price به جای code

    elif data == 'cancel':
        bot.answer_callback_query(call_id, 'process canceled')
        bot.edit_message_reply_markup(cid, mid, reply_markup=None)
        
    elif data.startswith('buy'):
        command, price, qty = data.split('_')  # استخراج قیمت و تعداد
        price = int(price)  # تبدیل به عدد صحیح
        qty = int(qty)  # تبدیل به عدد صحیح
        sum_price = price * qty  # محاسبه قیمت کل
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('cancel', callback_data='cancel'),
                   InlineKeyboardButton('پرداخت انجام شد', callback_data='payment_completed'))  # تغییر callback_data به یک مقدار مناسب
        insert_sell_row(cid, qty, sum_price)
        print("sell_row")
        bot.send_message(cid, f' محصول شما به تعداد {qty} و قیمت {sum_price} \n لطفا از 1 تا 10 به فیلم نمره بدهید', reply_markup=markup)


user_data = {}
@bot.message_handler(commands=['rate_movie'])
def ask_for_rating(message):
    cid = message.chat.id
    bot.send_message(cid, "اسم فیلم مورد نظر را انتخاب کرده و نظر خود را از 1 تا 10 به اشتراک بگذارید")

@bot.message_handler(func=lambda message: any(movie['title'] == message.text for genre in movies.values() for movie in genre))
def move_part(message):
    cid = message.chat.id
    bot.send_message(cid, "نظر خود را از 1 تا 10 به اشتراک بگذارید")
    user_data[cid] = message.text  # استفاده از user_data به جای bot.user_data

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_rating(message):
    rating = int(message.text)
    cid = message.chat.id

    if 1 <= rating <= 10:
        product_name = user_data.get(cid)  # استفاده از user_data به جای bot.user_data
        #print(product_name)#اسم 
        if product_name:
            insert_movie_ratings(product_name, cid, rating)
            print("rate")
            bot.send_message(cid, "نظر شما با موفقیت ثبت شد!")
        else:
            bot.send_message(cid, "عنوان فیلمی پیدا نشد.")
    else:
        bot.send_message(cid, "لطفاً یک عدد معتبر بین 1 تا 10 وارد کنید.")






# @bot.message_handler(commands=['keybord'])   
# def keybord_command(message):
#     cid=message.chat.id
#     markup=ReplyKeyboardMarkup()
#     markup.add('button','button2') 
#     markup.add('button3','button4')    
#     bot.send_message(cid,'sample text',reply_markup=markup) 
      
# @bot.message_handler(func=lambda message:message.text=='button')
# def button_one(message):
#     cid=message.chat.id
#     hideboard=ReplyKeyboardRemove()
#     bot.send_message(cid,'message for button 1',reply_markup=hideboard)


    
buttons = [{'button1':'text1'}, {'button2':'text2'}, {'button3':'text3'}, {'button4':'text4'}]

@bot.message_handler(commands=['keybord'])
def keybord_command(message):
    cid = message.chat.id
    all_active(cid)
    inserttouser(message)
    markup = ReplyKeyboardMarkup(resize_keyboard=True) # تنظیم صفحه کاید به صورت خودکار به اندازه صفحه نمایش کاربر
    for i in range(0, len(buttons),2):    
        row_buttons = [KeyboardButton(list(button.keys())[0]) for button in buttons[i:i+2]]
        markup.row(*row_buttons)
    bot.send_message(cid, "Choose an option:", reply_markup=markup)
        # # markup.row(*buttons[i:i+2])
    # for button in buttons:       کلید ها ززیر هم زیر هم قرار میگیرند
    #     markup.add(button)

@bot.message_handler(func=lambda message: message.text in [list(button.keys())[0] for button in buttons])
def handle_buttons(message):
    cid = message.chat.id
    all_active(cid)
    inserttouser(message)
    mal=message.text
    print(mal)
    button_text = "No description found"
    for button in buttons:
        if mal in button:
            button_text = button[mal] #اگر چیزری پیدا نشد میاد متنی که بالا قرار دادیم رو نشون میده
            break  # اگر مقدار پیدا شد، از حلقه خارج می‌شویم
    text = f'message for {message.text} , {button_text}'

    hideboard = ReplyKeyboardRemove()
    bot.send_message(cid, text, reply_markup=hideboard)

    



    
@bot.message_handler(func=lambda message: True)
def send_user_info(message):
    cid=message.chat.id
    all_active(cid)
    #print(message.text)   متن فرستادهشده
    #print(message) کل اطلاعات پیام
    inserttouser(message)

    # mesfor=message.forward_from_chat   پیدا کردن ایدی عددی کانال
    user_id = message.from_user.id  # شناسه کاربر(message.chat.id)
    first_name = message.from_user.first_name  # نام
    last_name = message.from_user.last_name  # نام خانوادگی (اختیاری)
    username = message.from_user.username  # نام کاربری (اختیاری)
    # photos = bot.get_user_profile_photos(user_id)عکس فرد رو بگیره#
    # print(message)#{'content_type': 'text', 'id': 600, 'message_id': 600, 'from_user': {'id': 5580972570, 'is_bot': False, 'first_name': 'Sarina *~*', 'username': 'sarina_ee', 'last_name': None, 'language_code': 'en', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None
    # print("===============================")
    # print(message.id)#601
    # print(message.text)#پیام ارسال شده
    # print("===============================")
    # print(message.chat.id)#5580972570
    # print("===============================")
    # print(message.from_user.id)#5580972570

    if message.text == "help"  or "Help":
        bot.reply_to(message, 'if you need help please click  /help')    
    else:    
        response = f"""
        شناسه کاربر: {user_id}
        نام: {first_name}
        نام خانوادگی: {last_name if last_name else 'ندارد'}
        نام کاربری: @{username if username else 'ندارد'}
        به family movie خوش اومدید.
        ژانر مورد نظر خودتون رو انتخاب کنید یا اسم فیلم رو برامون تایپ کنید.
        """   
        # if photos.total_count > 0:
        #     bot.send_photo(message.chat.id, photos.photos[0][0].file_id, caption=response)
        # else:
        bot.reply_to(message, response)
        





# # if __name__ == '__main__':
bot.infinity_polling()






































    
