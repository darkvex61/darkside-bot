# 🌑 DarkSide Telegram Bot

**DarkSide D1** (@darsidex1_bot) - Groq API ile çalışan akıllı Telegram botu.

---

## 🚀 Özellikler

- ✅ Akıllı AI sohbet (Llama 3.3 70B model)
- ✅ Konuşma geçmişi hafızası
- ✅ Türkçe desteği
- ✅ Kod yazma & açıklama
- ✅ Yaratıcı içerik üretimi
- ✅ Tamamen ücretsiz (Groq API)

---

## 📋 Gereksinimler

- Python 3.9+
- Telegram hesabı
- Groq API key (ücretsiz)

---

## 🛠️ Kurulum

### 1️⃣ Repository'yi Klonla

```bash
git clone https://github.com/darkvex61/darkside-bot.git
cd darkside-bot
```

### 2️⃣ Virtual Environment Oluştur (Opsiyonel ama Tavsiye)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

### 3️⃣ Gerekli Kütüphaneleri Yükle

```bash
pip install -r requirements.txt
```

### 4️⃣ .env Dosyası Oluştur

`.env.example` dosyasını `.env` olarak kopyala:

```bash
cp .env.example .env
```

Sonra `.env` dosyasını aç ve API key'lerini gir:

```env
TELEGRAM_BOT_TOKEN=7123456789:AAHdF3qWxYz...
GROQ_API_KEY=gsk_aBcDeFgHiJkLmNoPqRs...
```

### 5️⃣ Bot'u Çalıştır

```bash
python bot.py
```

Bot başarıyla başladıysa şu mesajı göreceksin:
```
🌑 DarkSide Bot başlatılıyor...
```

---

## 🔑 API Key Nasıl Alınır?

### Telegram Bot Token

1. Telegram'da **@BotFather** ara
2. `/newbot` komutunu gönder
3. Bot adını belirle (örn: DarkSide D1)
4. Username belirle (örn: darsidex1_bot)
5. Token'ı kopyala ve `.env` dosyasına yapıştır

### Groq API Key

1. https://console.groq.com/ adresine git
2. Kaydol (ücretsiz)
3. **API Keys** → **Create API Key** bas
4. Key'i kopyala ve `.env` dosyasına yapıştır

---

## 💻 PC'de Çalıştırma

### Windows:

```bash
# Terminal aç (PowerShell veya CMD)
cd darkside-bot
python bot.py
```

### Linux/Mac:

```bash
cd darkside-bot
python3 bot.py
```

**Not:** Bot çalışırken terminal penceresini kapatma! Kapattığında bot durur.

---

## ☁️ Railway'de Deploy (24/7 Çalışsın)

### 1. Railway'e Kaydol

https://railway.app/ → GitHub ile giriş yap

### 2. New Project

- **Deploy from GitHub repo** seç
- Bu repository'yi seç: `darkvex61/darkside-bot`

### 3. Environment Variables Ekle

Railway dashboard'da:
- **Variables** sekmesine git
- Şunları ekle:
  ```
  TELEGRAM_BOT_TOKEN = 7123456789:AAHdF3qWxYz...
  GROQ_API_KEY = gsk_aBcDeFgHiJkLmNoPqRs...
  ```

### 4. Deploy!

Railway otomatik olarak deploy edecek. 2-3 dakika sonra bot aktif olur!

---

## 📱 Kullanım

Bot'u Telegram'da aç: **@darsidex1_bot**

### Komutlar:

- `/start` - Bot'u başlat
- `/help` - Yardım mesajı
- `/clear` - Konuşma geçmişini temizle

### Örnekler:

```
Sen: Python'da liste nasıl oluşturulur?
Bot: [Detaylı açıklama + kod örneği]

Sen: Bana bir şiir yaz
Bot: [Şiir yazar]

Sen: Bugün ne yapsam?
Bot: [Öneri verir]
```

---

## 🔧 Sorun Giderme

### "TELEGRAM_BOT_TOKEN bulunamadı" hatası

- `.env` dosyasının doğru konumda olduğundan emin ol
- `.env` dosyasındaki key'lerin doğru olduğunu kontrol et

### Bot yanıt vermiyor

- Internet bağlantını kontrol et
- Groq API limitini kontrol et (günde 14,400 mesaj)
- Terminal'de hata mesajlarını oku

### Railway'de bot çalışmıyor

- Environment variables'ı kontrol et
- Logs sekmesinden hataları oku
- Deploy durumunu kontrol et (yeşil tick olmalı)

---

## 📊 Limitler

- **Groq API:** 14,400 mesaj/gün (ücretsiz)
- **Railway:** 500 saat/ay (ücretsiz)
- **Telegram:** Limit yok

---

## 🤝 Katkıda Bulun

Pull request'ler kabul edilir! Özellik eklemek veya hata düzeltmek isterseniz:

1. Fork yap
2. Feature branch oluştur
3. Commit yap
4. Push yap
5. Pull request aç

---

## 📝 Lisans

Bu proje kişisel kullanım içindir.

---

## 👤 Geliştirici

**@darkvex61** - DarkSide D1 Bot

---

## 🙏 Teşekkürler

- Groq API (ücretsiz AI)
- python-telegram-bot library
- Railway (hosting)

---

**Bot'un tadını çıkar! 💀**
