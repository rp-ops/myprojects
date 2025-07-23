import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="My Image Processor", layout="wide")

# Title
st.title("My Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data
def load_image():
    path = r"C:\Users\RAJASHREE\Desktop\0.image_analysis\my_image.jpg"
    return Image.open(path).convert("RGB")

# Load and display image
myImage = load_image()
st.image(myImage, caption="My Image", use_container_width=False)

# Convert to NumPy array
raju_np = np.array(myImage)
R, G, B = raju_np[:, :, 0], raju_np[:, :, 1], raju_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(raju_np)
green_img = np.zeros_like(raju_np)
blue_img = np.zeros_like(raju_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

myimg_gray = myImage.convert("L")
myImage_np = np.array(myimg_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(3, 3))
im = ax.imshow(myImage_np, cmap=colormap)
plt.axis("off")

# DO NOT USE: plt.show()
# USE THIS INSTEAD:
st.pyplot(fig)