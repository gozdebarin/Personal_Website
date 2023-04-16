

# ---- IMPORT LIBRARIES ----
import requests
import streamlit as st

# option menu
from streamlit_option_menu import option_menu # pip install streamlit-option-menu

# images
from PIL import Image

# animations
from streamlit_lottie import st_lottie  # pip install streamlit-lottie




# ---- LOAD IMAGES & ANIMATIONS ----
# load images
img_info1 = Image.open("images/info1.jpg")
img_info2 = Image.open("images/info2.jpg")



# browser and general layout
st.set_page_config(page_title="Gözde Barın",
                   page_icon=":sparkles:",
                   layout="centered",
                   initial_sidebar_state="expanded")





# ---- OPTION MENU ----
with st.sidebar:
    selected = option_menu("Menu", ["Home",  "About Me", "My Portfolio Projects", 'Contact'], 
                           icons=['bi-house', 'file-person', 'bi-journals', 'envelope'],
                           menu_icon="cast", default_index=0,
                           orientation="vertical",
                           styles={
        "container": {"padding": "5!important", "background-color": "#E6DDCF"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#D0B8A8"},
    }
    )   
    st.write("---")



# 1) Home Section

if selected == 'Home':
    st.image(img_info1)

    st.write("[Learn More >>](https://pythonandvba.com)")
    



# 2) About Me Section

if selected == 'About Me':
    st.title("About Me")
    st.write("---")
    st.image(img_info2)

 


# 2) My Portfolio Projects

if selected == 'My Portfolio Projects':
    st.title("My Portfolio Projects")
    st.write("---")





# 4) Contact Form Section
if selected == 'Contact':
    st.title("Contact")
    st.write("---")
    st.write('<p style="font-size:18px; color:grey;">Please fill out the contact form.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:18px; color:grey;">I will get in touch with you as soon as possible!</p>', unsafe_allow_html=True)


    contact_form = """
    <form action="https://formsubmit.co/gozdemadendere@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email address" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
            
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    local_css("style/style.css")
         
    

    st.write("---")
    st.write('<p style="font-size:22px; color:grey;">Connect with me:</p>', unsafe_allow_html=True)
    st.write("[LinkedIn](https://www.linkedin.com/in/gozdebarin/) | [Github](https://github.com/gozdebarin) | [Tableau](https://public.tableau.com/app/profile/gozdebarin) | [Medium](https://medium.com/@gozdebarin)")

