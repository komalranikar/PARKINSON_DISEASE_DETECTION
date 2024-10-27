import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Parkinson's Disease Dataset Analysis")

# File upload
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    data = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.subheader("Dataset Preview")
    st.write(data.head())

    # Show dataset statistics
    st.subheader("Dataset Statistics")
    st.write(data.describe())

    # Select a feature for visualization
    feature = st.selectbox("Select a feature to visualize", data.columns)

    # Visualize the selected feature
    st.subheader(f"Distribution of {feature}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data[feature], bins=30, kde=True)
    st.pyplot(plt)

    # Correlation heatmap
    if st.checkbox("Show Correlation Heatmap"):
        st.subheader("Correlation Heatmap")
        plt.figure(figsize=(12, 8))
        correlation_matrix = data.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        st.pyplot(plt)


