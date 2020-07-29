import streamlit as st

st.title('My Portfolio')
st.text("")
from PIL import Image
image = Image.open("maaz.jpg")

st.sidebar.image(image,use_column_width=True)
st.sidebar.title('Maaz Ansari')
st.sidebar.text('B.Tech Data Science')

if st.sidebar.button("About"):
    st.header('About')
    st.write('I am currently a 4th year student prusuing B.Tech Data Science from NMIMS University, Mumbai, India. Im a fast learner and I try to indulge myself in new activities and new challenges. I have a handful of experience in Machine learning and Deep learning now for 3 years. I am thorough with languages like Python and R and I wish to pursue my career as a Machine learning engineer. Apart from ML, I am passionate about analyzing data and using the information obtained to solve business problems.')
    st.write('Interests: Data Science | Machine Learning | Deep Learning | Natural Language Processing | Data Analytics | Time Series | Economics')
    
    st.header('Contact Information')
    st.text("")
    
    html_temp = """
    <a href="https://github.com/maaz-ansari" target="_blank">GitHub</a>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
        
    st.text("")
    
    html_temp = """
    <a href="https://www.linkedin.com/in/maaz-ansari-755360166/" target="_blank">LinkedIN</a>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
        
    st.text("")
    st.write('Phone: +91 9022169400')
    st.write('E-mail: maaz.ansari1721@nmims.edu.in')
    
    
    
if st.sidebar.button("Skills"):
    st.header('Programming Languages:')
    st.image(Image.open("lang.PNG"))
    
    st.header('Tools:')
    st.image(Image.open("sk_22.png"))
    
    st.header('Technical Knowledge:')
    st.image(Image.open("ski_2.PNG"))
    
    

    
if st.sidebar.button("Projects"):
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Movie/Book Review Spoiler Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("")
    st.image(Image.open("sp.jpg"))
    
    html_temp = """
    <a href="https://spoiler-prediction.herokuapp.com/" target="_blank">Demo</a>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
        
    st.text("")
    
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Flight Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("")
    st.image(Image.open("fpp.gif"))
    
    html_temp = """
    <a href="https://strea1.herokuapp.com/" target="_blank">Demo</a>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
        
    st.text("")
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Automated Attendance System using Face Recognition</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("")
    st.image(Image.open("aas.jpg"))
    html_temp = """
    <a href="" target="_blank">Reseach Paper</a>
    """
    st.markdown(html_temp, unsafe_allow_html=True)


    st.text("")    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Zomato Interactive Dashboard using Python (Voila)</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("")
    st.image(Image.open("zom.jpg"))
    html_temp = """
    <a href="https://zomatodash.herokuapp.com/" target="_blank">Demo</a>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("")
        
     
    
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