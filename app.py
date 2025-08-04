import streamlit as st
import os

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.header("Real-Time & Images Object Detection")

st.subheader("Automatically detects 20 objects from image")
st.caption("[Click here for App](/YOLO_for_image/)")

col1, col2 = st.columns(2)
with col1:
    st.write('Normal image')
    st.image('./media/realtimenormal.png')
    
with col2:
    st.write('Detected image')
    st.image('./media/realtimedetect.png')

st.subheader("Real-time Object detection")
st.caption("[Click here for App](/YOLO_webrtc/)")

st.subheader("Below are the objects our model will detect")

# First row
col1, col2, col3 = st.columns(3)
with col1:
    st.write('DOG')
    st.image('./media/dog.jpg', width=300)
with col2:
    st.write('PERSON')
    st.image('./media/Person.jpg', width=300)
with col3:
    st.write('AEROPLANE')
    st.image('./media/aeroplane.jpg', width=300)

# Second row
col1, col2, col3 = st.columns(3)
with col1:
    st.write('COW')
    st.image('./media/cow.jpg', width=300)
with col2:
    st.write('SOFA')
    st.image('./media/Sofa.jpg', width=300)
with col3:
    st.write('POTTED PLANT')
    st.image('./media/pottedplant.jpg', width=300)

# Third row
col1, col2, col3 = st.columns(3)
with col1:
    st.write('CAR')
    st.image('./media/car.jpg', width=300)
with col2:
    st.write('CAT')
    st.image('./media/cat.jpg', width=300)
with col3:
    st.write('CHAIR')
    st.image('./media/chair.jpg', width=300)

# Fourth row
col1, col2, col3 = st.columns(3)
with col1:
    st.write('BICYCLE')
    st.image('./media/bicycle.jpg', width=300)
with col2:
    st.write('MOTORBIKE')
    st.image('./media/motorbike.jpeg', width=300)
with col3:
    st.write('DINING TABLE')
    st.image('./media/dinningtable.jpg', width=300)

# Fifth row
col1, col2 = st.columns(2)
with col1:
    st.write('TV MONITOR')
    st.image('./media/tv.jpg', width=400)
with col2:
    st.write('BUS')
    st.image('./media/bus.jpg', width=400)

# Sixth row
col1, col2 = st.columns(2)
with col1:
    st.write('TRAIN')
    st.image('./media/train.jpg', width=400)
with col2:
    st.write('BIRD')
    st.image('./media/bird.jpg', width=400)

# Seventh row
col1, col2, col3 = st.columns(3)
with col1:
    st.write('BOTTLE')
    st.image('./media/Bottle.jpg', width=300)
with col2:
    st.write('SHEEP')
    st.image('./media/sheep.jpg', width=300)
with col3:
    st.write('BOAT')
    st.image('./media/boat.jpg', width=300)

# Last row
col1, col2 = st.columns(2)
with col1:
    st.write('HORSE')
    st.image('./media/horse.jpg', width=300)
