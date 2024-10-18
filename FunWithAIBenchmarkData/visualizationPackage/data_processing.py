########################################################################################################################################################################
# Name: Will Padgett, Sarah Mahan                                                                                                                                      #
# email:  padgetwg@mail.uc.edu, mahansa@mail.uc.edu                                                                                                                    #
# Assignment Number: Assignment 07                                                                                                                                     #
# Due Date:   10/22/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment: Add a data visualization to the provided project                                                                                #                                                                                                                                                                  
# Brief Description of what this module does.  this module processes the data                                                                                          #                                       
#                                                                                                                                                                      #
# Citations: GPT 4o                                                                                                                                                    #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################

import pandas as pd
from collections import Counter

def add_word_count_columns(data: pd.DataFrame) -> pd.DataFrame:
    """Add temporary word count and cumulative word count columns."""
    data['WordCount_Temp'] = data.iloc[:, 0].str.split().apply(len)
    data['Cumulative Word Count'] = data['WordCount_Temp'].cumsum()
    return data

def get_most_common_words(data: pd.DataFrame, n=10) -> pd.DataFrame:
    """Extract the n most common words from the first column."""
    all_words = ' '.join(data.iloc[:, 0]).split()
    return pd.DataFrame(Counter(all_words).most_common(n), columns=['Word', 'Frequency'])
