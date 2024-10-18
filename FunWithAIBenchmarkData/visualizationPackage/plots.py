########################################################################################################################################################################
# Name: Will Padgett, Sarah Mahan                                                                                                                                      #
# email:  padgetwg@mail.uc.edu, mahansa@mail.uc.edu                                                                                                                    #
# Assignment Number: Assignment 07                                                                                                                                     #
# Due Date:   10/22/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment: Add a data visualization to the provided project                                                                                #                                                                                                                                                                  
# Brief Description of what this module does.  this module plots the dataset                                                                                           #                                       
#                                                                                                                                                                      #
# Citations: GPT 4o                                                                                                                                                    #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plot_histogram(data: pd.DataFrame):
    """Create and display a histogram of word counts."""
    max_word_count = data['WordCount_Temp'].max()
    bin_size = int(max(1, max_word_count // 10))

    fig = px.histogram(
        data, x='WordCount_Temp', nbins=bin_size,
        title='Distribution of Word Counts Across Questions',
        labels={'WordCount_Temp': 'Number of Words in Question', 'count': 'Number of Questions'},
        template='plotly_dark', text_auto=True
    )
    fig.update_traces(marker_color='mediumaquamarine')
    fig.update_layout(bargap=0.1, showlegend=False)
    fig.show()

def plot_bar_chart(data: pd.DataFrame):
    """Create a bar chart of average word count per correct answer."""
    correct_answers_column = data.columns[-1]
    grouped_data = data.groupby(correct_answers_column)['WordCount_Temp'].mean().reset_index()
    grouped_data.columns = ['Correct Answer', 'Average Word Count']

    fig = px.bar(
        grouped_data, x='Correct Answer', y='Average Word Count',
        title='Average Word Count per Correct Answer',
        template='plotly_dark', color='Correct Answer',
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig.show()

def plot_most_common_words(most_common_words: pd.DataFrame):
    """Plot the top 10 most common words."""
    fig = px.bar(
        most_common_words, x='Word', y='Frequency',
        title='Top 10 Most Common Words in Questions',
        template='plotly_dark'
    )
    fig.show()

def plot_average_word_count_line(data: pd.DataFrame):
    """Plot a line graph of average word count across questions."""
    data['Average Word Count'] = data['WordCount_Temp'].expanding().mean()

    fig = px.line(
        data, x=data.index, y='Average Word Count',
        title='Average Word Count Across Questions',
        labels={'index': 'Question Index', 'Average Word Count': 'Average Words per Question'},
        template='plotly_dark'
    )
    fig.show()

def display_top_5_longest_questions(data: pd.DataFrame):
    """Display a table of the top 5 longest questions."""
    top_5_longest = data.nlargest(5, 'WordCount_Temp')

    fig = go.Figure(data=[go.Table(
        header=dict(values=['Question', 'Word Count'], fill_color='paleturquoise', align='left'),
        cells=dict(values=[top_5_longest.iloc[:, 0], top_5_longest['WordCount_Temp']],
                   fill_color='lavender', align='left')
    )])
    fig.update_layout(title='Top 5 Longest Questions')
    fig.show()
