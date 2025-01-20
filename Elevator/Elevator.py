import os
import colorama
from termcolor import cprint
import time
import threading
import PySimpleGUI as sg   

os.system("color")
colorama.init()

sg.theme('dark purple ')   #*change

path = os.getcwd() + "\images"
SPEED = 1
ELEVATOR_LIMIT = 8

#! Define the main window's contents (its a mess, dont even try to read it)
layout = [[[sg.Image(key="-3F-", size=(300,100),enable_events = True, background_color="white smoke",filename =path +"\F3-0.png"),sg.Image(key="-E3-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\elevator-closed.png"),sg.Image(key="-B3-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\\B3dd.png")], 
           [sg.Image(key="-2F-", size=(300,100),enable_events = True, background_color="white smoke",filename =path +"\F2-0.png"),sg.Image(key="-E2-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\elevator-closed.png"),sg.Image(key="-B2-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\\B2dd.png")],
           [sg.Image(key="-1F-", size=(300,100),enable_events = True, background_color="white smoke",filename =path +"\F1-0.png"),sg.Image(key="-E1-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\elevator-closed.png"),sg.Image(key="-B1-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\\B1dd.png")],
           [sg.Image(key="-0F-", size=(300,100),enable_events = True, background_color="white smoke",filename =path +"\F0-0.png"),sg.Image(key="-E0-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\elevator-closed.png"),sg.Image(key="-B0-", size=(100,100),enable_events = True, background_color="white smoke",filename =path +"\\B0dd.png")]]]

#! Create main window
window = sg.Window('Building', layout,finalize=True) 

building = [[False,0],[False,0],[False,0],[False,0]] #one list for each flor >  [state(calling elevator), n ppl incoming]
elevator = [0,[],0,True] # current floor, floors to go, n of ppl inside,state change(active or not, used to set buttons state)

def floorsUpdate(): # updates elevators visualy
    while True:
        #UPDATES FLOORS N OF PPL
        window['-0F-'].update(filename= path + '/F0-' + str(building[0][1]) + '.png')
        window['-1F-'].update(filename= path + '/F1-' + str(building[1][1]) + '.png')
        window['-2F-'].update(filename= path + '/F2-' + str(building[2][1]) + '.png')
        window['-3F-'].update(filename= path + '/F3-' + str(building[3][1]) + '.png')

        if kill_thread: #threading
            break #breaks thread

def elevatorSystem(): # elevator logic, called by thread, images updates also done here
    while True:

        #BUTTONS STATE
        if elevator[2] == 0 and elevator[3]:
            window['-B3-'].update(filename= path + '/B3dd.png')
            window['-B2-'].update(filename= path + '/B2dd.png')
            window['-B1-'].update(filename= path + '/B1dd.png')
            window['-B0-'].update(filename= path + '/B0dd.png')
            cprint('Elevator awaiting',"green")
            time.sleep(SPEED)
        elif elevator[3]:
            window['-B3-'].update(filename= path + '/B3d.png')
            window['-B2-'].update(filename= path + '/B2d.png')
            window['-B1-'].update(filename= path + '/B1d.png')
            window['-B0-'].update(filename= path + '/B0d.png')
            elevator[3] = False 
        if elevator[2] < 1:
            elevator[3] = True
        #BUTTONS STATE
    
        for floor in range(4):
            
            if (building[floor][0] and elevator[0] == floor) or (floor in elevator[1] and elevator[0] == floor):
                
                if elevator[3]: #clunky botton stuff.
                    window['-B3-'].update(filename= path + '/B3d.png')
                    window['-B2-'].update(filename= path + '/B2d.png')
                    window['-B1-'].update(filename= path + '/B1d.png')
                    window['-B0-'].update(filename= path + '/B0d.png')
                    elevator[3] = False

                #UNLOAD PPL INSIDE
                if elevator[1].count(floor) > 0 or building[floor][0]:

                    cprint('Opening doors at floor '+ str(floor),"green")
                    window['-E'+ str(floor) +'-'].update(filename= path + '/elevator-opening-'+str(elevator[2])+'.png')
                    time.sleep(SPEED)
                    window['-E'+ str(floor) +'-'].update(filename= path + '/elevator-open-'+str(elevator[2])+'.png')
                    time.sleep(SPEED)

                if elevator[1].count(floor) > 0:
                    cprint(str(elevator[1].count(elevator[0])) + " ppl left the elevator")
                    window['-B' +str(floor)+ '-'].update(filename= path + '/B'+str(floor)+ 'd.png')
                    elevator[2] -= elevator[1].count(elevator[0])
                    elevator[1] = [x for x in elevator[1] if x != floor]
                    
                #LOADS PPL WAITING
                if elevator[2] < ELEVATOR_LIMIT:
                    
                    if ((elevator[2] + building[floor][1]) < ELEVATOR_LIMIT):
                        elevator[2] += building[floor][1]
                        window['-E'+ str(floor) +'-'].update(filename= path + '/elevator-open-'+str(elevator[2])+'.png')
                        print(str(building[floor][1]) + " ppl entered the elevator at floor" + str(floor))
                        building[floor][1] = 0
                        building[floor][0] = False
                        ##SET IMAGE OF FLOOR HERE OR IN THE MAIN LOOP
                    else:
                        diff = abs(elevator[2] - ELEVATOR_LIMIT)
                        print(str(diff) + " ppl entered the elevator")
                        elevator[2] += diff
                        building[floor][1] -= diff
                        building[floor][0] = False
                        diff = 0

                    #awaits the correct number of button presses
                    while(len(elevator[1]) != elevator[2]):
                        window['-E'+ str(floor) +'-'].update(filename= path + '/elevator-open-'+str(elevator[2])+'.png')
                        cprint("Awaiting button press","green")
                        time.sleep(SPEED)

                    
                    cprint("All set, closing doors","green")
                    window['-E'+ str(floor) +'-'].update(filename= path + '/elevator-opening-'+str(elevator[2])+'.png')
                    time.sleep(SPEED)
                    window['-E'+ str(floor) +'-'].update(filename= path + '/elevator-closed.png')

                else:
                    cprint("Elevator full","green")
                    time.sleep(SPEED)
        
        ##Adds or subtract floor depending on closest target floor

        temp = 10
        tempCalling = []

        for i in range(4):
                if building[i][0] == True:
                    tempCalling.append(i)

        if elevator[1]:
            for i in elevator[1]:

                if abs(elevator[0] - i) < temp:
                    temp = i
            
            if temp > elevator[0]:
                elevator[0] += 1
                cprint("Going up!","green")
                time.sleep(SPEED)
            elif temp < elevator[0]:
                elevator[0] -= 1
                cprint("Going down!","green")
                time.sleep(SPEED)
            else:elevator[0] = 0

        elif tempCalling:
                            
            for i in tempCalling:
                if abs(elevator[0] - i) < temp:
                    temp = i
            if temp > elevator[0]:
                elevator[0] += 1
                cprint("Going up!","green")
                time.sleep(SPEED)
            elif temp < elevator[0]:
                elevator[0] -= 1
                cprint("Going down!","green")
                time.sleep(SPEED)
            else:elevator[0] = 0
        
        tempCalling = []
        if elevator[2] == 0:
            elevator[3] = True

        if kill_thread:
            break
    
