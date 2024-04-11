import pandas as pd
import os

class Sharding:
    """
    A class used to split a CSV file into multiple smaller files.

    Attributes
    ----------
    filename : str
        the name of the CSV file to be split
    chunk_size : int
        the number of rows in each chunk

    Methods
    -------
    split_csv()
        Splits the CSV file into chunks and saves them as separate files.
    """

    def __init__(self, filename, chunk_size=1000):
        self.filename = filename
        self.chunk_size = chunk_size

    def split_csv(self):
        """
        Splits the CSV file into chunks and saves them as separate files.
        """
        df = pd.read_csv(self.filename)
        num_chunks = (len(df) + self.chunk_size - 1) // self.chunk_size

        self.__create_directory(f'{self.filename[:-4]}')
        for i in range(num_chunks):
            chunk = df[i * self.chunk_size:(i + 1) * self.chunk_size]
            chunk.to_csv(f'{self.filename[:-4]}/{self.filename[:-4]}_part{i+1}.csv', index=False)
        
        self.__delete_file()

    def __delete_file(self):
        # Check if file exists
        if os.path.exists(self.filename):
            # Delete the file
            os.remove(self.filename)
            print(f"File {self.filename} has been deleted successfully.")
        else:
            print(f"The file {self.filename} does not exist.")

    def __create_directory(self, dir_path):
        # Check if the directory already exists
        if not os.path.exists(dir_path):
            # Create the directory
            os.makedirs(dir_path)
            print(f"Directory '{dir_path}' created successfully.")
        else:
            print(f"Directory '{dir_path}' already exists.")
# Example usage
