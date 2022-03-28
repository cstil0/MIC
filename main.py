import sys
import os

from loadDataframes import Dataframes
import GUI

if __name__ == '__main__':
    excel_path = 'Y:CATEGORIA 0_VMIX.xlsx'
    dataframes = Dataframes(excel_path)
    #df_VMIX, df_DADES = Dataframes.loadExcel(dataframes, excel_path)

    # Fila on estàn els noms de les columnes
    col_num = 4
    # Per si en algun moment torna a fer falta
    #cabeza_serie_num, bombo1_num, bombo2_num, bombo3_num = GUI.inputGroups()
    cabeza_serie_num, bombo1_num, bombo2_num, bombo3_num = (17, 17, 17, 17)
    dataframe = Dataframes.createDataframes(dataframes, excel_path, col_num, cabeza_serie_num, bombo1_num, bombo2_num, bombo3_num )
    # Open window GUI
    GUI.selectGroup_window(dataframe)
