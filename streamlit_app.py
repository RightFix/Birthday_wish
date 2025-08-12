import streamlit as st
import time

st.title("🥳 Happy Birthday 🎈")


wishes = ["Happy Birthday, My Best! 🎉💖", "Ogunnike Motorola Oyindamola", "You’re more than a friend to me", "Thank you for filling my life with laughter, love, and endless memories.",  "I’m so grateful for every moment we’ve shared and excited for all the adventures ahead." , "May this year bring you joy as bright as your smile" , "Blessings as countless as your dreams", "and love that surrounds you always." , "You deserve nothing less than the absolute best today and forever. 💐✨"]

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
   if st.button("click me"):
      st.audio("Simi-Happy-Birthday.mp3", loop=True, autoplay=True, width=2)

      for wish in wishes:
          st.markdown(f"<p style='text-align: center;'>{wish}</p>", unsafe_allow_html=True)
          time.sleep(2)

st.rerun()