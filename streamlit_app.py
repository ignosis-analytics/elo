import streamlit as st
from elo import rate_1vs1

result = rate_1vs1(800, 1200)

st.title("🎈 My new app")
st.write(
    "Let's start building WooHoo Hee! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(result)
