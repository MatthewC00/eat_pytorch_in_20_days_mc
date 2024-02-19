import streamlit as st 
import plotly.express as px 
import time
import pandas as pd 

st.title('streamlit控件范例')

st.header("1，button")

#button常用于启动一段费时代码的执行
if st.button("Start count sheep"):
    msg = st.empty() #st.empty可以作为占位符
    for i in range(1,11):
        msg.write("{} sheep...".format(i))
        time.sleep(0.3)
else:
    pass #st.stop

st.header("2，selectbox") 

stock = st.selectbox(label = "Choose a stock",options=["GOOG","AAPL","AMZN","FB"])

st.write('You selected:', stock)

fig = px.line(data_frame=px.data.stocks(),x="date",y=[stock]) 

st.plotly_chart(fig)

st.header("3，number_input") 

st.write("input x and y to eval x+y:")
x = st.number_input("x",min_value=-10000,max_value=10000)
y = st.number_input("y",min_value=0,max_value=8)
st.write('x+y=', x+y)


st.header("4，slider") 

st.write("slide to choose your age:")
age = st.slider(label="age",min_value=0,max_value=120)

st.write('your age is ', age)


st.header("5，text_input") 

st.write("what's your name")
name = st.text_input(label="name",max_chars=100)
st.write("your name is ",name)

st.header("6，text_area") 

st.write("give an introduction of  yourself")
name = st.text_area(label="introduction",max_chars=1024)


st.header("7，download_button") 

@st.cache
def save_csv():
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    df = px.data.stocks()
    return df.to_csv().encode('utf-8')

csv = save_csv()

st.download_button(
     label="Download stock data",
     data=csv,
     file_name='stocks.csv',
     mime='text/csv',
 )

st.header("8，file_uploader")  

csv_file = st.file_uploader("Choose a csv file")

if csv_file is not None:
    try:
        dfstocks = pd.read_csv(csv_file)
        st.table(dfstocks)
    except Exception as err:
        st.write(err)
        
image_file = st.file_uploader("choose a image file(jpg/png)")
if image_file is not None:
    try:
        st.image(image_file)
    except Exception as err:
        st.write(err)
