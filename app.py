import streamlit as st 
from PIL import Image

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.header("Real-Time & Images Object Detection ")
st.subheader("Automatically detects 20 objects from image")
st.caption("[Click here for App](/YOLO_for_image/)")

# Display example image comparison
col1, col2 = st.columns(2)
with col1:
    st.write('Normal image')
    st.image('./media/realtimenormal.png', width=400)
    
with col2:
    st.write('Detected image')
    st.image('./media/realtimedetect.png', width=400)

st.subheader("Real time Object detection")
st.caption("[Click here for App](/YOLO_webrtc/)")

st.subheader("Below are the objects our model can detect:")

# Helper to load and resize images
def load_image(path, size=(300, 300)):
    image = Image.open(path)
    return image.resize(size)

# List of labels and image paths
image_data = [
    ("DOG", "./media/dog.jpg"),
    ("PERSON", "./media/person.jpg"),
    ("AEROPLANE", "./media/aeroplane.jpg"),
    ("COW", "./media/cow.jpg"),
    ("SOFA", "./media/sofa.jpg"),
    ("POTTED PLANT", "./media/pottedplant.jpg"),
    ("CAR", "./media/car.jpg"),
    ("CAT", "./media/cat.jpg"),
    ("CHAIR", "./media/chair.jpg"),
    ("BICYCLE", "./media/bicycle.jpg"),
    ("MOTOR BIKE", "./media/bike.jpg"),
    ("DINING TABLE", "./media/dinningtable.jpg"),
    ("TV MONITOR", "./media/tv.jpg"),
    ("BUS", "./media/bus.jpg"),
    ("TRAIN", "./media/train.jpg"),
    ("BIRD", "./media/bird.jpg"),
    ("BOTTLE", "./media/bottle.jpg"),
    ("SHEEP", "./media/sheep.jpg"),
    ("BOAT", "./media/boat.jpg"),
    ("HORSE", "./media/horse.jpg"),
]

# Display 2 images per row
for i in range(0, len(image_data), 2):
    col1, col2 = st.columns(2)
    
    label1, path1 = image_data[i]
    with col1:
        st.write(label1)
        st.image(load_image(path1), width=300)

    if i + 1 < len(image_data):
        label2, path2 = image_data[i + 1]
        with col2:
            st.write(label2)
            st.image(load_image(path2), width=300)
