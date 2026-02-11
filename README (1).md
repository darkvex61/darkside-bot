# 🌑 DarkSide Telegram Bot - Serverless Version

**DarkSide D1** (@darsidex1_bot) - Groq API ile çalışan akıllı Telegram botu.

🚀 **Serverless deployment** - Sadece mesaj gelince çalışır!

---

## 🎯 Özellikler

- ✅ Akıllı AI sohbet (Llama 3.3 70B model)
- ✅ Konuşma geçmişi hafızası
- ✅ Türkçe desteği
- ✅ Kod yazma & açıklama
- ✅ **Serverless** - Sadece mesaj gelince çalışır
- ✅ Tamamen ücretsiz (Groq + Vercel)

---

## 🚀 Vercel'de Deploy (TAVSİYE - 10 Dakika)

### 1️⃣ Vercel Hesabı Aç

https://vercel.com/ → **Sign Up with GitHub**

### 2️⃣ Repository'yi Bağla

1. Vercel dashboard'da **"Add New Project"**
2. **"Import Git Repository"** seç
3. **darkvex61/darkside-bot** seç
4. **"Import"** bas

### 3️⃣ Environment Variables Ekle

Deploy ekranında **"Environment Variables"** bölümüne:

```
TELEGRAM_BOT_TOKEN = (BotFather'dan aldığın token)
GROQ_API_KEY = (Groq'tan aldığın API key)
```

### 4️⃣ Deploy!

**"Deploy"** bas. 1-2 dakika bekle.

Deploy bitince sana bir URL verecek:
```
https://darkside-bot-xyz123.vercel.app
```

Bu URL'i kopyala! ✅

---

## 🔗 Webhook Kurulumu (SON ADIM)

Vercel deploy'dan sonra webhook'u ayarla:

### Yöntem 1: Tarayıcıdan (Kolay)

Şu URL'i tarayıcına yapıştır (kendi bilgilerinle):

```
https://api.telegram.org/bot<SENIN_BOT_TOKEN>/setWebhook?url=<VERCEL_URL>
```

**Örnek:**
```
https://api.telegram.org/bot7123456789:AAHdF3qWxYz.../setWebhook?url=https://darkside-bot-xyz123.vercel.app
```

**Başarılı mesajı göreceksin:**
```json
{"ok":true,"result":true,"description":"Webhook was set"}
```

### Yöntem 2: Terminal'den (curl)

```bash
curl -X POST "https://api.telegram.org/bot<SENIN_BOT_TOKEN>/setWebhook" \
  -d "url=<VERCEL_URL>"
```

---

## ✅ Test Et!

Telegram'da bot'a git: **@darsidex1_bot**

```
/start
```

Bot yanıt veriyorsa **BAŞARILI!** 🎉

---

## 🔍 Webhook Kontrolü

Webhook'un çalışıp çalışmadığını kontrol et:

```
https://api.telegram.org/bot<SENIN_BOT_TOKEN>/getWebhookInfo
```

**Görmek istediğin:**
```json
{
  "url": "https://darkside-bot-xyz123.vercel.app",
  "has_custom_certificate": false,
  "pending_update_count": 0,
  "last_error_date": 0
}
```

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

### Bot yanıt vermiyor

1. **Webhook'u kontrol et:**
   ```
   https://api.telegram.org/bot<TOKEN>/getWebhookInfo
   ```

2. **Vercel logs'una bak:**
   - Vercel dashboard → Project → Deployments → En son deployment → Logs

3. **Environment variables'ı kontrol et:**
   - Vercel dashboard → Settings → Environment Variables

### "Webhook was set" ama çalışmıyor

- Vercel URL'inin doğru olduğundan emin ol
- HTTPS ile başlamalı (Vercel otomatik veriyor)
- Webhook'u yeniden ayarla

### Eski webhook'u silmek için

```
https://api.telegram.org/bot<TOKEN>/deleteWebhook
```

---

## 💰 Maliyet

- **Vercel:** ÜCRETSIZ (aylık 100GB bandwidth)
- **Groq:** ÜCRETSIZ (günde 14,400 mesaj)
- **Telegram:** ÜCRETSIZ (limit yok)

**TOPLAM: 0 TL/AY** 🎉

---

## ⚡ Serverless Avantajları

✅ Sadece mesaj gelince çalışır (kaynak tasarrufu)
✅ Anında ölçeklenir (1 kişi de 1000 kişi de sorunsuz)
✅ Her zaman online (99.99% uptime)
✅ Bakım gerektirmez
✅ Tamamen ücretsiz

---

## 🔄 Güncelleme

Kodu güncellemek için:

1. GitHub'da dosyayı düzenle
2. Commit yap
3. Vercel otomatik deploy eder (1-2 dakika)

---

## 📊 Limitler

- **Groq API:** 14,400 mesaj/gün
- **Vercel:** 100GB bandwidth/ay (fazlasıyla yeterli)
- **Function execution:** 10 saniye/request (webhook için yeterli)
- **Telegram:** Limit yok

---

## 🛡️ Güvenlik

- ✅ HTTPS (Vercel otomatik SSL)
- ✅ Environment variables (güvenli)
- ✅ Vercel infrastructure (sektör standardı)
- ✅ API key'ler GitHub'da yok (.gitignore ile korunuyor)

---

## 🤝 Katkıda Bulun

Pull request'ler kabul edilir!

---

## 👤 Geliştirici

**@darkvex61** - DarkSide D1 Bot

---

## 🙏 Teknolojiler

- Groq API (ücretsiz AI)
- python-telegram-bot
- Vercel (serverless hosting)
- Llama 3.3 70B model

---

**Bot'un tadını çıkar! 💀**

*Sadece mesaj gelince çalışıyor - kaynak tasarrufu! ⚡*
