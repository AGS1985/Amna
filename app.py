import streamlit as st
#from gtts import gTTS
#from io import BytesIO
from PIL import Image



def calculate_bmi(weight, height, age):
    bmi = weight / (height/100)**2
    if age < 20:
        # use a different range for children
        if bmi < 18:
            return "You are Underweight, please eat more to gain more weight"
        elif bmi <= 25:
            return "Normal weight, you are perfect well done"
        else:
            return "you are overweighted , please go to the gym to lose weight"
    else:
        # use a different range for adults
        if bmi < 18.5:
            return "You are Underweight !"
        elif bmi <= 24.9:
            return "Normal weight, you are perfect well done"
        else:
            return "You are overweighted !"
st.text('Amna Mohamed Shaat')

st.title("BMI Calculator")
st.subheader('Body mass index (BMI) is a measure of body fat based on height and weight that applies to adult men and women.')
img = Image.open('img2.png')
st.image(img,width=600)

#sound_file = BytesIO()
#tts = gTTS('Please enter your weight ,height and age details', lang='en')
#tts.write_to_fp(sound_file)
#st.audio(sound_file)
weight = st.number_input("Enter your weight in kilograms: ",value=0)
height = st.number_input("Enter your height in centimeters: ",value=0)
age = st.number_input("Enter your age: ",value=0)


if st.button("Calculate"):
    
    bmi = weight / (height/100)**2
    bmi_status = calculate_bmi(weight, height, age)
    img = Image.open('img.png')
    st.image(img,width=500,caption='Check your BMI Category')
    st.success("Your BMI is: {:.2f}".format(bmi))
    st.success("Based on your BMI: {}".format(bmi_status))
    if bmi > 18 and bmi <= 24.9:
        st.balloons()
    if bmi > 25:
        st.warning('Please go to the gym to lose weight', icon="⚠️")
    if bmi < 18:
        st.warning('Please eat more to gain more weight', icon="⚠️")







