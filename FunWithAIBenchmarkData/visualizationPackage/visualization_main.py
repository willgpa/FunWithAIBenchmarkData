########################################################################################################################################################################
# Name: Will Padgett, Sarah Mahan                                                                                                                                      #
# email:  padgetwg@mail.uc.edu, mahansa@mail.uc.edu                                                                                                                    #
# Assignment Number: Assignment 07                                                                                                                                     #
# Due Date:   10/22/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment: Add a data visualization to the provided project                                                                                #                                                                                                                                                                  
# Brief Description of what this module does.  This module calls the visualization functions                                                                           #                                       
#                                                                                                                                                                      #
# Citations: GPT 4o                                                                                                                                                    #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################
from visualizationPackage.data_loader import load_data
from visualizationPackage.data_processing import (
    add_word_count_columns, get_most_common_words
)
from visualizationPackage.plots import (
    plot_histogram, plot_bar_chart, plot_most_common_words,
    plot_average_word_count_line, display_top_5_longest_questions
)

def run_visualization():
    """Run all visualizations."""
    data = load_data()
    if data.empty:
        print("Data could not be loaded.")
        return

    # Add word count columns
    data = add_word_count_columns(data)

    # 1. Histogram of Word Counts
    plot_histogram(data)

    # 2. Bar Chart of Average Word Count per Correct Answer
    plot_bar_chart(data)

    # 3. Top 10 Most Common Words
    most_common_words = get_most_common_words(data)
    plot_most_common_words(most_common_words)

    # 4. Line Graph of Average Word Count Across Questions
    plot_average_word_count_line(data)

    # 5. Display Top 5 Longest Questions
    display_top_5_longest_questions(data)

if __name__ == "__main__":
    run_visualization()
