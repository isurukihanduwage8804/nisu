import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page configuration
st.set_page_config(page_title="Nisu Nayama", page_icon="❤️")

# Lottie animation load කරගන්න function එක
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Heart animation එකක URL එකක් (LottieFiles හරහා)
lottie_heart = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_6aYlH6.json")

# Header එක
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Nisu Nayama</h1>", unsafe_allow_html=True)

# Animation එක display කිරීම
if lottie_heart:
    st_lottie(lottie_heart, height=300, key="heart")

# පොඩි message එකක්
st.markdown("<h3 style='text-align: center;'>සතුටින් ඉන්න හැමදාම! ❤️</h3>", unsafe_allow_html=True)

# තව හදවත් විසිවෙන effect එකක් (Snow effect එක heart වලට modify කරලා)
if st.button('Click for Surprise! 🎁'):
    st.balloons()
    st.snow() # මෙතනදි streamlit වල stars/snow වගේ වැටෙනවා
