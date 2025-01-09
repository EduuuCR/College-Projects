import os
import random
import math
import PySimpleGUI as sg

path = os.getcwd()

f = open(path + r"\questions.txt", "r")
flines = f.readlines()

randomNums = []

while len(randomNums) < 3:
    num = random.randint(0,16)
    if num not in randomNums:
        randomNums.append(num)

questions = []

for x in randomNums:
    questions.append(flines[x].rstrip("\n"))

def encrypt(word, stage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if stage == 0: #Caesar Stage

        difficulty = random.randint(0,3)

        if difficulty == 0:
            key1 = random.randint(65,89) 
            offset = key1 - 64
            word1 = ''.join(( chr( 97 + ( ord(l) - 97 + offset ) % 26) for l in word))
            cAlphabet = ''.join(( chr( 97 + ( ord(letter) - 97 + offset ) % 26) for letter in alphabet))
            key = chr(key1) 

        elif difficulty == 1:
            key1 = random.randint(97,121) 
            offset = (key1 - 96) * -1
            word1 = ''.join(( chr( 97 + ( ord(l) - 97 + offset ) % 26) for l in word))
            cAlphabet = ''.join(( chr( 97 + ( ord(letter) - 97 + offset ) % 26) for letter in alphabet))
            key = chr(key1) 

        else:
            key1 = random.randint(65,90) 
            key2 = random.randint(97,122)

            if key1 == key2:
                while key1 != key2:
                    key2 = random.randint(97,122)

            offset = (key1 - 64) + ((key2 - 96) * -1)

            word1 = ''.join(( chr( 97 + ( ord(l) - 97 + offset ) % 26) for l in word))

            cAlphabet = ''.join(( chr( 97 + ( ord(letter) - 97 + offset ) % 26) for letter in alphabet))
            
            key = chr(key1) + chr(key2)

        for x in range(0, len(alphabet)):
            if(alphabet[x] in word):
                alphabet = alphabet[:x] + alphabet[x].upper() + alphabet[(x+1):]
                cAlphabet = cAlphabet[:x] + cAlphabet[x].upper() + cAlphabet[(x+1):]

        alphabet = alphabet.replace("", " ")[1: -1]
        cAlphabet = cAlphabet.replace("", " ")[1: -1]

        return [word1,key,alphabet, cAlphabet]


    elif stage == 1: #Circle Stage

        key1 = random.randint(65,90) 
        while math.floor(((key1 - 64) * (key1 - 64) * 3.14) % 26) == 26:
            key1 = random.randint(65,90) 

        offset = (key1 - 64) * (key1 - 64) * 3.14
        offset = math.floor(offset)

        word1 = ''.join(( chr( 97 + ( ord(l) - 97 + offset ) % 26) for l in word))

        cAlphabet = ''.join(( chr( 97 + ( ord(letter) - 97 + offset ) % 26) for letter in alphabet))

        key = chr(key1) 

    elif stage == 2: # TimeCube Stage

        key1 = random.randint(128336,128346) #- 128335
        key2 = random.randint(128348,128359) #- 128347 + 0.5

        time = key1 if bool(random.randint(0, 1)) else key2

        offset = time - 128335 if time < 128348 else time - 128347 + 0.5

        offset = offset * 60
        offset = offset * offset * offset

        while offset % 26 == 0 or offset == 26:
            key1 = random.randint(128336,128346) #- 128335
            key2 = random.randint(128348,128359) #- 128347 + 0.5

            time = key1 if bool(random.randint(0, 1)) else key2

            offset = time - 128335 if time < 128348 else time - 128347 + 0.5

            offset = offset * 60
            offset = offset * offset * offset

        word1 = ''.join(( chr(math.trunc( 97 + ( ord(l) - 97 + offset ) % 26)) for l in word))

        cAlphabet = ''.join(( chr(math.trunc( 97 + ( ord(letter) - 97 + offset ) % 26)) for letter in alphabet))
        
        key = chr(time)

    for x in range(0, len(alphabet)):
        if(alphabet[x] in word):
            alphabet = alphabet[:x] + alphabet[x].upper() + alphabet[(x+1):]
            cAlphabet = cAlphabet[:x] + cAlphabet[x].upper() + cAlphabet[(x+1):]

    alphabet = alphabet.replace("", " ")[1: -1]
    cAlphabet = cAlphabet.replace("", " ")[1: -1]

    return [word1,key,alphabet, cAlphabet]


currentStage = 0
currentCrypto = encrypt(questions[currentStage],currentStage)
hintVisible = False

sg.theme('black')

layout = [  [sg.Text( text = "Crypto: " + currentCrypto[0] , key = "-Crypto-" , text_color = "white", font = ("Arial Black",30) )] ,
            [sg.Text( text = "Key: " + currentCrypto[1], key = "-Key-" , text_color = "yellow", font = ("Arial Black",30) )],
            [sg.Text('Answer: ',font = ("Arial Black",30)), sg.InputText(k = '-INPUT-',size = (25), font = ("Arial Black",30))],
            [sg.Button('Enter', k = '-ENTER-', bind_return_key = True), sg.Button('Exit') ],
            [sg.Text( text = currentCrypto[2], key = "-Help0-" , text_color = "white", font = ("Courier",20),visible = hintVisible)],
            [sg.Text( text = currentCrypto[3], key = "-Help1-" , text_color = "white", font = ("Courier",20),visible = hintVisible )],
            [sg.Text( text = "", key = "-Help2-" , text_color = "white", font = ("Courier",15),visible = hintVisible )],
            [sg.Text( text = questions[currentStage], key = "-Help3-" , text_color = "white", font = ("Courier",10),visible = hintVisible )] ]

window = sg.Window('EncryptPOG', layout,element_justification='c',finalize=True,return_keyboard_events=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    elif event == "-ENTER-":
        if window['-INPUT-'].get() == questions[currentStage]:
            
            if currentStage < 2:

                currentStage += 1
                currentCrypto = encrypt(questions[currentStage],currentStage)

                window['-Crypto-'].update(value="Crypto: " + currentCrypto[0])
                window['-Key-'].update(value="Key: " + currentCrypto[1])
                window['-Help0-'].update(value=currentCrypto[2])
                window['-Help1-'].update(value=currentCrypto[3])
                if currentStage == 1 :
                    char = ord(currentCrypto[1]) - 64
                    result = char * char * 3.14
                    window['-Help2-'].update("π * {0}² = {1} ☛ {2} % 26 = {3}".format(char,result,result,math.floor(result % 26)))
                if currentStage == 2 :
                    key = currentCrypto[1]
                    keyToTime = ord(key) - 128335 if ord(key) < 128348 else ord(key) - 128347 + 0.5
                    timeToMin = keyToTime * 60
                    minSquared = timeToMin*timeToMin*timeToMin
                    minSquared = math.trunc(minSquared)
                    squaredMod = minSquared % 26
                    window['-Help2-'].update(key + "={0} ☛ {1} * 60 = {2} ☛ {3}³(❒) = {4} ☛ {5} % 26 = {6}".format(keyToTime,keyToTime,timeToMin,timeToMin,minSquared,minSquared,squaredMod))
                
                window['-Help3-'].update(value=questions[currentStage])
                window['-INPUT-'].update('')

                if currentStage == 1:
                   window['-Crypto-'].update(value="Crypto ◯ : " + currentCrypto[0])

                if currentStage == 2:
                   window['-Crypto-'].update(value="Crypto ⏳ = ❒ : " + currentCrypto[0])

            else:
                sg.Popup("Correct Answer :D",custom_text = "Bye",no_titlebar = True, text_color = "Green",font = ("Arial Black",50))
                break

        else: 
            sg.popup_no_buttons("Incorrect Answer :(",no_titlebar = True,auto_close = True,auto_close_duration = 1.5, text_color = "Red",font = ("Arial Black",50))
            window['-INPUT-'].update('')
    elif event == "?":
        hintVisible = not hintVisible
        window['-Help0-'].update(visible=hintVisible)
        window['-Help1-'].update(visible=hintVisible)
        window['-Help2-'].update(visible=hintVisible)
        window['-Help3-'].update(visible=hintVisible)
        window['-INPUT-'].update('')
        

    
window.close()