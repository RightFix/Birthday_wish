import streamlit as st
import time

st.title("🥳🎂 Happy Birthday Motorola")

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", loop= True, autoplay= True)

wishes = ["Happy Birthday, My Best! 🎉💖", "Ogunnike Motorola Oyindamola", 
"You’re more than a friend  you’re family to me", "Thank you for filling my life with laughter, love, and endless memories.",  "I’m so grateful for every moment we’ve shared and excited for all the adventures ahead." , "May this year bring you joy as bright as your smile" , "blessings as countless as your dreams", "and love that surrounds you always." , "You deserve nothing less than the absolute best today and forever. 💐✨"]

for wish in wishes:
  st.write(wish)
  time.sleep(3)