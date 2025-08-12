import streamlit as st

st.title("🥳🎂 Happy Birthday Motorola")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


if 'show_widget' not in st.session_state:
    st.session_state.show_widget = True

st.checkbox("Toggle Widget Visibility", value=st.session_state.show_widget, key="toggle_visibility")

if st.session_state.toggle_visibility:
    st.text_input("This widget is visible", "Hello", key="visible_input")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", loop= True, autoplay= True)
else:
    st.write("Widget is hidden.")
