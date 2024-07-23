from communicator import speak, recognize_speech_from_microphone as micInput
from csv_editor import CSVEditor
from utils import is_convertible_to_int


class CSV_Sub_Tasks:
    def __init__(self, csv_: CSVEditor):
        # Initialization code here (if needed)
        self.csv_ = csv_
        self.added_rows = []
        self.added_cols = []

    def save_changes(self):
        # code to save changes in csv_file
        speak('Here\'s the overview of the changes you made')
        df = self.csv_.get_dataframe()
        print(df)

        doSave = micInput(
            'Do you want to save the changes you made? say \'yes\' to save the changes')
        if doSave == 'yes':
            csv_filename_path_toSave = micInput(
                f'Say the filename/path where you want to save the changes or directly or provide an empty input if you want to save your changes in same csv_file i.e. \'{self.csv_.csv_file_path}\'')

            if csv_filename_path_toSave == '':
                self.csv_.save_csv()
            else:
                self.csv_.save_csv(csv_filename_path_toSave)

            speak(f'Successfully saved the changes in the file {
                self.csv_.csv_file_path}')
        else:
            speak("Your changes have not been saved. Any unsaved changes will be lost.")

    def load_csv(self):
        try:
            # Code to add a new row with specified values
            pass
        except Exception as e:
            speak(f"An error occurred while adding a row")
            print(str(e))

    def addRow(self):
        try:
            # Code to load the current CSV data to a file
            no_of_rows_to_add = int(
                micInput('Say the number of rows you want to add'))

            for no_of_row in range(no_of_rows_to_add):
                row_index = self.csv_.add_row()
                self.added_rows.append(row_index)

            if len(self.added_rows) == no_of_rows_to_add:
                speak(f'Successfully added {
                      no_of_rows_to_add}/{len(self.added_rows)} rows!')
                df = self.csv_.get_dataframe()
                print(df)

            for row_added in self.added_rows:
                speak(f'Row.{row_added}:')
                print(print(f'\n{self.csv_.get_row(row_added)}\n'))

                speak("Please choose one of the following options:")
                speak(
                    "1. Set all row values at once,\n2. Add them column by column,\n3. Keep the row empty")

                setting_row_values_choice = micInput(
                    "Say the number of your choice")

                setting_row_values_choice1 = setting_row_values_choice == 'one' or setting_row_values_choice == '1'
                setting_row_values_choice2 = setting_row_values_choice == 'two' or setting_row_values_choice == '2'
                setting_row_values_choice3 = setting_row_values_choice == 'three' or setting_row_values_choice == '3'

                if setting_row_values_choice1 or setting_row_values_choice2:

                    if setting_row_values_choice1:
                        values_to_set_in_row = micInput(
                            'Say the row values seperated by space')

                        values_to_set_in_row = values_to_set_in_row.split(' ')
                        temp_values = []
                        for value in values_to_set_in_row:
                            if is_convertible_to_int(value):
                                value = int(value)
                            temp_values.append(value)
                        else:
                            values_to_set_in_row = temp_values

                        self.csv_.set_row(row_added, values_to_set_in_row)

                        print(f'\n{self.csv_.get_row(row_added)}\n')

                    elif setting_row_values_choice2:
                        columns = self.csv_.get_row(row_added).columns

                        for col in columns:
                            value_to_set_in_col_of_row = micInput(
                                f'Say the value for the column.{col}')

                            if is_convertible_to_int(value_to_set_in_col_of_row):
                                value_to_set_in_col_of_row = float(
                                    value_to_set_in_col_of_row)

                            self.csv_.edit_row(
                                value_to_set_in_col_of_row, row_added, col)

                        print(f'\n{self.csv_.get_row(row_added)}\n')

                elif setting_row_values_choice3:
                    print(f'\n{self.csv_.get_row(row_added)}\n')

                else:
                    raise ValueError(
                        f'You must say/enter the values between 1 - 3, but you say/enter {setting_row_values_choice}')

            self.save_changes()

        except Exception as e:
            speak(f"An error occurred while loading the CSV")
            print(str(e))

            self.added_rows.reverse()
            for row_added in self.added_rows:
                self.csv_.drop_row(row_added)
                self.added_rows.remove(row_added)
            self.added_rows.reverse()

            self.addRow()

    def drop_row(self):
        try:
            # Code to drop a row at the specified index
            pass
        except Exception as e:
            speak(f"An error occurred while dropping a row")
            print(str(e))

    def edit_row(self):
        try:
            # Code to edit a specific row and column with a new value
            pass
        except Exception as e:
            speak(f"An error occurred while editing a row")
            print(str(e))

    def add_column(self):
        try:
            # Code to add a new column with the specified name and optional values
            pass
        except Exception as e:
            speak(f"An error occurred while adding a column")
            print(str(e))

    def drop_column(self):
        try:
            # Code to drop a column with the specified name
            pass
        except Exception as e:
            speak(f"An error occurred while dropping a column")
            print(str(e))

    def edit_column(self):
        try:
            # Code to edit a specific cell in a column
            pass
        except Exception as e:
            speak(f"An error occurred while editing a column")
            print(str(e))

    def get_row(self):
        try:
            # Code to get the data for a specific row
            pass
        except Exception as e:
            speak(f"An error occurred while getting a row")
            print(str(e))

    def set_row(self):
        try:
            # Code to set a new row at the specified index
            pass
        except Exception as e:
            speak(f"An error occurred while setting a row")
            print(str(e))

    def get_column(self):
        try:
            # Code to get the data for a specific column
            pass
        except Exception as e:
            speak(f"An error occurred while getting a column")
            print(str(e))

    def set_column(self):
        try:
            # Code to set a new column with the specified name
            pass
        except Exception as e:
            speak(f"An error occurred while setting a column")
            print(str(e))
