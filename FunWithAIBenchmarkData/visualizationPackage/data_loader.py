########################################################################################################################################################################
# Name: Will Padgett, Sarah Mahan                                                                                                                                      #
# email:  padgetwg@mail.uc.edu, mahansa@mail.uc.edu                                                                                                                    #
# Assignment Number: Assignment 07                                                                                                                                     #
# Due Date:   10/22/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment: Add a data visualization to the provided project                                                                                #                                                                                                                                                                  
# Brief Description of what this module does.  this module loads the dataset                                                                                           #                                       
#                                                                                                                                                                      #
# Citations: GPT 4o                                                                                                                                                    #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################

from pathlib import Path
import pandas as pd
from pathlib import Path
import pandas as pd

def get_data_path() -> Path:
    """Return the path to the dataset."""
    base_dir = Path(__file__).resolve().parent.parent
    return base_dir / "dataPackage" / "MMLU" / "data" / "college_chemistry_test.csv"

def load_data() -> pd.DataFrame:
    """Load the dataset and return a DataFrame."""
    data_path = get_data_path()
    print(f"Looking for file at: {data_path}")

    if not data_path.exists():
        print(f"Error: The file {data_path} was not found.")
        return pd.DataFrame()

    try:
        data = pd.read_csv(data_path)
        print(f"Successfully loaded data from: {data_path}")
        return data
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return pd.DataFrame()
