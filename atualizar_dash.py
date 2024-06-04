import pyautogui as bot
print(bot.position())

print(bot.size())

i = 0
while i <= 96:
    print(bot.position())
    bot.click(x=1303, y=1038)
    bot.sleep(2)
    bot.click(x=968, y=115)
    bot.sleep(15)
    bot.click(x=1523, y=110)
    bot.sleep(20)
    bot.click(x=1046, y=568)
    bot.sleep(5)
    bot.click(x=685 , y=374)
    bot.sleep(2)
    bot.click(x=1118, y=812)
    bot.sleep(10)
    bot.click(x=1022, y=675)
    bot.sleep(20)
    bot.click(x=1186, y=690)
    bot.sleep(2)
    bot.click(x=1291, y=1040)
    bot.sleep(700)
i += 1



#bot.sleep(900)
