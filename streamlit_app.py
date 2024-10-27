# Import necessary libraries
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved Parkinson's disease prediction model
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Disease Prediction System',
        ['Parkinsons Prediction'],
        icons=['person'],
        default_index=0
    )

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    # Page title
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields for Parkinson's disease-related parameters
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Code for prediction
    parkinsons_diagnosis = ''

    # Prediction button
    if st.button("Parkinson's Test Result"):
        try:
            # Convert inputs to float
            input_data = [
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR),
                float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2),
                float(D2), float(PPE)
            ]

            # Predict using the input data
            parkinsons_prediction = parkinsons_model.predict([input_data])

            # Determine the result
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

            # Display the result
            st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Please enter valid numeric values for all parameters.")
