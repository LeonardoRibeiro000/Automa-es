import pyautogui as bot
print(bot.position())

print(bot.size())


i = 0
while i <= 96:#
#---------abrir programa-----------------------------------
    #print(bot.position())
    bot.click(x=1190, y=1050)
    
    print("abriu programa")
    bot.sleep(10)
    
#--------- CSV --------------------------------------------
    #print(bot.position())
    bot.click(x=375, y=626)
    print("clicou no csv")
    bot.sleep(2)

#--------salvar--------------------------------------------
    #print(bot.position())
    bot.write("gestao_leitos", interval=0.25)
    bot.sleep(5)
    bot.press("Enter")
    #bot.click(x=1080, y=662)
    print("salvou o arquivo")
    bot.sleep(15)

#----------OK----------------------------------------------
    #print(bot.position())
    
    bot.press("Enter")
    print("OK")
    #bot.click(x=1032, y=610)
    bot.sleep(1)
    bot.click(x=1917, y=1043)
    print("Desktop")
    bot.sleep(2)
    #bot.alert("Extração concluída!")
    #bot.press("Enter")

    bot.click(x=457, y=1058)
    print("Abriu documentos")
    bot.sleep(2)

    bot.click(x=338, y=287)
    bot.hotkey("ctrl","c")
    print("copiou relatório gerado")

    bot.sleep(2)
    bot.click(x=114, y=416)
    print("abriu onedrive")

    bot.sleep(2)
    bot.click(x=278, y=263)

    bot.sleep(1)
    bot.press("Enter")
    print("abriu a pasta PWBI")


    bot.click(x=277, y=376)
    bot.sleep(2)
    bot.press("Enter")
    print("abriu a pasta hotelaria")
    bot.sleep(2)

    bot.hotkey("ctrl", "v")
    print("salvou o arquivo")
    bot.sleep(2)

    bot.click(x=825, y=426)
    print("substituiu o arquivo no onedrive")
    bot.sleep(5)

    bot.click(x=106, y=515)
    print("voltou para a pasta documento")

    bot.sleep(2)
    bot.click(x=1915, y=1051)
    print("desktop")

    #Espera de 15 minutos para iniciar
    bot.sleep(600)

i += 1

