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
    #here you can plug you AI model. This will enable the code to run
    # the output will be path to your image that will be hosted on server
    #once done pass that path in below url param
    # i have used dummy path from a server to show the output
    url = 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/06/smallest-dog-breeds-toy-poodle.jpg?fit=728%2C524'
    img = open('dog.jpg', 'wb')
    img.write(requests.get(url).content)
    img.close()
    return 'dog.jpg'

#examples = [
#    [os.path.abspath("short-pdf.pdf")],
#    [os.path.abspath("long-pdf.pdf")]
#]

iface = gr.Interface(fn = image_restored, 
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
