import streamlit as st
st.title('My Portfolio')
st.text("")
from PIL import Image
image = Image.open("maaz.jpg")

st.sidebar.image(image,use_column_width=True)
st.sidebar.title('Maaz Ansari')
st.sidebar.text('B.Tech Data Science')

import webbrowser

if st.sidebar.button("About"):
    st.header('About')
    st.write('I am currently a 4th year student prusuing B.Tech Data Science from NMIMS University, Mumbai, India. Im a fast learner and I try to indulge myself in new activities and new challenges. I have a handful of experience in Machine learning and Deep learning now for 3 years. I am thorough with languages like Python and R and I wish to pursue my career as a Machine learning engineer. Apart from ML, I am passionate about analyzing data and using the information obtained to solve business problems.')
    st.write('Interests: Data Science | Machine Learning | Deep Learning | Natural Language Processing | Data Analytics | Time Series | Economics')
    
    
if st.sidebar.button("Skills"):
    #st.header('Programming Languages:')
    #st.image(Image.open(r"C:\Users\Maaz\Downloads\lang.png"))
    
    #st.header('Tools:')
    #st.image(Image.open(r"C:\Users\Maaz\Downloads\sk_22.png"))
    
    #st.header('Technical Knowledge:')
    #st.image(Image.open(r"C:\Users\Maaz\Downloads\ski_2.png"))
    
    
    
    
if st.sidebar.button("Projects"):
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Flight Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    #st.header('Flight Price Prediction')
    st.text("")
    st.image(Image.open("fp.gif"))
    if st.button("Demo",key='FPP'):
        webbrowser.open_new_tab('https://strea1.herokuapp.com/')
        
    st.text("")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Automated Attendance System using Face Recognition</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("")
    #st.header('Automated Attendance System using Face Recognition')
    #st.image(Image.open(r"C:\Users\Maaz\Downloads\aas.jpg"))
    if st.button("Demo",key='AAS'):
        webbrowser.open_new_tab('')

    st.text("")    
    st.header('Zomato Interactive Dashboard using Python (Voila)')
    if st.button("Demo",key='ZID'):
        webbrowser.open_new_tab('')
        
#     st.header('Flight Price Prediction')
#     if st.button("Demo"):
#         webbrowser.open_new_tab(url)
     
    
if st.sidebar.button("Experience"):
    st.header('Experience')
    st.subheader('Data Analyst Internship at Terracon Ecotech Pvt Ltd. – Mumbai (May 2019 – June 2019)')
    st.write('Project MMR - To apply machine learning algorithms and predictive analysis on the given data after data cleaning in order to produce actionable insights for the company.')
    st.text('')
    st.text('')
    st.subheader('Data Science Internship at Dimensionless Technologies. – Mumbai (April 2020 – Ongoing)')
    st.write('1. Create content for the Data Science and Artificial Intelligence Course.')
    st.write('2. Create and Host Kaggle Competition.')
    st.write('3. Making new case studies in R & Python.')

    
if st.sidebar.button("Achievements"):
    st.header('Achievements')
    st.write('• Data Science Technical Project Competition: 1st Place.')
    st.write('• U’lectro: 2nd Place & won a sponsored trip to Singapore for attending International Innovation and Technology Conference.')
    st.write('• International Innovation and Technology Conference in Singapore – Sponsored Trip.')
    st.write('• Inter-College Live Technical Project Competition held by MHRD’s Innovation Cell (Govt. of India): 1st Place.')
    st.write('• ResCon Data Analysis Competition: 1st Place.')
    st.write('• 4C The Marketing Cell: 1st Place in MJAM.')
    st.write('• Mr. and Miss. University, Top Ten Finalist.')
    st.write('• Trophy for social studies, highest marks in History, Geography and Economics.')
    st.write('• House Captain (2014-2015)')
    
   
    
if st.sidebar.button("Hobbies & Interests"):
    st.header('Hobbies & Interests')
    st.write('• Playing Chess, Volleyball, Football and Badminton.')
    st.write('• Learning new languages like French, German.')
    st.write('• Trekking')
    st.write('• Travelling')

    
# st.beta_color_picker('Pick A Color', '#00f900')