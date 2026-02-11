import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

# Logging ayarları
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment variables'dan API key'leri al
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Groq client'ı başlat
groq_client = Groq(api_key=GROQ_API_KEY)

# Her kullanıcı için sohbet geçmişi (basit hafıza)
user_conversations = {}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Bot başlatıldığında çalışır"""
    user_name = update.effective_user.first_name
    welcome_message = f"""
🌑 **DarkSide AI Aktif!**

Selam {user_name}! Ben DarkSide, senin kişisel AI asistanınım.

**Yapabileceklerim:**
• Sohbet edebilirim
• Sorularını yanıtlarım
• Kod yazabilirim
• Yaratıcı içerik üretebilirim
• Analiz yapabilirim

Sadece mesaj at, ben hallederim! 💀

**Komutlar:**
/start - Bu mesajı göster
/clear - Sohbet geçmişini temizle
/help - Yardım
"""
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yardım komutu"""
    help_text = """
📚 **DarkSide AI - Yardım**

**Nasıl kullanılır?**
Sadece bana mesaj yaz, ben yanıtlarım!

**Örnekler:**
• "Python'da liste nasıl oluşturulur?"
• "Bana bir şiir yaz"
• "Bugün ne yapsam?"
• "React ile component nasıl yazılır?"

**Komutlar:**
/start - Başlangıç mesajı
/clear - Konuşma geçmişini temizle
/help - Bu mesaj

**Not:** Ben Groq API kullanıyorum (Llama 3 modeli).
Güncel olayları bilmiyorum ama akıllı sohbet edebilirim! 🧠
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sohbet geçmişini temizle"""
    user_id = update.effective_user.id
    if user_id in user_conversations:
        user_conversations[user_id] = []
    await update.message.reply_text("✅ Sohbet geçmişini temizledim! Yeni bir konuşma başlayalım.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kullanıcı mesajlarını işle ve Groq'a gönder"""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Kullanıcı ilk defa yazıyorsa, yeni liste oluştur
    if user_id not in user_conversations:
        user_conversations[user_id] = []
    
    # Kullanıcı mesajını geçmişe ekle
    user_conversations[user_id].append({
        "role": "user",
        "content": user_message
    })
    
    # Geçmiş çok uzunsa (20 mesajdan fazla), eski mesajları sil
    if len(user_conversations[user_id]) > 20:
        user_conversations[user_id] = user_conversations[user_id][-20:]
    
    try:
        # "Yazıyor..." göstergesi
        await update.message.chat.send_action("typing")
        
        # Groq API'ye mesaj gönder
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Sen DarkSide adında akıllı, yardımsever ve eğlenceli bir AI asistansın. Türkçe konuşuyorsun. Kullanıcıya doğal ve samimi bir şekilde yanıt veriyorsun. Kısa ve öz cevaplar vermeye özen gösteriyorsun ama gerektiğinde detaylı açıklama da yapabiliyorsun."
                },
                *user_conversations[user_id]
            ],
            model="llama-3.3-70b-versatile",  # En iyi ücretsiz model
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        
        # AI yanıtını al
        ai_response = chat_completion.choices[0].message.content
        
        # AI yanıtını geçmişe ekle
        user_conversations[user_id].append({
            "role": "assistant",
            "content": ai_response
        })
        
        # Yanıtı kullanıcıya gönder
        await update.message.reply_text(ai_response)
        
    except Exception as e:
        logger.error(f"Hata oluştu: {e}")
        error_message = f"⚠️ Bir hata oluştu: {str(e)}\n\nAPI key'lerini kontrol et veya daha sonra tekrar dene."
        await update.message.reply_text(error_message)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Hata yakalandığında çalışır"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Bot'u başlat"""
    # Token kontrolü
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN bulunamadı! Environment variable'ı ayarla.")
        return
    
    if not GROQ_API_KEY:
        logger.error("GROQ_API_KEY bulunamadı! Environment variable'ı ayarla.")
        return
    
    # Application oluştur
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Komut handler'ları ekle
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_command))
    
    # Mesaj handler'ı ekle (tüm text mesajlar)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Hata handler'ı ekle
    application.add_error_handler(error_handler)
    
    # Bot'u başlat
    logger.info("🌑 DarkSide Bot başlatılıyor...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
