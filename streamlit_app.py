import streamlit as st
from PIL import Image

st.title('Image Resizer App')

# 이미지 업로드
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 이미지 열기
    image = Image.open(uploaded_file)

    # 원본 이미지 표시
    st.image(image, caption='Original Image', use_column_width=True)

    # 크기 조정 비율 입력
    width_factor = st.slider("Select width resize factor", 1, 4, 2)
    height_factor = st.slider("Select height resize factor", 1, 4, 2)
    
    # 이미지 크기 조정
    new_size = (image.width * width_factor, image.height * height_factor)
    resized_image = image.resize(new_size)

    # 크기 조정된 이미지 표시
    st.image(resized_image, caption='Resized Image', use_column_width=True)

    # 이미지 저장
    st.download_button(label="Download resized image",
                       data=resized_image.tobytes(),
                       file_name="resized_image.jpg",
                       mime="image/jpeg")
