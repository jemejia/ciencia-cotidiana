# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.title("CSV Data Visualization")
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     st.write("Data Overview:")
#     st.dataframe(data.head())

#     st.sidebar.title("Visualization Settings")
#     column = st.sidebar.selectbox("Select a column to plot", data.columns)
#     plot_height = st.sidebar.slider("Plot height", 4, 12, 6)
#     plot_aspect = st.sidebar.slider("Plot aspect ratio", 1, 4, 2)
#     A="¿Con cuál género se identifica?"
#     if column != A:

#         st.write(f"Visualizing '{column}' segregado por '{A}'")
#         g = sns.FacetGrid(data, col=A, margin_titles=True, height=plot_height, aspect=plot_aspect)
#         g.map(plt.hist, column)

#         st.pyplot(g.fig)

#     else:
#         st.write(f"Please select any column other than '{A}' to visualize.")

# else:
#     st.write("Please upload a CSV file to explore its data.")


import streamlit as st
import pandas as pd
import plotly.express as px



st.title("CSV Data Visualization")
standard_question_header = "Por favor asigne un “verdadero ” o “falso” a las siguientes afirmaciones según considere: "
standard_value_header = "En una escala de 1 a 7, donde 1 significa “totalmente en desacuerdo”, 4 “neutro” y 7 “totalmente de acuerdo” valore las siguientes afirmaciones: "
standard_knowledge_header = "En una escala de 1 a 7 donde 1 significa “no estoy informado” y 7 “estoy bien informado” valore su conocimiento sobre los siguientes temas: "
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)    
    data.columns = [col  if standard_question_header not in col else col[len(standard_question_header):] for col in data.columns]
    data.columns = [col  if standard_value_header not in col else col[len(standard_value_header):] for col in data.columns]
    data.columns = [col  if standard_knowledge_header not in col else col[len(standard_knowledge_header):] for col in data.columns]
    A="¿Con cuál género se identifica?"
    A=st.sidebar.selectbox("Select a column to segregate by", data.columns)
    data_1 = data.dropna(subset=[A])
    st.write("Data Overview:")
    st.dataframe(data.head())

    st.sidebar.title("Visualization Settings")
    column = st.sidebar.selectbox("Select a column to plot", data.columns)

    if column != A:

        st.write(f"Visualizing '{column}' segregado por {A}")
        fig = px.histogram(
            data_1,
            x=column,
            color=A,
            nbins=50,
            title=f"Visualizing '{column}' segregado por {A}"
        )

        st.write(fig)

    else:
        st.write(f"Please select any column other than {A} to visualize.")
        
else:
    st.write("Please upload a CSV file to explore its data.")