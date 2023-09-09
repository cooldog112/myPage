import streamlit as st
from PIL import Image
st.set_page_config(
    page_title = '호돌HOME',
    page_icon = '🚲'
)
menu = st.sidebar.selectbox('MENU', ['자기소개','학교소개','동아리소개','???'])
if menu == '자기소개':
    st.subheader('자기소개🌈')
elif menu == '학교소개':
    st.subheader('학교소개🏫')
    col1, col2 = st.columns(2)
    with col1:
        st.write('HI')
    with col2:
        image = Image.open('school.jpg')
        #width가 사진의 폭
        st.image(image, width=200)
elif menu == '동아리소개':
    st.subheader('동아리소개🕹')
else:
    st.subheader('관심분야')