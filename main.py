import os
import sys
import time
import telebot
from telebot import types

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ADMIN_ID = int(os.environ.get("ADMIN_ID", "333416014"))
CHANNEL_USERNAME = "@vip_bbg"
SUPPORT_USERNAME = "@czccvz"
ASIA_NUMBER = "07756320299"
TON_WALLET = "UQB4z3HA-WY5ZrbhIvucFMy9waz6eSb6BoZjT5gctNJHGak7"

bot = telebot.TeleBot(TOKEN)

# حقوق الأداة الثابتة للمستثمر زينب
ZAINAB_RIGHTS = "👑 أداة التداول الشاملة للمستثمر زينب 👑"

# قائمة التحكم الرئيسية (أزرار شفافة ملونة بالإيموجي)
def main_inline_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_trade = types.InlineKeyboardButton("🟢 📊 صفقات التداول 🟢", callback_data="view_trades")
    btn_vip = types.InlineKeyboardButton("🟡 👑 قسم الـ VIP 🟡", callback_data="view_vip")
    btn_support = types.InlineKeyboardButton("🔵 📞 بوابة الإيداع 🔵", callback_data="view_support")
    btn_contact = types.InlineKeyboardButton("🟠 👨‍💻 تواصل مع الدعم 🟠", url=f"https://t.me/{SUPPORT_USERNAME.replace('@', '')}")
    btn_channel = types.InlineKeyboardButton("🟣 📢 قناة تداول VIP 🟣", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}")
    
    markup.add(btn_trade, btn_vip)
    markup.add(btn_support, btn_contact)
    markup.add(btn_channel)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        welcome_text = (
            f"👋 أهلاً بك في بوت التداول والاستثمار المعتمد!\n\n"
            f"✨ **{ZAINAB_RIGHTS}** ✨\n\n"
            f"يرجى التحكم بالبوت بالكامل عبر الأزرار الشفافة الملونة بالأسفل 👇:"
        )
        bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=main_inline_keyboard())
    except Exception as e:
        print(f"Error in start: {e}")