#creates a thread for the elevator and building, necessary for updating values while the main programming still interactive
t = threading.Thread(target=elevatorSystem)
et = threading.Thread(target=floorsUpdate)
kill_thread = False
t.start()
et.start()

#! Event loop
while True:
    event, values = window.read()    

    if event == sg.WINDOW_CLOSED: #? Exits
        break
    #*Add people ========================================================
    elif event == "-3F-":
        
        if building[3][1] > 4:
            cprint("max amount of ppl reache on floor 3","red")
        else: 
            building[3][1] +=1
            print("add person 3 floor")

    elif event == "-2F-":
        
        if building[2][1] > 4:
            cprint("max amount of ppl reache on floor 2","red")
        else: 
            building[2][1] +=1
            print("add person 2 floor")

    elif event == "-1F-":
        
        if building[1][1] > 4:
            cprint("max amount of ppl reache on floor 1","red")
        else: 
            building[1][1] +=1
            print("add person 1 floor")

    elif event == "-0F-":
        
        if building[0][1] > 4:
            cprint("max amount of ppl reache on floor 0","red")
        else: 
            building[0][1] +=1
            print("add person 0 floor")

    #* Call Elevator====================================================
    elif event == "-E3-" and building[3][1] > 0:
        if not building[3][0]:
            building[3][0] = True
            window['-E3-'].update(filename= path + '/elevator-calling.png')
            cprint("called E3","blue")
    elif event == "-E2-" and building[2][1] > 0:
        if not building[2][0]:
            building[2][0] = True
            window['-E2-'].update(filename= path + '/elevator-calling.png')
            cprint("called E2","blue")
    elif event == "-E1-" and building[1][1] > 0:
        if not building[1][0]:
            building[1][0] = True
            window['-E1-'].update(filename= path + '/elevator-calling.png')
            cprint("called E1","blue")
    elif event == "-E0-" and building[0][1] > 0:
        if not building[0][0]:
            building[0][0] = True
            window['-E0-'].update(filename= path + '/elevator-calling.png')
            cprint("called E0","blue")

    #* Elev buttons ====================================================
    elif event == "-B3-" and elevator[2] > 0:
        if len(elevator[1]) < 8 and len(elevator[1]) < elevator[2]:
            elevator[1].append(3)
            window['-B3-'].update(filename= path + '/B3a.png')
            cprint("pressed B3","blue")
    elif event == "-B2-" and elevator[2] > 0:
        if len(elevator[1]) < 8 and len(elevator[1]) < elevator[2]:
            elevator[1].append(2)
            window['-B2-'].update(filename= path + '/B2a.png')
            cprint("pressed B2","blue")
    elif event == "-B1-" and elevator[2] > 0:
        if len(elevator[1]) < 8 and len(elevator[1]) < elevator[2]:
            elevator[1].append(1)
            window['-B1-'].update(filename= path + '/B1a.png')
            cprint("pressed B1","blue")
    elif event == "-B0-" and elevator[2] > 0:
        if len(elevator[1]) < 8 and len(elevator[1]) < elevator[2]:
            elevator[1].append(0)
            window['-B0-'].update(filename= path + '/B0a.png')
            cprint("pressed B0","blue")
    
    
window.close()

for c in range(4):
    print("Floor" + str(c) +":",end="")
    print(building[c]) 

print("Elevator:",end="")
print(elevator)

#kills threads
kill_thread = True

et.join()
t.join()

input("quit?")
