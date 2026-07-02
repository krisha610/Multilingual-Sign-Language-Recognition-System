import streamlit as st


def show_metrics(count):

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Detected Fingers",
            value=count
        )

    with col2:
        st.metric(
            label="Gesture",
            value=str(count)
        )