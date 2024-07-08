from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters

# /airdrop komutu için bir işlev oluşturun
async def airdrop(update: Update, context: CallbackContext) -> None:
    photo_url = "https://public.bnbstatic.com/static/academy/uploads/8456ba0fa9e64f0992d5f7b549af3597.jpg"  # Fotoğraf URL'si

    # Buton listesi oluşturun
    keyboard = [
         [
            InlineKeyboardButton("🐸 ArenaGames 🐸", url="https://t.me/Arenavsbot?start=ref_kEyQiFnQZT99aZWnjGz4FB")
        ],
         [
            InlineKeyboardButton("🐔 Chick Coop 🐔", url="https://t.me/chickcoopofficial_bot/chickcoop?startapp=ref_1543996252"),
            InlineKeyboardButton("🐰 White Bunny 🐰", url="https://t.me/whitebunnywtf_bot?start=ref66687ca7e4ba0b1915e15222")
        ],
        [
            InlineKeyboardButton("🚀 Time Farm 🚀 ", url="https://t.me/TimeFarmCryptoBot?start=5vnf1clN6dVmErek"),
            InlineKeyboardButton("💰 Blum 💰", url="https://t.me/BlumCryptoBot/app?startapp=ref_wni7bsd2Iz")
        ],
        [
            InlineKeyboardButton("Pixel", url="https://t.me/pixelversexyzbot?start=1543996252"),
        InlineKeyboardButton("YesCoin", url="https://t.me/theYescoin_bot/Yescoin?startapp=D8UYWP")
        ],
        [
            InlineKeyboardButton("Hamster", url="https://t.me/hAmster_kombat_bot/start?startapp=kentId1543996252"),
            InlineKeyboardButton("Cex.IO", url="https://t.me/cexio_tap_bot?start=1716295512797457")
        ],
        [

            InlineKeyboardButton("W-Coin", url="https://t.me/wcoin_tapbot?start=NzEzMTczMDMwOA=="),
            InlineKeyboardButton("Cat Miner", url="https://t.me/catgoldminerbot?start=club_1002178183206_7131730308")
        ],
        [
            InlineKeyboardButton("MemeFi", url="https://t.me/memefi_coin_bot?start=r_bce937eea8"),
            InlineKeyboardButton("Catizen", url="https://t.me/catizenbot/gameapp?startapp=r_2811_2375654")
        ],

    ]
    photo_caption = "Merhaba arkadaşlar, hala kayıt olmadıysanız aşağıdaki linklerden hemen kayıt olabilirsiniz."

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=photo_caption, reply_markup=InlineKeyboardMarkup(keyboard))


def main() -> None:
    # Telegram botunuzun token'ını buraya girin
    TOKEN = '7301705910:AAEpn0c_dCL2Sd_57aSGVwik50DnMhWDlps'

    # Botu başlatın
    application = ApplicationBuilder().token(TOKEN).build()

    # /airdrop komutunu yönetin
    application.add_handler(CommandHandler("airdrop", airdrop))

    # Kanal mesajlarını işlemek için bir handler ekleyin
    application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.CHANNEL, airdrop))

    # Botu çalıştırın
    application.run_polling()

if __name__ == '__main__':
    main()