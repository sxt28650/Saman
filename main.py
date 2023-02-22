import configparser
from file_reader import read_file

config = configparser.ConfigParser()
config.read('config.ini')

source_file_path = config.get('FILE_PATHS', 'source_file')
destination_file_path = config.get('FILE_PATHS', 'destination_file')

source_file_contents = read_file(source_file_path)

with open(destination_file_path, 'w') as file:
    file.write(source_file_contents)
