import pandas as pd
# import numpy as np


class CSVEditor():
    def __init__(self, csv_file_path=None):
        self._csv_file_path = csv_file_path
        self._dataframe = pd.DataFrame()
        self._indices = 0
        self._columns = 0

    def save_csv(self, new_csv_file_path=None):
        """Save the current _dataframe to a CSV file."""
        if new_csv_file_path == None:
            self._dataframe.to_csv(self.csv_file_path, index=False)
        else:
            self._dataframe.to_csv(new_csv_file_path, index=False)

    def add_row(self, values=None):
        """Add a new row to the CSV."""
        newRow_index = len(self._dataframe)
        self._dataframe.loc[newRow_index] = values
        return newRow_index

    def drop_row(self, row_index):
        """Drop a row from the CSV."""
        self._dataframe.drop(row_index, inplace=True)

    def edit_row(self, new_value, row_index, *column_name):
        """Edit a specific row in the CSV."""
        if column_name != None:
            self._dataframe.loc[row_index, [*column_name]] = new_value

    def add_column(self, column_name=None, values=None):
        """Add a new column to the CSV."""
        if column_name == None:
            column_name = f'column. {self._dataframe.columns.__len__()}'
        self._dataframe.loc[:, column_name] = values

    def drop_column(self, column_name):
        """Drop a column from the CSV."""
        self._dataframe.drop(column_name, axis=1, inplace=True)

    def edit_column(self, column_name, *row_index, new_value):
        """Edit the values of a specific column in the CSV."""
        self._dataframe.loc[[*row_index], column_name] = new_value

    def get_dataframe(self):
        """Get the entire _dataframe of the CSV."""
        return self._dataframe

    def get_indices(self):
        """Get the entire _dataframe of the CSV."""
        return self._indices

    def get_cols(self):
        """Get the entire _dataframe of the CSV."""
        return self._columns

    def get_row(self, row_index):
        """Get a specific row from the CSV."""
        return self._dataframe.iloc[[row_index]]

    def set_row(self, row_index, new_row):
        """Edit a specific row in the CSV."""
        self._dataframe.iloc[row_index] = new_row

    def get_column(self, column_name):
        """Get a specific column from the CSV."""
        self._dataframe[[column_name]]

    def set_column(self, column_name, new_column):
        self._dataframe.loc[:, [column_name]] = new_column

    def get_cell(self, row_index, column):
        return self._dataframe.loc[row_index, column]

    def set_cell(self, row_index, column, new_value):
        self._dataframe.loc[[row_index], [column]] = new_value
        return self._dataframe.loc[[row_index], [column]]

    @property
    def csv_file_path(self):
        """Get the file path of the CSV."""
        return self._csv_file_path

    @csv_file_path.setter
    def csv_file_path(self, new_file_path):
        """Set the file path of the CSV."""
        self._csv_file_path = new_file_path


class CreateCSV(CSVEditor):
    def __init__(self, csv_filename):
        """Create a new CSV file with the given headers."""
        csv_filename = csv_filename + '.csv'
        super().__init__(csv_file_path=csv_filename)
        pd.DataFrame().to_csv(f'{csv_filename}')


class EditCSV(CSVEditor):
    def __init__(self, csv_file_path):
        """Load an existing CSV file."""
        csv_file_path = csv_file_path + '.csv'
        super().__init__(csv_file_path=csv_file_path)
        csv_ = pd.read_csv(csv_file_path)
        self._dataframe = csv_
        self.indices = csv_.index
        self.columns = csv_.columns
