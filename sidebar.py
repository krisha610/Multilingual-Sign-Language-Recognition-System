import streamlit as st


def render_sidebar():

    st.sidebar.title("Settings")

    confidence = st.sidebar.slider(
        "Detection Confidence",
        0.1,
        1.0,
        0.7,
        0.1
    )

    max_hands = st.sidebar.selectbox(
        "Maximum Hands",
        [1, 2]
    )

    return confidence, max_hands