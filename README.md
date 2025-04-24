# 🍃 Leaf Identification Web App

This is a web-based **Leaf Identification** system built with Flask and Python. Users can upload an image of a leaf, and the app identifies the plant species, shows detailed information about the plant, and displays relevant location maps using Leaflet.js and OpenStreetMap.

## 🔍 Features

- Upload a leaf image to identify its species
- View detailed plant information based on identification
- Interactive map display of plant’s known locations (countries and states)
- Smooth UI with modal-based info sections
- Built with a lightweight Flask backend and JavaScript-powered frontend


## 📸 Screenshots

### 🔹 Home Page
![Home Screenshot](images/home.png)

### 🔹 Upload & Identification Result
![Result Screenshot](images/result.png)

### 🔹 Location Maps
![Map Screenshot](images/maps.png)

*(Place your images in a `images/` folder and replace the above paths with actual ones)*

---

## 🧑‍💻 Technologies Used

- **Frontend:** HTML, CSS, JavaScript, Leaflet.js
- **Backend:** Python (Flask)
- **Geocoding API:** OpenStreetMap (Nominatim)
- **Scripts:** `leaf_species.py`, `plant.py` for classification and plant details

---

## ⚙️ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/ManasiBhosale/Leaf_Identification.git
   cd Leaf_Identification
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🙌 Credits

- Mapping and location integration using OpenStreetMap  
- Frontend modals and UX design inspired by common UI patterns

---

## ⭐️ Show Your Support

If you found this project helpful, feel free to **star** the repo!

---
