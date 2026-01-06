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

# Heart animation එක
lottie_heart = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_6aYlH6.json")

# --- UI එක සැකසීම ---

# ප්‍රධාන Heading එක (ගොඩක් ලොකුවට)
st.markdown("""
    <h1 style='text-align: center; font-size: 80px; color: #ff4b4b; font-family: 'Arial Black', sans-serif;'>
        Nisu Nayama
    </h1>
    """, unsafe_allow_html=True)

# Animation එක
if lottie_heart:
    st_lottie(lottie_heart, height=300, key="heart")

st.write("---")

# ප්‍රශ්නය
st.markdown("<h2 style='text-align: center;'>ඔයා මට කැමතිද? 😍</h2>", unsafe_allow_html=True)

# Buttons දෙක මැදට ගන්න columns පාවිච්චි කිරීම
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button('ඔව්, ගොඩක්! ❤️'):
        st.balloons()
        st.success("මමත් ඔයාට ගොඩක් ආදරෙයි! 🥰")
        st.snow()

# යටින් වැටෙන ලස්සන Message එක
st.markdown("<br><br><p style='text-align: center; color: #ff4b4b; font-weight: bold; font-size: 20px;'>Made with love you Ayush</p>", unsafe_allow_html=True)
