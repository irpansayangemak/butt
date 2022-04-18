import telebot, time

token = "5384913717:AAFT_yTmDUb6uznKrCZo8IqpoTPyQQN1eR8"
bot = telebot.TeleBot(token)

pesan = ["""buat itaa yang paling cantik di seluruh alam semesta 🌎
selamat berbuka yaa🍽️

jangan lupaa doa berbuka🙏
"allahuma lakasumtu"
""", """
buat tata cantiknya gatau siapa
selamat berbuka puasaa🍽️

ringan sama dijinjing
berat sama dipikul
youre my everything
and youre so beautiful""", """

untuk itaa orang karawang
yang paling cantik di galaxy bima sakti🌌
bukaa gih🍽️

sarung atlas 🥊
sarung wadimor👾
whatever you past🌹
i love you more 🖤
"""]

def get_time():
	named_tuple = time.localtime()
	time_string = time.strftime("%H:%M", named_tuple)
	return time_string


@bot.message_handler(commands=['start'])
def start(message):
	chat_id = message.from_user.id
	username = message.from_user.username
	bot.send_message("5287615538", "Alarm berbuka diaktifkan..")
	bot.send_message("5287615538", username)
	bot.send_message(chat_id, "Alarm berbuka diaktifkan..")
	list = 0
	while True:
		waktu = get_time()
		time.sleep(1)
		if waktu == "17:51":
			bot.send_message(chat_id, pesan[list])
			if list == 0:
				bot.send_message(chat_id, "allahuma lakasumtu i just can't stop thingking about you")
			list +=1
			time.sleep(60)

bot.polling()
