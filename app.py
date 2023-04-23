

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
    st.write('<p style="font-size:20px; color:black;">Supervised Machine Learning | Python (Scikit-Learn, Pandas) | Streamlit </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">This machine learning project aims to identify peoples heart attack risk based on their medical attributes and to help healthcare providers.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">I created  a prediction  model using Supervised Machine Learning algorithm, then I developed a Web-App using Streamlit framework.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Heart%20Attack%20Prediction%20App-Machine%20Learning'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 2
    st.write('<p style="font-size:28px; color:black;">Business Analysis & Data Exploration</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">SQL | Tableau </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">In this project my aim was to explore in-depth a real world dataset using MySQL, and also to answer the business questions and visualize some of them using Tableau.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">In SQL part, I applied a variety of techniques, including table joins, case statements, aggregation functions, and subqueries.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/SQL%20Business%20Analysis-Data%20Exploration'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



      # 3
    st.write('<p style="font-size:28px; color:black;">Heart Attack Exploratory Data Analysis (EDA)</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Plotly, Pandas, Seaborn, Matplotlib) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">In this project my goal was to perform Exploratory Data Analysis using Heart Attack Dataset. </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">Firstly, I analyzed and explored the dataset then I created some enlightening visualizations using Python.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/blob/main/Heart%20Attack%20Exploratory%20Data%20Analysis/README.md'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")




    # 4
    st.write('<p style="font-size:28px; color:black;">Eniac Data Cleaning & Storytelling</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Pandas, Seaborn, Matplotlib)</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The main goal of this project is to implement the data cleaning and data quality process, which includes: </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">Evaluating and cleaning data to make it usable, evaluating the impact of discounts on sales/revenue, make a recommendation for more discounts. </p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Eniac%20Data%20Cleaning%20and%20Storytelling%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 5
    st.write('<p style="font-size:28px; color:black;">Interactive Dashboard Projects</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Tableau | Business Intelligence Tool</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">I love creating dynamic dashboards that help people see and understand their data using Tableau. These dashboards provides visibility at a glance, saves time and resources, improves decision making, simplifies performance checks.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">You can access my interactive dashboards from this link.</p>', unsafe_allow_html=True)
    # button
    url = 'https://public.tableau.com/app/profile/gozdebarin'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Projects</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")


    # 6
    st.write('<p style="font-size:28px; color:black;">House Prices Prediction</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Supervised Machine Learning | Python (Scikit-Learn, Pandas) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">In this project, I created  a prediction  model using Supervised Machine Learning algorithm to predict whether a house is expensive or not.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/House%20Prices%20Prediction-Machine%20Learning'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")


    

    # 7
    st.write('<p style="font-size:28px; color:black;">Spotify Clustering Songs</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Unsupervised Machine Learning | Python (Scikit-Learn, Pandas) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The purpose of this project is to cluster similar songs using K-means clustering algorithm and Spotipy API, thus automatically creating Spotify playlists.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Spotify%20Clustering%20Songs%20Unsupervised%20Machine%20Learning%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")




    # 8
    st.write('<p style="font-size:28px; color:black;">A/B Testing - Montana University Website Homepage </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Pandas) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The main purpose of this project is to perform an A/B Test to check CTR(click-through rate) for different text on a button on the website of Montana S. University.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Montana%20S.%20University%20A-B%20Testing%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Project</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")



    # 9
    st.write('<p style="font-size:28px; color:black;">Gans Data Engineering & Data Pipeline</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (BeautifulSoup, Pandas, Seaborn), Requests (API) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The aim of this project is to collect data from external sources that can potentially help Gans to predict e-scooter movement. </p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Gans%20Data%20Engineering%20Project'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Projects</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")




    # 10
    st.write('<p style="font-size:28px; color:black;">Movie Recommender System </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">Python (Scikit-Learn, Pandas) </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The main objective of this project will be to create 3 different recommender systems that give users from WBSFLIX relevant content to watch: Popularity Based Recommender, Item Based Recommender, User Based Recommender. </p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/Movie%20Recommender%20System'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Projects</button></a>
    ''',
    unsafe_allow_html=True)
    st.write("---")




    # 11
    st.write('<p style="font-size:28px; color:black;">Interactive Excel Dashboard  </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:20px; color:black;">MS Excel </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">I have created Dashboard using Excel to highlight the most important information and key performance indicators (KPIs) for Kevin Cookie Company.</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:16px; color:grey;">The dashboard is dynamic & interactive and adjusts depending on the country, months, and products selected via the slicer.</p>', unsafe_allow_html=True)
    # button
    url = 'https://github.com/gozdebarin/My_Portfolio_Projects/tree/main/MS%20Excel%20Interactive%20Dashboard'
    st.markdown(f'''
    <a href={url}><button style="background-color:#FAFAFA;">View Projects</button></a>
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


