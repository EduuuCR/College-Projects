import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import PySimpleGUI as sg
import cv2
import extcolors

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from colormap import rgb2hex

currentQuestion = 0
result = 0 
probability = 0
failState = False
questionStage = True
tutorialTxt = "\n1°Evite ambientes muito escuros ou claros\n2°Envie uma foto apenas do seu rosto ou da área afetada pelo sintoma\n3°O fundo da imagem deve ser simples, sem muitas cores.\n"
photo = None
#4,5,5 -- +1 +2 +3
questions = [
"Sua pele arde ou repuxa e fica vermelha no inverno?", # 0
"Você já teve reações cutâneas após o contato com certos materiais, como níquel ou látex?", # 1
"Quando você ingere comida muito condimentadas, seu rosto fica vermelho, com calor ou ardendo?", # 2
"Você tem histórico de condições de pele, como eczema ou psoríase?", # 3
"Você já teve vermelhidão na pele sem o uso de cosméticos?",# 4
"Sua pele reage negativamente a cosméticos, como produtos para o rosto ou maquiagem?", # 5
"Já ocorreram formação de bolhas ou irritação extrema na pele após usar produtos cosméticos?", # 6
"Sente desconforto na pele, como queimação/ressecamento após exposição solar ?",# 7
"Após um banho quente, você tem a sensação de que a pele fica seca, repuxando e coça?", # 8
"Você já teve reações cutâneas desencadeadas por produtos de cuidados pessoais?", # 9
"Sua pele é facilmente irritada ou sensível a produtos comuns para a pele?", # 10
"Você já experimentou coceira ou irritação na pele após a aplicação de produtos cosméticos?", # 11
"Sua pele tende a ficar seca, descamada ou irritada com facilidade?", # 12
"Sua pele é geralmente sensível a produtos químicos ou substâncias irritantes?" # 13
]

sg.theme('bluepurple')

layout = [  [sg.Text( text = questions[currentQuestion] , key = "-Question-" , text_color = "black", font = ("Arial Black",20) )] ,
            [sg.Button('Sim', k = '-Sim-',font = ("Arial Black",10)), sg.Button('Não', k = '-Não-',font = ("Arial Black",10)), sg.Button("Selecionar Foto",k = '-Photo-',font = ("Arial Black",10),visible= False) ]]

window = sg.Window('SkinSense', layout,element_justification='c',finalize=True,return_keyboard_events=True)#,size=(1500,150)
window.TKroot.minsize(1500,150)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    
    elif event == "-Photo-":

      photo = sg.popup_get_file('Selecione sua foto', keep_on_top=True)
      output_width = 900   

      img = Image.open(photo)
      wpercent = (output_width/float(img.size[0]))
      hsize = int((float(img.size[1])*float(wpercent)))
      img = img.resize((output_width,hsize), Image.Resampling.LANCZOS)

      colors, pixels = extcolors.extract_from_image(img)

      rgb_list = [x[0] for x in colors]
      colored = 0
      for rgb in rgb_list:
        if (rgb[0] >= rgb[1] + 50 and rgb[0] >= rgb[2] + 60) and (rgb[1] - rgb[2]) >= 10 :
          colored +=1

      probability2 = 0

      if colored == 0:
        probability2 = 0
        failState = True

      elif colored == 1:
        probability2 += 3

      elif colored == 2:
        probability2 += 7

      elif colored > 2:
        probability2 += 10

      if (probability == 10 and (probability2 == 10 or probability2 == 7)) or ((probability == 8 or probability == 5) and probability2 ==10) and failState == 0:
        window['-Question-'].update(value="Você com certeza tem sensibilidade de pele!",font = ("Arial Black",20))

      elif (probability == 8 or probability == 5) and probability2 ==7 and failState == 0:
        window['-Question-'].update(value="Muito provavelmente você tem sensibilidade de pele",font = ("Arial Black",20))

      elif (probability == 10 or probability == 8) and probability2 == 3 and failState == 0:
        window['-Question-'].update(value="Existem grandes chances de você ter sensibilidade de pele, porém, \nnão detectamos nada na imagem",font = ("Arial Black",20))

      elif probability == 2 and probability2 ==10 and failState == 0:
        window['-Question-'].update(value="Existem grandes chances de você ter sensibilidade de pele, ou ter \nenviado uma imagem muito vermelha",font = ("Arial Black",20))

      elif (probability == 5 and probability2 ==3) or (probability == 2 and probability2 ==7) and failState == 0:
        window['-Question-'].update(value="Existe a possibilidade de você ter sensibilidade de pele, porém, \nparece que é outro sintoma que você tem, é recomendado passar eu um dermatologista para verificar",font = ("Arial Black",20))

      elif probability == 2 and probability2 ==3 and failState == 0:
        window['-Question-'].update(value="Provavelmente você não tem sensibilidade, caso esteja sentindo \nalguma coisa parecida recomendamos você a consultar um dermatologista",font = ("Arial Black",20))

      elif probability == 0 and failState == 1:
        window['-Question-'].update(value="Você respondeu o questionario todo com não, tirando qualquer \npossibilidade de ser sensibilidade, caso ainda esteja com problemas recomendamos você a consultar um dermatologista",font = ("Arial Black",20))

      elif probability2 == 0 and failState == 1:
        window['-Question-'].update(value="A imagem que você enviou não contem cor vermelha, caso acredite \nter algo no rosto, responda o questionario novamente e envie uma nova foto assim como a recomendada!",font = ("Arial Black",20))

    if event == "-Sim-":
      if currentQuestion < 4:
        result += 1
      elif currentQuestion < 9:
        result += 3
      else: result += 5 

      if currentQuestion < len(questions) -1:
        currentQuestion += 1
      else: questionStage = False
      
    if event == "-Não-":
      if currentQuestion < 4:
        result -= 1
      elif currentQuestion < 9:
        result -= 2
      else: result -= 3 

      if currentQuestion < len(questions) -1:
        currentQuestion += 1
      else: questionStage = False
    
    if questionStage:
      window['-Question-'].update(value=questions[currentQuestion])
    else:
      if photo == None:
        window['-Question-'].update(value="Envie sua foto 📸" + tutorialTxt,font = ("Arial Black",20))
      window['-Sim-'].update(visible = False)
      window['-Não-'].update(visible = False)
      window['-Photo-'].update(visible = True)
      
      if result == 44:
        probability =+ 10
      elif 30 <= result <= 43:
        probability =+ 8
      elif  10 <= result <= 29:
        probability =+ 5
      elif  0 <= result <= 9:
        probability =+ 2
      elif  result < 0:
        probability = 0
        failState = True

window.close()
