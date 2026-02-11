"""
DarkSide Telegram Bot - Webhook Version
Vercel serverless deployment için optimize edilmiş
"""

import os
import json
from http.server import BaseHTTPRequestHandler
from groq import Groq
from telegram import Update, Bot
from telegram.ext import Application

# Environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET', 'darkside-secret-key')

# Groq client
groq_client = Groq(api_key=GROQ_API_KEY)

# In-memory conversation storage (Vercel her request'te yeni instance oluşturur)
# Gerçek production'da Redis/Database kullanılmalı, ama basit kullanım için yeterli
conversations = {}

def get_ai_response(user_id: int, user_message: str) -> str:
    """Groq AI'dan cevap al"""
    
    # Kullanıcının geçmişini al veya yeni oluştur
    if user_id not in conversations:
        conversations[user_id] = []
    
    # Mesajı ekle
    conversations[user_id].append({
        "role": "user",
        "content": user_message
    })
    
    # Son 10 mesajı tut (memory limiti için)
    if len(conversations[user_id]) > 20:
        conversations[user_id] = conversations[user_id][-20:]
    
    try:
        # Groq API call
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Sen DarkSide adında akıllı, yardımsever ve eğlenceli bir AI asistansın. Türkçe konuşuyorsun. Kullanıcıya doğal ve samimi bir şekilde yanıt veriyorsun. Kısa ve öz cevaplar vermeye özen gösteriyorsun ama gerektiğinde detaylı açıklama da yapabiliyorsun."
                },
                *conversations[user_id]
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False
        )
        
        ai_response = chat_completion.choices[0].message.content
        
        # AI cevabını geçmişe ekle
        conversations[user_id].append({
            "role": "assistant",
            "content": ai_response
        })
        
        return ai_response
        
    except Exception as e:
        return f"⚠️ Bir hata oluştu: {str(e)}"

async def process_update(update_data: dict):
    """Telegram update'ini işle"""
    
    # Update objesini oluştur
    update = Update.de_json(update_data, Bot(TELEGRAM_BOT_TOKEN))
    
    if not update.message:
        return {"status": "ok", "message": "No message"}
    
    message = update.message
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    
    # Komutları işle
    if message.text and message.text.startswith('/'):
        command = message.text.split()[0]
        
        if command == '/start':
            response = f"""
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
        
        elif command == '/help':
            response = """
📚 **DarkSide AI - Yardım**

**Nasıl kullanılır?**
Sadece bana mesaj yaz, ben yanıtlarım!

**Örnekler:**
• "Python'da liste nasıl oluşturulur?"
• "Bana bir şiir yaz"
• "Bugün ne yapsam?"

**Komutlar:**
/start - Başlangıç mesajı
/clear - Konuşma geçmişini temizle
/help - Bu mesaj

**Not:** Ben Groq API kullanıyorum (Llama 3).
Sadece mesaj gelince çalışırım (serverless)! 🧠
"""
        
        elif command == '/clear':
            if user_id in conversations:
                conversations[user_id] = []
            response = "✅ Sohbet geçmişini temizledim! Yeni bir konuşma başlayalım."
        
        else:
            response = "❓ Bilinmeyen komut. /help yazarak komutları görebilirsin."
    
    # Normal mesaj - AI'a gönder
    else:
        if message.text:
            response = get_ai_response(user_id, message.text)
        else:
            response = "📝 Sadece text mesajları işleyebiliyorum şu an."
    
    # Cevabı gönder
    bot = Bot(TELEGRAM_BOT_TOKEN)
    await bot.send_message(
        chat_id=message.chat_id,
        text=response,
        parse_mode='Markdown'
    )
    
    return {"status": "ok"}

class handler(BaseHTTPRequestHandler):
    """Vercel serverless function handler"""
    
    def do_POST(self):
        """POST request'leri işle (Telegram webhook)"""
        
        # Content length al
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Body'yi oku
        post_data = self.rfile.read(content_length)
        
        try:
            # JSON parse et
            update_data = json.loads(post_data.decode('utf-8'))
            
            # Update'i işle (async)
            import asyncio
            result = asyncio.run(process_update(update_data))
            
            # Response gönder
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            
        except Exception as e:
            # Hata durumunda
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {"status": "error", "message": str(e)}
            self.wfile.write(json.dumps(error_response).encode())
    
    def do_GET(self):
        """GET request'leri işle (healthcheck)"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"status": "alive", "bot": "DarkSide AI"}
        self.wfile.write(json.dumps(response).encode())
