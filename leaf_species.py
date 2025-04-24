# leaf_species.py
import sys
import os
import numpy as np
from pathlib import Path
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
import warnings

# Disable oneDNN optimizations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Suppress TensorFlow warnings
warnings.filterwarnings('ignore', category=UserWarning, module='tensorflow')
warnings.filterwarnings('ignore', category=DeprecationWarning, module='tensorflow')

try:
    file = sys.argv[1]
    img_path = Path(f"./uploads/{file}")
    model_path = Path("./model/leaf_model.h5")
    
    if not img_path.exists():
        raise FileNotFoundError(f"Image file '{file}' not found in uploads folder.")
    
    # Load the model
    model = load_model(model_path)
    
    # Preprocess the image
    test_image = image.load_img(img_path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    
    # Predict using the model
    result = model.predict(test_image, verbose=0)
    max_index = np.argmax(result[0])
    

    plant_arr= ['Acer_Campestre','Acer_Ginnala','Acer_Negundo','Acer_Palmatum','Acer_Platanoides','Aesculus_Flava','Ailanthus_Altissima','Catalpa_Speciosa','Ficus_Carica','Ginkgo_Biloba']

    
    print(plant_arr[max_index] if max_index is not None else "Prediction error.")

except IndexError:
    print("Error: No file argument provided. Please provide an image file name as a command-line argument.")
except FileNotFoundError as e:
    print(f"Error: {e}")
except OSError as e:
    print(f"OS Error: {e}")
except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
