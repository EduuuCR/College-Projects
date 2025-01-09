#BIBLIOTECAS
import random
import PySimpleGUI as sg #INTERFACE

path = "D:\Trabson\POG"

#ABRINDO ARQUIVO
f = open(path + r"\questions.txt", "r")
flines = f.readlines()

#NÚMEROS RANDOM
randomNums = []

while len(randomNums) < 3:
    num = random.randint(0,19)
    if num not in randomNums:
        randomNums.append(num)
    
questions = []

#PEGANDO AS PERGUNTAS
for x in randomNums:
    questions.append(flines[x])

#CONFIGURANDO PROGRAMAS
currentQuestionNum = 0
currentQuestion = questions[currentQuestionNum]
question =  currentQuestion.split(",")[0]
anwser = currentQuestion.split(",")[1]
correctAnwsers = 0
superCorret = 0
secret =  []

imgRED = path + '/RED.png'
imgGREEN = path + '/GREEN.png'
imgBLUE = path + '/BLUE.png'
imgSEC = path + '/SEC.png'
imgNO = path + '/no.png'
imgYES = path + '/yes.png'
imgSYES = path + '/syes.png'
imgSSYES = path + '/ssecret.png'

#CONFIGURANDO A JANELA
sg.theme('black')

layout = [  [sg.Text( text = question, key = "-QUESTION-" , text_color = "yellow", font = "bold" )] ,
            [sg.Text('Anwser: '), sg.InputText(k = '-INPUT-'), sg.Image(k = '-CHECK0-',size = (10,30),filename  = imgBLUE,enable_events = True), sg.Image(k = '-CHECK1-',size = (10,30),filename  = imgBLUE,enable_events = True), sg.Image(k = '-CHECK2-',size = (10,30),filename  = imgBLUE,enable_events = True)],
            [sg.Button('Enter', k = '-ENTER-', bind_return_key = True), sg.Button('Exit') ] ]


window = sg.Window('NoName', layout)

#ABRINDO A JANELA
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    elif event == '-CHECK0-':
        secret.append(0)
    elif event == '-CHECK1-':
        secret.append(1)
    elif event == '-CHECK2-':
        secret.append(2)
    elif secret == [0,2,1,1,2,0]:
        sg.Popup(image = imgSSYES)
        window.close() 
    elif event == '-ENTER-':
        temp = currentQuestion
        temp = temp.rstrip("?")
        temp = temp.count(' ') + 1

        if window['-INPUT-'].get().isnumeric():
            if int(window['-INPUT-'].get()) == temp:
                superCorret += 1
                window['-CHECK'+ str(currentQuestionNum) + '-'].update(filename = imgSEC)
            else:
                window['-CHECK'+ str(currentQuestionNum) + '-'].update(filename = imgRED)
        elif window['-INPUT-'].get() == anwser.rstrip("\n"):
            window['-CHECK'+ str(currentQuestionNum) + '-'].update(filename = imgGREEN)
            correctAnwsers +=1
        else:
            window['-CHECK'+ str(currentQuestionNum) + '-'].update(filename = imgRED)

        currentQuestionNum += 1

        if currentQuestionNum == 3:
            if superCorret == 3:
                sg.Popup(image = imgSYES)
            elif correctAnwsers == 3:
                sg.Popup(image = imgYES)
            else:
                sg.Popup(image = imgNO)
            window.close() 
        else:
            currentQuestion = questions[currentQuestionNum]
            question =  currentQuestion.split(",")[0]
            anwser = currentQuestion.split(",")[1]
    
            window['-QUESTION-'].update(value = question)
            window['-INPUT-'].update('')

window.close()