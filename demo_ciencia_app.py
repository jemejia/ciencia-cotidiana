# Import necessary libraries
import streamlit as st
import pandas as pd
import altair as alt

# Define function to generate histograms
def generate_histogram(file):
    # Read CSV file
    df = pd.read_csv(file)

    # Get columns with categorical or binary data
    categorical_cols = df.select_dtypes(include=['category', 'bool']).columns.tolist()

    # Generate histogram for each categorical or binary column
    for col in categorical_cols:
        chart = alt.Chart(df).mark_bar().encode(
            alt.X(col),
            y='count()'
        ).properties(title=f"Histogram for {col}")
        st.altair_chart(chart, use_container_width=True)

# Define Streamlit app
def app():
    st.title("Histogram Generator")

    # Upload CSV file
    file = st.file_uploader("Upload CSV file", type=['csv'])

    if file is not None:
        # Retrieve histogram
        generate_histogram(file)

# Run Streamlit app
if __name__ == '__main__':
    app()
