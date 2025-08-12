import streamlit as st
import time

st.title("🥳🎂 Happy Birthday Motorola")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", loop= True, autoplay= True)

wishes = []

for wish in wishes:
  st.write(wish)
  time.sleep(3)