# معالجة الضغط على الأزرار الشفافة
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    try:
        # العودة للقائمة الرئيسية
        if call.data == "main_menu":
            welcome_text = (
                f"👋 أهلاً بك في بوت التداول والاستثمار المعتمد!\n\n"
                f"✨ **{ZAINAB_RIGHTS}** ✨\n\n"
                f"يرجى التحكم بالبوت بالكامل عبر الأزرار الشفافة الملونة بالأسفل 👇:"
            )
            bot.edit_message_text(welcome_text, chat_id, message_id, parse_mode="Markdown", reply_markup=main_inline_keyboard())

        # عرض صفقات التداول
        elif call.data == "view_trades":
            trade_text = (
                f"🎯 **قائمة الصفقات المتاحة - {ZAINAB_RIGHTS}**\n\n"
                "💎 **قائمة استثمار عملة TON:**\n"
                "🔹 ادخل بـ 5 TON تربح 10 TON\n"
                "🔹 ادخل بـ 10 TON تربح 15 TON\n"
                "🔹 ادخل بـ 15 TON تربح 25 TON\n"
                "🔹 ادخل بـ 25 TON تربح 50 TON (🔥 سعر متضاعف x2)\n\n"
                "⭐️ **قائمة استثمار نجوم التليجرام:**\n"
                "🔸 ادفع 100 نجمة تربح 250 نجمة\n"
                "🔸 ادفع 250 نجمة تربح 500 نجمة\n"
                "🔸 ادفع 500 نجمة تربح 1000 نجمة\n"
                "🔸 ادفع 1000 نجمة تربح 2000 نجمة"
            )
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn_asia = types.InlineKeyboardButton("🔴 💳 دفع آسيا سيل 🔴", callback_data="pay_asia")
            btn_ton = types.InlineKeyboardButton("🔵 💎 دفع TON 🔵", callback_data="pay_ton")
            btn_stars = types.InlineKeyboardButton("🟡 ⭐️ دفع نجوم (تلقائي) 🟡", callback_data="pay_stars_menu")
            btn_back = types.InlineKeyboardButton("⚫️ 🔙 عودة للخلف ⚫️", callback_data="main_menu")
            markup.add(btn_asia, btn_ton)
            markup.add(btn_stars)
            markup.add(btn_back)
            bot.edit_message_text(trade_text, chat_id, message_id, parse_mode="Markdown", reply_markup=markup)

        # قائمة دفع النجوم التلقائية
        elif call.data == "pay_stars_menu":
            stars_text = f"⭐️ **قسم دفع النجوم التلقائي - {ZAINAB_RIGHTS}**\n\nاختر الصفقة التي تريد دخولها بالنجوم وسيتم الدفع فوراً عبر التليجرام:"
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("🟢 ⭐️ 100 نجمة لتـربح 250 🟢", callback_data="star_100"),
                types.InlineKeyboardButton("🔵 ⭐️ 250 نجمة لتـربح 500 🔵", callback_data="star_250"),
                types.InlineKeyboardButton("🟡 ⭐️ 500 نجمة لتـربح 1000 🟡", callback_data="star_500"),
                types.InlineKeyboardButton("🟠 ⭐️ 1000 نجمة لتـربح 2000 🟠", callback_data="star_1000"),
                types.InlineKeyboardButton("⚫️ 🔙 عودة لصفقات التداول ⚫️", callback_data="view_trades")
            )
            bot.edit_message_text(stars_text, chat_id, message_id, parse_mode="Markdown", reply_markup=markup)

        # تنفيذ فواتير النجوم
        elif call.data.startswith("star_"):
            amount = int(call.data.split("_")[1])
            prices = {100: 250, 250: 500, 500: 1000, 1000: 2000}
            win_amount = prices[amount]
            
            bot.send_invoice(
                chat_id,
                title=f"صفقة {amount} نجمة",
                description=f"دخول صفقة بـ {amount} نجمة لتربح {win_amount} نجمة بحقوق المستثمر زينب.",
                invoice_payload=f"payload_star_{amount}",
                provider_token="", 
                currency="XTR",
                prices=[types.LabeledPrice(label=f"صفقة {amount} نجمة", amount=amount)]
            )

        # عرض قسم VIP
        elif call.data == "view_vip":
            vip_text = (
                f"👑 **👑 قسم الـ VIP الخاص بالمستثمر زينب 👑**\n\n"
                "هذا القسم مخصص للمستثمرين وأصحاب الصفقات الكبرى لتوصيات تداول مباشرة ومضمونة بنسبة عالية جداً.\n\n"
                "اضغط على الزر الشفاف بالأسفل للانتقال إلى القناة الرسمية للـ VIP ومتابعة الأرباح أولاً بأول."
            )
            markup = types.InlineKeyboardMarkup()
            btn_channel = types.InlineKeyboardButton("🟣 📢 دخول قناة VIP 🟣", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}")
            btn_back = types.InlineKeyboardButton("⚫️ 🔙 عودة للخلف ⚫️", callback_data="main_menu")
            markup.add(btn_channel)
            markup.add(btn_back)
            bot.edit_message_text(vip_text, chat_id, message_id, reply_markup=markup)

        # عرض قسم الدعم والإيداع وطرق الدفع
        elif call.data == "view_support":
            support_text = (
                f"🏦 **بوابة الإيداع والتحويل - {ZAINAB_RIGHTS}**\n\n"
                f"📱 **رقم تحويل آسيا سيل المعتمد:**\n`{ASIA_NUMBER}`\n\n"
                f"💎 **عنوان محفظة TON المعتمدة:**\n`{TON_WALLET}`\n\n"
                "⚠️ بعد إتمام التحويل يدوياً (آسيا سيل أو TON)، اضغط على زر التأكيد الشفاف بالأسفل لإرسال الإيصال."
            )
            markup = types.InlineKeyboardMarkup()
            btn_confirm = types.InlineKeyboardButton("🟢 ✅ تأكيد التحويل وإرسال الإيصال 🟢", callback_data="confirm_payment")
            btn_contact = types.InlineKeyboardButton("🟠 👨‍💻 مراسلة الدعم الفني مباشر 🟠", url=f"https://t.me/{SUPPORT_USERNAME.replace('@', '')}")
            btn_back = types.InlineKeyboardButton("⚫️ 🔙 عودة للخلف ⚫️", callback_data="main_menu")
            markup.add(btn_confirm)
            markup.add(btn_contact)
            markup.add(btn_back)
            bot.edit_message_text(support_text, chat_id, message_id, parse_mode="Markdown", reply_markup=markup)

        elif call.data == "pay_asia":
            bot.send_message(chat_id, f"📱 يرجى تحويل الرصيد إلى رقم الآسيا سيل المعتمد التالي:\n`{ASIA_NUMBER}`")
        elif call.data == "pay_ton":
            bot.send_message(chat_id, f"💎 يرجى تحويل العملة إلى عنوان المحفظة المعتمد التالي:\n`{TON_WALLET}`")
        elif call.data == "confirm_payment":
            msg = bot.send_message(chat_id, "✍️ أرسل الآن صورة إيصال التحويل (الوصل) أو لقطة الشاشة لإثبات الدفع:")
            bot.register_next_step_handler(msg, process_payment_proof)
            
    except Exception as e:
        print(f"Error in inline: {e}")

