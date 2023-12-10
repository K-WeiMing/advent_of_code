"""
Helper function to read in the data based on the current folder structure
"""
import os

def load_data():
    f_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file_name = "inputs.txt"
    f_path = os.path.join(f_path,"inputs" ,input_file_name)
    print(f_path)
    with open(f_path, "r") as file:
        data = file.readlines()
        
    # Replace '\n' in the inputs
    data = [str(i.replace("\n", "")) for i in data]
    return data
