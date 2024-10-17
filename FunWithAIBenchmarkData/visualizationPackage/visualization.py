########################################################################################################################################################################
# Name: Will Padgett, Sarah Mahan                                                                                                                                      #
# email:  padgetwg@mail.uc.edu, mahansa@mail.uc.edu                                                                                                                    #
# Assignment Number: Assignment 07                                                                                                                                     #
# Due Date:   10/22/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment: Add a data visualization to the provided project                                                                                #                                                                                                                                                                  
# Brief Description of what this module does.  this module loads the dataset and does multiple maniputalions before displaying results in a data visualization         #                                       
#                                                                                                                                                                      #
# Citations: GPT 4o                                                                                                                                                    #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################




from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def load_data():
    """Load the dataset from the specified path."""
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / "dataPackage" / "MMLU" / "data" / "college_chemistry_test.csv"

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

def get_most_common_words(data, n=10):
    """Extract the n most common words from the first column."""
    all_words = ' '.join(data.iloc[:, 0]).split()
    most_common = Counter(all_words).most_common(n)
    return pd.DataFrame(most_common, columns=['Word', 'Frequency'])

def run_visualization():
    """Run all visualizations."""
    data = load_data()
    if data.empty:
        print("Data could not be loaded.")
        return

    # Add Word Count and Cumulative Word Count columns if they don't exist
    if 'WordCount_Temp' not in data.columns:
        data['WordCount_Temp'] = data.iloc[:, 0].str.split().apply(len)

    if 'Cumulative Word Count' not in data.columns:
        data['Cumulative Word Count'] = data['WordCount_Temp'].cumsum()

    # 1. Enhanced Word Count Distribution Histogram
    try:
        max_word_count = data['WordCount_Temp'].max()
        bin_size = int(max(1, max_word_count // 10))  # Ensure bin_size is an int

        fig1 = px.histogram(
            data,
            x='WordCount_Temp',
            nbins=bin_size,
            title='Distribution of Word Counts Across Questions',
            labels={
                'WordCount_Temp': 'Number of Words in Question',
                'count': 'Number of Questions'
            },
            template='plotly_dark',
            text_auto=True,
            hover_data={'WordCount_Temp': True}
        )

        fig1.update_traces(marker_color='mediumaquamarine')
        fig1.update_layout(
            xaxis_title='Number of Words in Each Question',
            yaxis_title='Number of Questions',
            showlegend=False,
            bargap=0.1
        )

        fig1.show()
    except Exception as e:
        print(f"An error occurred while creating the histogram: {e}")

    # 2. Colorful Bar Chart: Average Word Count per Correct Answer
    try:
        correct_answers_column = data.columns[-1]
        grouped_data = data.groupby(correct_answers_column)['WordCount_Temp'].mean().reset_index()
        grouped_data.columns = ['Correct Answer', 'Average Word Count']

        fig2 = px.bar(
            grouped_data,
            x='Correct Answer',
            y='Average Word Count',
            title='Average Word Count per Correct Answer',
            labels={'Correct Answer': 'Answer Option', 'Average Word Count': 'Avg. Words per Question'},
            template='plotly_dark',
            color='Correct Answer',
            color_discrete_sequence=px.colors.qualitative.Vivid
        )
        fig2.show()
    except Exception as e:
        print(f"An error occurred while creating the colorful bar chart: {e}")

    # 3. Bar Chart: Top 10 Most Common Words in Questions
    most_common_words = get_most_common_words(data, n=10)
    fig3 = px.bar(
        most_common_words,
        x='Word',
        y='Frequency',
        title='Top 10 Most Common Words in Questions',
        labels={'Word': 'Word Used', 'Frequency': 'Number of Occurrences'},
        template='plotly_dark'
    )
    fig3.show()

   # 4. Average Word Count Line Graph
    try:
        # Compute average word count up to each question index
        data['Average Word Count'] = data['WordCount_Temp'].expanding().mean()

        fig4 = px.line(
            data,
            x=data.index,
            y='Average Word Count',
            title='Average Word Count Across Questions',
            labels={
                'index': 'Question Index',
                'Average Word Count': 'Average Words per Question'
            },
            template='plotly_dark'
        )

        fig4.update_layout(
            xaxis_title='Question Index',
            yaxis_title='Average Words per Question'
        )

        fig4.show()
    except Exception as e:
        print(f"An error occurred while creating the average word count line graph: {e}")


    # 5. Display Top 5 Longest Questions
    try:
        top_5_longest = data.nlargest(5, 'WordCount_Temp')
        fig5 = go.Figure(
            data=[go.Table(
                header=dict(
                    values=['Question', 'Word Count'],
                    fill_color='paleturquoise',
                    align='left'
                ),
                cells=dict(
                    values=[
                        top_5_longest.iloc[:, 0],  # Questions
                        top_5_longest['WordCount_Temp']  # Word counts
                    ],
                    fill_color='lavender',
                    align='left'
                )
            )]
        )
        fig5.update_layout(
            title='Top 5 Longest Questions'
        )
        fig5.show()
    except Exception as e:
        print(f"An error occurred while creating the top 5 questions table: {e}")


if __name__ == "__main__":
    run_visualization()