# تأكيد التحويلات اليدوية وإرسالها لك
def process_payment_proof(message):
    try:
        user_info = (
            f"🔔 **إشعار دفع يدوي جديد!**\n\n"
            f"👤 **المرسل:** {message.from_user.first_name}\n"
            f"🆔 **الآيدي:** `{message.from_user.id}`\n"
            f"🏷️ **اليوزر:** @{message.from_user.username}\n"
        )
        bot.send_message(ADMIN_ID, user_info, parse_mode="Markdown")
        
        if message.content_type == 'photo':
            bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
            bot.send_message(ADMIN_ID, "👆 الإيصال أعلاه بانتظار موافقتك لتفعيل الصفقة.")
        else:
            bot.send_message(ADMIN_ID, f"📝 نص الإثبات المرسل:\n\n{message.text}")
            
        bot.send_message(message.chat.id, f"✅ تم إرسال إثباتك بنجاح إلى إدارة المستثمر زينب. جاري التدقيق والتحقق فوراً.")
    except Exception as e:
        print(f"Error in payment proof: {e}")

# معالجة دفع النجوم التلقائي بنجاح
@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    try:
        payload = message.successful_payment.invoice_payload
        amount = message.successful_payment.total_amount
        
        user_text = (
            f"🎉 **تم الدفع بالنجوم بنجاح!**\n\n"
            f"لقد دخلت صفقة بـ {amount} نجمة بنجاح عبر نظام المستثمر زينب التلقائي.\n"
            f"سيتم تحويل أرباحك إلى حسابك فوراً!"
        )
        bot.send_message(message.chat.id, user_text, parse_mode="Markdown")
        
        admin_text = (
            f"💰 **إشعار دفع تلقائي بالنجوم!**\n\n"
            f"👤 **المستخدم:** {message.from_user.first_name}\n"
            f"🆔 **الآيدي:** `{message.from_user.id}`\n"
            f"⭐️ **المبلغ المدفوع:** {amount} نجمة\n"
            f"نوع الصفقة: {payload}"
        )
        bot.send_message(ADMIN_ID, admin_text, parse_mode="Markdown")
    except Exception as e:
        print(f"Error in successful payment: {e}")

# تشغيل البوت
if __name__ == "__main__":
    print("🤖 البوت يعمل الآن بنظام الأزرار الشفافة والدعم الفني المباشر...")
    while True:
        try:
            bot.infinity_polling(timeout=15, long_polling_timeout=10)
        except Exception as e:
            print(f"🔄 إعادة اتصال تلقائي... السبب: {e}")
            time.sleep(5)
