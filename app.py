

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
img_info3 = Image.open("images/info3.jpg")


# browser and general layout
st.set_page_config(page_title="Gözde Barın",
                   page_icon=":sparkles:",
                   layout="centered",
                   initial_sidebar_state="expanded")





# ---- OPTION MENU ----
with st.sidebar:
    selected = option_menu("Menu", ["Portfolio Projects", "About Me",  'Contact'], 
                           icons=['bi-journals','file-person',  'envelope'],
                           menu_icon="cast", default_index=0,
                           orientation="vertical",
                           styles={
        # sidebar style
        "container": {"padding": "5!important", "background-color": "#F6F5F2"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#EBE5DB"},
        "nav-link-selected": {"background-color": "#D0B8A8"},
    }
    )   
    st.write("---")


# 1) My Portfolio Projects

if selected == 'Portfolio Projects':
    st.image(img_info3)
    st.write("---")

    # 1
    st.write('<p style="font-size:28px; color:black;">Heart Attack Prediction App</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Scikit-Learn, Pandas, Matlotlib, Plotly) | Streamlit </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">In this project, my aim was to identify the heart attack risk for people, based on their medical attributes. Therefore I developed an App, that quickly calculates heart attack risk to help healthcare providers.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">I created  a prediction  model using Supervised machine-learning algorithm, then I built a Web-Application using Streamlit framework.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/Heart_Attack_Prediction_App'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 2
    st.write('<p style="font-size:28px; color:black;">Business Analysis & Data Exploration</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">SQL | Tableau </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">My aim was to explore in-depth a real world dataset using MySQL and also to answer the business questions.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">I applied a variety of techniques, including table joins, case statements, aggregation functions.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/SQL%20Business%20Analysis-Data%20Exploration'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 3
    st.write('<p style="font-size:28px; color:black;">Data Cleaning and Storytelling</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Pandas, Seaborn, Matplotlib)</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The main goal of this project is to implement the data cleaning and data quality process, which includes: Evaluating and cleaning data to make it usable, evaluating the impact of discounts on sales/revenue, make a recommendation for more discounts. </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">I applied a variety of techniques, including table joins, case statements, aggregation functions.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Python%20Data%20Cleaning%20and%20Storytelling%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 4
    st.write('<p style="font-size:28px; color:black;">Interactive Dashboard Projects</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Tableau </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">I love creating dynamic dashboards that help people see and understand their data using Tableau Business Intelligence tool. </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">You can access my interactive dashboards from this link.</p>', unsafe_allow_html=True)
    # button
    url = 'https://public.tableau.com/app/profile/gozdebarin'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Projects</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 5
    st.write('<p style="font-size:28px; color:black;">Gans Data Engineering & Data Pipeline</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Pandas, Seaborn) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The main objective of my project is to learn the data engineering process which contains: </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">- Collect data: data collection via web scraping or Application Programming Interfaces (APIs)</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">- Set up a local database on MySQL: a database creation in MySQL for data storage</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">- Create a Data Pipeline to the Cloud: use Amazon Web Services (AWS) to move the pipeline to the cloud</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">- Automate the Data Pipeline: automate the whole data collection and storage process</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Gans%20Data%20Engineering%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Projects</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")

    # 6
    st.write('<p style="font-size:28px; color:black;">A/B Testing Project for Montana S. University </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Pandas) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">In this project, we analyzed an AB-test to check CTR for different text on a button on the website of a University Library in Montana.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Montana%20S.%20University%20A-B%20Testing%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 7
    st.write('<p style="font-size:28px; color:black;">House Prices Prediction</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Scikit-Learn, Pandas) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">In this project, I created  a prediction  model using Supervised machine-learning algorithm to predict whether a house is expensive or not.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/House%20Prices%20Prediction-Machine%20Learning'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 8
    st.write('<p style="font-size:28px; color:black;">Youtube Web Scraping - EDA Project</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Pandas, Seaborn, Matplotlib) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The purpose of this project is to gain some insights that might be useful to new creators. I will explore the statistics of a successful data science Youtube channel.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The steps of the project are obtaining video metadata for the channel via Youtube API, preprocessing the data and designing additional features for analysis, and performing exploratory data analysis.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Youtube%20Web%20Scraping%20-%20EDA%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")





# 2) About Me Section

if selected == 'About Me':
    st.title("About Me")
    st.write("---")
    st.image(img_info1)
    st.image(img_info2)


    


# 3) Contact Form Section
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
         
    


    

    # --- SOCIAL LINKS ---
    SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gozdebarin/",
    "GitHub": "https://github.com/gozdebarin",
    "Tableau": "https://public.tableau.com/app/profile/gozdebarin",
    "Medium": "https://medium.com/@gozdebarin",
    }

    st.write('\n')
    st.write("---")
    st.write('<p style="font-size:22px; color:grey;">Connect with me:</p>', unsafe_allow_html=True)
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


