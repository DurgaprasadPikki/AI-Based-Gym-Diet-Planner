import streamlit as st
import os
import random
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model

# Load Model
model_path = 'FV.h5'
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Label Dictionary
labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
          7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
          14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
          19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
          26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
          32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}

# Fruits and Vegetables Lists
fruits = [f.lower() for f in ['Apple', 'Banana', 'Bell Pepper', 'Chilli Pepper', 'Grapes', 'Jalepeno', 'Kiwi', 
          'Lemon', 'Mango', 'Orange', 'Paprika', 'Pear', 'Pineapple', 'Pomegranate', 'Watermelon']]

vegetables = [v.lower() for v in ['Beetroot', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Corn', 'Cucumber', 
              'Eggplant', 'Ginger', 'Lettuce', 'Onion', 'Peas', 'Potato', 'Raddish', 'Soy Beans', 'Spinach', 
              'Sweetcorn', 'Sweetpotato', 'Tomato', 'Turnip']]

# Function to Fetch Random Calories
def fetch_calories(prediction):
    try:
        return f"{random.randint(30, 50)} kcal (per 100 grams)"
    except Exception as e:
        st.error("Unable to fetch calories info.")
        print(e)
        return None

# Function to Process Image
def processed_img(img_path):
    try:
        img = load_img(img_path, target_size=(224, 224))  # Corrected target_size
        img = img_to_array(img).astype('float32') / 255  # Convert dtype to float32
        img = np.expand_dims(img, axis=0)
        
        answer = model.predict(img)
        y_class = np.argmax(answer, axis=-1)[0]
        
        res = labels.get(y_class, "Unknown")
        return res.lower()  # Ensure lowercase for comparison
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# Main Function
def run():
    st.title("🍍 Fruits & Vegetables Classifier 🍅")

    img_file = st.file_uploader("Choose an Image", type=["jpg", "png", "jpeg"])
    
    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)

        # Ensure the directory exists
        upload_dir = './upload_images/'
        os.makedirs(upload_dir, exist_ok=True)
        
        save_image_path = os.path.join(upload_dir, img_file.name)
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # Predict when an image is uploaded
        result = processed_img(save_image_path)
        
        if result:
            category = "Vegetable" if result in vegetables else "Fruit"
            st.info(f'**Category: {category}**')
            st.success(f"**Predicted: {result.capitalize()}**")

            # Fetch calories
            cal = fetch_calories(result)
            if cal:
                st.warning(f'**Calories: {cal}**')

# Run the App
if __name__ == '__main__':
    run()