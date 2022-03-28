import sys

import pandas as pd
import numpy as np

class Dataframes:
    def __init__(self, path):
        self.excelPath = path

        self.vmixRaw = None
        self.dataRaw = None
        self.cabezaSerie = None
        self.bombo1 = None
        self.bombo2 = None
        self.bombo3 = None

    # -- Categories Dataframes --
    # CREC QUE AIXÒ NO FARÀ FALTA
    def createCategoriaA1(self, df_data_raw, col_num, col_names):
        # Drop first four rows
        df_data_clean = df_data_raw.drop(df_data_raw.index[:5])
        # Get first four columns
        categoria_A1_clean = [df_data_clean['Unnamed: 1'],
                              df_data_clean['Unnamed: 2'],
                              df_data_clean['Unnamed: 3'],
                              df_data_clean['Unnamed: 4']]

        # Concatenate in a single dataframe
        df_categoria_A1 = pd.concat(categoria_A1_clean, axis=1, keys=col_names)
        return df_categoria_A1

    def createCabezasSerie(self, df_data_raw, col_num, col_names, num_teams):
        # Make it more flexible
        curr_pos = 4
        # Drop first three rows and below ones
        df_data_clean = df_data_raw.drop(df_data_raw.index[:curr_pos])
        df_data_clean = df_data_clean.drop(df_data_raw.index[curr_pos + num_teams:])
        # Get first four columns
        cabezas_serie_clean = [df_data_clean['Unnamed: 6'],
                              df_data_clean['Unnamed: 7'],
                              df_data_clean['Unnamed: 8'],
                              df_data_clean['Unnamed: 9']]

        # Concatenate in a single dataframe
        df_cabeza_serie = pd.concat(cabezas_serie_clean, axis=1, keys=col_names)
        #print('Cabezas de serie:')
        #print(df_cabeza_serie)
        return df_cabeza_serie

    def createBombo1(self, df_data_raw, col_num, col_names, num_teams, num_teams_prev):
        #Make it more flexible
        curr_pos = 6 + num_teams_prev + 1
        final_pos = curr_pos + num_teams
        # Drop first 23 rows and below ones
        df_data_clean = df_data_raw.drop(df_data_raw.index[:curr_pos])
        df_data_clean = df_data_clean.drop(df_data_raw.index[final_pos:])
        # Get first four columns
        bombo1_clean = [df_data_clean['Unnamed: 6'],
                        df_data_clean['Unnamed: 7'],
                        df_data_clean['Unnamed: 8'],
                        df_data_clean['Unnamed: 9']]

        # Concatenate in a single dataframe
        df_bombo1 = pd.concat(bombo1_clean, axis=1, keys=col_names)
        #print('Bombo 1:')
        #print(df_bombo1)
        return df_bombo1

    def createBombo2(self, df_data_raw, col_num, col_names, num_teams, num_teams_prev):
        curr_pos = 6 + num_teams_prev + 4
        final_pos = curr_pos + num_teams
        # Drop first 43 rows and below ones
        df_data_clean = df_data_raw.drop(df_data_raw.index[:curr_pos])
        df_data_clean = df_data_clean.drop(df_data_raw.index[final_pos:])
        # Get first four columns
        bombo2_clean = [df_data_clean['Unnamed: 6'],
                        df_data_clean['Unnamed: 7'],
                        df_data_clean['Unnamed: 8'],
                        df_data_clean['Unnamed: 9']]

        # Concatenate in a single dataframe
        df_bombo2 = pd.concat(bombo2_clean, axis=1, keys=col_names)
        #print('Bombo 2:')
        #print(df_bombo2)
        return df_bombo2

    def createBombo3(self, df_data_raw, col_num, col_names, num_teams, num_teams_prev):
        curr_pos = 6 + num_teams_prev + 7
        final_pos = curr_pos + num_teams
        # Drop first 63 rows and below ones
        df_data_clean = df_data_raw.drop(df_data_raw.index[:curr_pos])
        df_data_clean = df_data_clean.drop(df_data_raw.index[final_pos:])
        # Get first four columns
        bombo3_clean = [df_data_clean['Unnamed: 6'],
                        df_data_clean['Unnamed: 7'],
                        df_data_clean['Unnamed: 8'],
                        df_data_clean['Unnamed: 9']]

        # Concatenate in a single dataframe
        df_bombo3 = pd.concat(bombo3_clean, axis=1, keys=col_names)
        #print('Bombo 3:')
        #print(df_bombo3)
        return df_bombo3

    # -- Load --
    def getColNames(self, df_data_raw, col_num):
        col_names = []
        for i in range (col_num):
            # Get column names knowing that they are at row 4
            col_names.append(df_data_raw.iloc[4,i])
        return col_names

    def loadExcel(self, path):
        xls_file = pd.ExcelFile(path)
        df_VMIX = pd.read_excel(xls_file, 'VMIX')
        df_DADES = pd.read_excel(xls_file, 'DADES')
        return df_DADES, df_VMIX

    def createDataframes(self, excel_path, col_num, cabeza_serie_num, bombo1_num, bombo2_num, bombo3_num):
        self.dataRaw, self.vmixRaw = self.loadExcel(excel_path)
        # Eliminem la primera columna per què no es guardi al dataframe final
        print(self.vmixRaw)
        if 'Unnamed: 0' in self.dataRaw:
            del self.dataRaw['Unnamed: 0']
        if 'Unnamed: 0' in self.vmixRaw:
            del self.vmixRaw['Unnamed: 0']
        print(self.vmixRaw)

        # Agafem els noms de les columnes per concatenar-ho
        col_names = self.getColNames(self.dataRaw, col_num)
        # Això ja no fa falta
        #df_categoria_A1 = self.createCategoriaA1(self.dataRaw, col_num, col_names)
        self.cabezaSerie = self.createCabezasSerie(self.dataRaw, col_num, col_names, cabeza_serie_num)
        self.bombo1 = self.createBombo1(self.dataRaw, col_num, col_names, bombo1_num, cabeza_serie_num)
        self.bombo2 = self.createBombo2(self.dataRaw, col_num, col_names, bombo2_num, bombo1_num + cabeza_serie_num)
        self.bombo3 = self.createBombo3(self.dataRaw, col_num, col_names, bombo3_num, bombo2_num + bombo1_num + cabeza_serie_num)

        return self

    # -- Export Datfaframes --
    def saveDataframe(self):
        with pd.ExcelWriter(self.excelPath) as writer:
            self.vmixRaw.to_excel(writer, sheet_name='VMIX')
            self.dataRaw.to_excel(writer, sheet_name='DADES')

    def exportDataframe(self, introduced_row, group_num, serie_num, is_last):
        # Update team info
        row_values = introduced_row.values[0]
        row_values = np.delete(row_values, 1)
        #for i in range (4):
        #position = i + 11
        #col_name = 'Unnamed: ' + str(position)
        #self.dataRaw.at[1, col_name] = row_values[i]

        # VMIX
        cols_first = ['E0', 'P0', 'L0']
        cols_groups = ['G', '_E', '_P', '_L']
        for i in range(3):
            # Grups petits
            # -- VMIX
            col_name = cols_groups[0] + str(group_num) + cols_groups[i+1] + str(serie_num)
            self.vmixRaw.at[0, col_name] = row_values[i]

            # -- DATA
            # Find row num
            #row_num = (group_num - 1% 5) + 6 + 3 * (group_num % 5
            #print(group_num)
            #print(row_num)

            if is_last:
                # Logo gran
                col_name = cols_first[i]
                self.vmixRaw.at[0, col_name] = row_values[i]

    def findData(self, teams, group_num):
        # Create a dictinary to access by index
        series_dict = {0: self.cabezaSerie, 1: self.bombo1, 2: self.bombo2, 3: self.bombo3}

        # Save all input teams until the last introduced
        is_last = False
        team_i = 0
        while is_last == False:
            # Posem això al principi per què si tot és empty anirà iterant fins a 4 i petarà a la següent linea
            if team_i == len(teams) - 1:
                is_last = True

            curr_serie = series_dict[team_i]
            curr_row = curr_serie.loc[curr_serie['EQUIP'] == teams[team_i]]
            # Check if empty
            if curr_row.empty:
                pass

            else:
                # Check if current is the last introduced one and if is not last per que no peti
                if not is_last and (teams[team_i + 1] == '' or teams[team_i + 1] == 'nan'):
                    is_last = True

                # Team i + 1 per què vagi de 1 a 4
                self.exportDataframe(curr_row, group_num, team_i + 1, is_last)
            team_i += 1

        self.saveDataframe()
        print('Done:)')



