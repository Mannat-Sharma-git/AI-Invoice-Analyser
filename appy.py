import streamlit as st

st.title('Welcome to My Streamlit')

#input

m1 = st.text_input('Enter Your Input :')
st.markdown(m1)

m2 = st.text_area('Enter Your Prompt :')
st.markdown(m2)

st.warning('Please Enter your input')

st.success('Updated Successfully')

m3 = st.selectbox('Please select' , ['Python','Java','SQL'])

st.markdown(m3)

m4 = st.multiselect('Please select' , ['Python','Java','SQL'])
st.markdown(m4)

st.sidebar.text_input('Enter Your Name ')
st.sidebar.selectbox('Please select' , ['Python','Java','SQL'])
st.sidebar.radio('Please select' , ['Python','Java','SQL'])
