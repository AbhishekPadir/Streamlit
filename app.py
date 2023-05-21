import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def main():
    st.title('Perform Various Tests')

    # File uploader to browse and select the dataset file
    dataset_file = st.file_uploader('Upload dataset file', type=['csv'])

# File uploader to browse and select the dataset file
dataset_file = st.file_uploader('Upload dataset file', type=['csv'])

if dataset_file is not None:
    try:
        # Read the dataset file
        data = pd.read_csv(dataset_file)

        # Select the plot type
        plot_type = st.selectbox('Select Plot Type:', ['Line Chart', 'Scatter Plot', 'Pair Plot'])

        if plot_type == 'Line Chart':
            # Select the x-axis column
            x_column = st.selectbox('Select X-axis column:', data.columns)

            # Select the y-axis column
            y_column = st.selectbox('Select Y-axis column:', data.columns)

            # Select the value column
            value_column = st.selectbox('Select Value column:', data.columns)

            # Create a subset of the data with selected columns
            subset = data[[x_column, y_column, value_column]]

            # Group the data by x and y columns and calculate the average of the value column
            grouped_data = subset.groupby([x_column, y_column])[value_column].mean().reset_index()

            # Create the line chart
            fig, ax = plt.subplots()
            plt.plot(data[x_column], data[y_column])
            plt.xlabel(x_column)
            plt.ylabel(y_column)

            # Display the line chart
            st.pyplot(fig)

        elif plot_type == 'Scatter Plot':
            # Select the x-axis column
            x_column = st.selectbox('Select X-axis column:', data.columns)

            # Select the y-axis column
            y_column = st.selectbox('Select Y-axis column:', data.columns)

            # Create the scatter plot
            fig, ax = plt.subplots()
            plt.scatter(data[x_column], data[y_column])
            plt.xlabel(x_column)
            plt.ylabel(y_column)

            # Display the scatter plot
            st.pyplot(fig)

        elif plot_type == 'Pair Plot':
            # Select the x-axis column
            x_column = st.selectbox('Select X-axis column:', data.columns)

            # Select the y-axis column
            y_column = st.selectbox('Select Y-axis column:', data.columns)

            # Select the value column
            value_column = st.selectbox('Select Value column:', data.columns)

            # Create a subset of the data with selected columns
            # subset = data[[x_column, y_column, value_column]]

            # Group the data by x and y columns and calculate the average of the value column
            # grouped_data = subset.groupby([x_column, y_column])[value_column].mean().reset_index()

            # Create the pair plot
            pair_plot = sns.pairplot(data)

            # Display the pair plot
            st.pyplot(pair_plot)

    except pd.errors.EmptyDataError:
        st.error('Uploaded file is empty')
    except pd.errors.ParserError:
        st.error('Invalid file format. Please upload a CSV file.')



# Add some styling features
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #FF5722;
        color: white;
    }
    .stTextInput input {
        background-color: #F5F5F5;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

main()

# Add website interactive features
st.sidebar.header('Additional Features')

# Checkbox for data summary
if dataset_file is not None:
    if st.sidebar.checkbox('Show Data Summary'):
        st.subheader('Data Summary')
        st.write(data.describe())

# Select columns for correlation matrix
if dataset_file is not None:
    corr_columns = st.sidebar.multiselect('Select Columns for Correlation Matrix', data.columns)

    if corr_columns:
        # Compute correlation matrix
        corr_matrix = data[corr_columns].corr()

        # Display correlation matrix as a heatmap
        st.subheader('Correlation Matrix')
        st.write(corr_matrix)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        st.pyplot()

# Additional interactive features...
