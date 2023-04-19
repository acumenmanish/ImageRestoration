
from PIL import Image
import numpy as np 
import streamlit as st 
import gradio as gr
import requests

st.title('Welcome to Cohort 11 Image Restoration Project!')


# Function to Read and Manupilate Images
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

# Uploading the File to the Page
uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])

# Checking the Format of the page
if uploadFile is not None:
    # Perform your Manupilations (In my Case applying Filters)
    img = load_image(uploadFile)
    st.image(img)
    st.write("Image Uploaded Successfully")
else:
    st.write("Make sure you image is in JPG/PNG Format.")
    
    
if st.button('Restore'):
    if uploadFile is not None:
     # Perform your Manupilations (In my Case applying Filters)
     img = load_image(uploadFile)
     st.image(img)
     st.write("Image Restored Successfully")
else:
    st.write('Goodbye')

def image_restored(file_obj):
    url = 'https://en.wiktionary.org/wiki/dog#/media/File:YellowLabradorLooking.jpg'
    r = requests.get(url, allow_redirects=True)
    open('dog.jpg', 'wb').write(r.content)
    return 'dog.jpg'

examples = [
    [os.path.abspath("short-pdf.pdf")],
    [os.path.abspath("long-pdf.pdf")]
]

iface = gr.Interface(fn = pdf_to_text, 
                     inputs = 'image', 
                     outputs = 'image', 
                     title = 'Blurred image to restored image Application',
                     description = 'Simple application in python to try the Gradio package components',
                     article = 
                        '''<div>
                            <p> Please wait while restoration of your image is happening.</p>
                        </div>'''
                    )
iface.launch()
