import streamlit as st
import time

st.title("🥳🎂 Happy Birthday 🎈🎂")

audio_url = "Simi-Happy-Birthday.mp3" # Replace with your link

st.markdown( f"<audio autoplay loop style='display:none'> <source src='{audio_url}', type='audio/mp3'> </audio> ", unsafe_allow_html=True)
#st.audio("Simi-Happy-Birthday.mp3", autoplay= True, loop= True)

wishes = ["Happy Birthday, My Best! 🎉💖", "Ogunnike Motorola Oyindamola", "You’re more than a friend to me", "Thank you for filling my life with laughter, love, and endless memories.",  "I’m so grateful for every moment we’ve shared and excited for all the adventures ahead." , "May this year bring you joy as bright as your smile" , "Blessings as countless as your dreams", "and love that surrounds you always." , "You deserve nothing less than the absolute best today and forever. 💐✨"]

for wish in wishes:
     st.markdown(f"<p style='text-align: center;'>{wish}</p>", unsafe_allow_html=True)
     time.sleep(2)

#st.rerun()