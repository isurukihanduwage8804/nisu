import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page setup
st.set_page_config(page_title="Nisu Nayama", page_icon="❤️")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ලස්සන Heart animation එකක්
lottie_heart = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_6aYlH6.json")

# --- UI එක සැකසීම ---

# Heading එක ගොඩක් ලොකුවට (Font size 80px)
st.markdown("""
    <h1 style='text-align: center; font-size: 80px; color: #ff4b4b; font-family: sans-serif;'>
        Nisu Nayama
    </h1>
    """, unsafe_allow_html=True)

# Animation එක මැදට
if lottie_heart:
    st_lottie(lottie_heart, height=300, key="heart")

st.write("---")

# ප්‍රශ්නය අහන කොටස
st.markdown("<h2 style='text-align: center;'>ඔයා මට කැමතිද? 😍</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button('ඔව්, ගොඩක්! ❤️'):
        st.balloons()
        st.success("මමත් ඔයාට ගොඩක් ආදරෙයි! 🥰")
        st.snow()

with col2:
    if st.button('නැහැ ☹️'):
        st.warning("අයියෝ... ඇයි ඒ? 💔")

# යටින් පොඩි Note එකක්
st.markdown("<br><p style='text-align: center; color: grey;'>Made with love by Isuru</p>", unsafe_allow_html=True)
