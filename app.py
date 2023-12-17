import os
import PIL.Image
import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown
from PIL import Image
import io 

custom_css = """
    <style>
            textarea {
            resize: vertical;
            }
    </style>
"""

def chefGemini():
    os.environ['GOOGLE_API_KEY'] = "AIzaSyBjWUT9snDSAy0DwQNPpEkOCjkejwt0J4Q"
    genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
    # model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_content("List 5 planets each with an interesting fact")
    # print(response.text)

    image = PIL.Image.open('uploaded_image.jpg')
    vision_model = genai.GenerativeModel('gemini-pro-vision')
    foodName = vision_model.generate_content(["Give Only The Name Of this Food",image])
    recipeOfTheFood = vision_model.generate_content(["Give The Recipe Of this Food",image])


    #print(foodName.text)
    #print(recipeOfTheFood.text)
    foodRecipeWithName= []
    foodRecipeWithName.append(foodName.text)
    foodRecipeWithName.append(recipeOfTheFood.text)
    print(foodRecipeWithName)
    return foodRecipeWithName




st.set_page_config(page_title="Chef Gimini",
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('Chef Gemini 👨‍🍳 - Recipe Generation Bot')

uploaded_file = st.file_uploader("Upload Food Pic", type=["jpg", "jpeg"])
col4, col5, col6 = st.columns([2, 1, 1])
col4.write("")
submit = col5.button("Generate Recipe")
col6.write("")
if submit :
    if uploaded_file is not None:
        st.text("Please Wait,Recipe Will Be Displayed Soon ...")
        image = Image.open(uploaded_file)
        image = image.convert("RGB")
        with io.BytesIO() as output:
            image.save(output, format="JPEG")
            with open("uploaded_image.jpg", "wb") as f:
                f.write(output.getvalue())
        
        foodRecipeWithFood = chefGemini()
        st.markdown(custom_css, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])

        col1.write("")

        col2.image("uploaded_image.jpg", width=300)

        col3.write("")

        st.text_input('Food Name : ',foodRecipeWithFood[0])

        st.text_area('Food Recipe : ',foodRecipeWithFood[1]) 


#if __name__ == "__main__" :
#  chefGemini()