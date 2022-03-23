import sys
import PySimpleGUI as sg

from loadDataframes import Dataframes

def group_window(dataframe, group_name, group_num):
    # Load equips
    cabezaSerie = dataframe.cabezaSerie['EQUIP'].values.tolist()
    bombo1 = dataframe.bombo1['EQUIP'].values.tolist()
    bombo2 = dataframe.bombo2['EQUIP'].values.tolist()
    bombo3 = dataframe.bombo3['EQUIP'].values.tolist()

    # -- GUI definition --
    window_name = 'Grup ' + group_name
    layout = [[sg.Text(window_name, font=('Calibri', 15), text_color='White')],
        [sg.Text('Cabeza de serie', font=('Calibri', 15), text_color='White', pad=10)],
        [sg.InputOptionMenu(cabezaSerie, background_color='LightBlue', size=(30,1))],
        [sg.Text('Bombo 1', font=('Calibri', 15), text_color='White', pad=10)],
        [sg.InputOptionMenu(bombo1, background_color='LightBlue', size=(30,1))],
        [sg.Text('Bombo 2', font=('Calibri', 15), text_color='White', pad=10)],
        [sg.InputOptionMenu(bombo2, background_color='LightBlue', size=(30,1))],
        [sg.Text('Bombo 3', font=('Calibri', 15), text_color='White', pad=10)],
        [sg.InputOptionMenu(bombo3, background_color='LightBlue', size=(30,1))],
        [sg.Button('Actualitzar', key = 'update', font=('Calibri', 15), button_color='Teal', pad=20)]]

    window = sg.Window(window_name, layout)
    # -- Loop & Pocess menu choices --
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, ' Exit'):
            break
        if event == 'update':
            if len(values) != 0:
                Dataframes.findData(dataframe, values, group_num)
        if event == 'close':
            break

    window.close()

# Per si en algun moment torna a fer falta
def inputGroups():
    sg.theme('DarkBlue8')
    layout = [
        [sg.Text('Número equips Cabeza de Serie: ', font=('Calibri', 15)), sg.InputText(size=(5,1))],
        [sg.Text('Número equips Bombo 1: ', font=('Calibri', 15)), sg.InputText(size=(5,1))],
        [sg.Text('Número equips Bombo 2: ', font=('Calibri', 15)), sg.InputText(size=(5,1))],
        [sg.Text('Número equips Bombo 3: ', font=('Calibri', 15)), sg.InputText(size=(5,1))],
        [sg.Button('Acceptar', key = 'accept', font=('Calibri', 15))]
    ]
    window = sg.Window('Selecció de grup', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, ' Exit'):
            break
        if event == 'accept':
            return int(values[0]), int(values[1]), int(values[2]), int(values[3])
            break
        if event == 'close':
            break

    window.close()

def selectGroup_window(dataframe):
    # -- GUI definition --
    sg.theme('DarkBlue8')
    layout = [
        [sg.Text('Selecció de grup:', font=('Calibri', 15), text_color='White')],
        [sg.Button('Grup A ', key = 'Grup_A', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup B', key = 'Grup_B', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup C', key = 'Grup_C', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup D ', key = 'Grup_D', font=('Calibri', 15), button_color='LightBlue',size=(10,3))],
        [sg.Button('Grup E', key = 'Grup_E', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup F', key = 'Grup_F', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup G ', key = 'Grup_G', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup H', key = 'Grup_H', font=('Calibri', 15), button_color='LightBlue',size=(10,3))],
        [sg.Button('Grup I', key = 'Grup_I', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button(' Grup J ', key = 'Grup_J', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup K ', key = 'Grup_K', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup L', key = 'Grup_L', font=('Calibri', 15), button_color='LightBlue',size=(10,3))],
        [sg.Button('Grup M', key = 'Grup_M', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup N', key = 'Grup_N', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button('Grup O', key = 'Grup_O', font=('Calibri', 15), button_color='LightBlue',size=(10,3)), sg.Button(' Grup P ', key = 'Grup_P', font=('Calibri', 15), button_color='LightBlue',size=(10,3))],
        [sg.Button('Guardar', key='save', font=('Calibri', 15), button_color='Teal', pad=20)]
    ]

    window = sg.Window('Selecció de grup', layout)

    # -- Loop & Pocess menu choices --
    while True:
        event, values = window.read()
        print(values)
        if event in (sg.WIN_CLOSED, ' Exit'):
            break
        if event == 'Grup_A':
            group_window(dataframe, 'A', 1)
        if event == 'Grup_B':
            group_window(dataframe, 'B', 2)
        if event == 'Grup_C':
            group_window(dataframe, 'C', 3)
        if event == 'Grup_D':
            group_window(dataframe, 'D', 4)
        if event == 'Grup_E':
            group_window(dataframe, 'E', 5)
        if event == 'Grup_F':
            group_window(dataframe, 'F', 6)
        if event == 'Grup_G':
            group_window(dataframe, 'G', 7)
        if event == 'Grup_H':
            group_window(dataframe, 'H', 8)
        if event == 'Grup_I':
            group_window(dataframe, 'I', 9)
        if event == 'Grup_J':
            group_window(dataframe, 'J', 10)
        if event == 'Grup_K':
            group_window(dataframe, 'K', 11)
        if event == 'Grup_L':
            group_window(dataframe, 'L', 12)
        if event == 'Grup_M':
            group_window(dataframe, 'M', 13)
        if event == 'Grup_N':
            group_window(dataframe, 'N', 14)
        if event == 'Grup_O':
            group_window(dataframe, 'O', 15)
        if event == 'Grup_P':
            group_window(dataframe, 'P', 16)
        if event == 'close':
            break
        if event == 'save':
            dataframe.saveDataframe()

    window.close()
