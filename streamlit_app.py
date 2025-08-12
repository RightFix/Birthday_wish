import streamlit as st
import time
import base64

title = "🥳 Happy Birthday Best 🎈"
st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)

# Path to your local audio file
file_path = "Simi-Happy-Birthday.mp3"

# Read and encode file to Base64
with open(file_path, "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode()

# Title
#st.title("🎉 Birthday Song Player")

# HTML + JavaScript for autoplay
st.markdown(
    f"""
    <audio id="myAudio" src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3"></audio>
    <script>
        var audio = document.getElementById('myAudio');
        var playPromise = audio.play();

        if (playPromise !== undefined) {{
            playPromise.catch(() => {{
                // Autoplay failed, retry on first click
                document.addEventListener('click', () => {{
                    audio.play();
                }}, {{once:true}});
            }});
        }}
    </script>
    """,
    unsafe_allow_html=True
)

wishes = ["Happy Birthday, My Best! 🎉💖", "Ogunnike Motorola Oyindamola", "You’re more than a friend to me", "Thank you for filling my life with laughter, love, and endless memories.",  "I’m so grateful for every moment we’ve shared and excited for all the adventures ahead." , "May this year bring you joy as bright as your smile" , "Blessings as countless as your dreams", "and love that surrounds you always." , "You deserve nothing less than the absolute best today and forever. 💐✨"]

for wish in wishes:
      st.markdown(f"<p style='text-align: center;'>{wish}</p>", unsafe_allow_html=True)
      time.sleep(2)
#st.audio("Simi-Happy-Birthday.mp3", loop=True, autoplay=True, width=301)
st.rerun()