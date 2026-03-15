# 🍃 Leaf Identification Web App

A modern, interactive web app that lets users discover plant facts and identify leaves using a CNN-based model. Snap a live photo or upload an image, get a classification, explore plant details and maps and even build your own collection of favourite leaves!

---

## 🚀 Table of Contents

1. [Project Overview](#-project-overview)
2. [Features](#-features)  
3. [Demo](#-demo)  
4. [Screenshots](#-site-screenshots)  
5. [Getting Started](#-getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
6. [Usage](#-usage)  
7. [Dataset & Model Details](#-dataset--model-details)  
8. [Folder Structure](#-folder-structure)  
9. [Future Improvements](#-future-improvements)  
10. [Contributing](#-contributing)  
11. [Credits](#-credits)  

---

## 📝 Project Overview

When you land on the site, a **random plant or tree fact** pops up to spark your curiosity. Then you can:

- **Snap** a live photo of a leaf (via your camera)  
- **Upload** a saved image  

Behind the scenes, a CNN trained on 1,625 leaf images across **10 species** (with 99% train, 94% val, 95% test accuracies) classifies your leaf. You’ll see:

- **Botanical Name** & Other Names  
- **Medicinal Uses**  
- **Known Locations** (interactive maps powered by Leaflet.js + OpenStreetMap)  

Plus, you can **save favorites** in your personal Collection so you never have to re-upload the same leaf twice.  

---

## ✨ Features

- **Random Plant Fact** popup on page load  
- **Live camera capture** or **file upload** for leaf images  
- High-accuracy **CNN classification** (10 species)  
- Detailed **plant info** (botanical, uses, etc.)  
- Interactive **location maps** for each species  
- **Collection** feature to bookmark leaves + timestamp  
- Modern, responsive UI with smooth modal dialogs
  
---

## 🎬 Demo

Watch the app in action! The video below demonstrates how to:

- Open the leaf identification website  
- Capture or upload a leaf image  
- View the classification results  
- Explore plant details and maps  
- Save the leaf to your personal collection  

<p align="center">
  <img src="https://raw.githubusercontent.com/ManasiBhosale/Leaf_Identification/64693c7da6ebaf3348e28c5f9a57284e2d3da93e/Site%20Screenshots/Demo.gif" width="80%">
</p>

---

## 📸 Site Screenshots

Here are some screenshots showcasing different features of the leaf identification site:

**1. Random Facts Popup**
   <br>
   A popup displaying a random fact about plants, fauna, or trees when the site is loaded.
   
   ![Facts Popup](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Facts_Popup.png)
     

**2. Index Page**
   <br>
   The homepage showing the site interface with options for uploading or taking a photo, viewing collections, etc.
   
   ![Index Page](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Index_Page.png)  
   
   
**3. Camera Upload Screen**
   <br>
   The screen where users can take a live image of a leaf for identification. <br>
   (Below image was taken on my laptop camera. I didn’t have any leaves handy at the moment, and since I definitely wasn’t about to show my face, please enjoy my phone stepping in to say “hello” on my behalf.)
   
   ![Camera Upload](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Camera_Upload.png)  
   

**4. Upload Screen**
   <br>
   The screen where users can upload a saved image of a leaf for classification.
   
   ![Upload](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Upload.png)  
   

**5. Classification Screen**
    <br>
   After uploading or capturing an image, the system classifies the leaf and displays the result.
   
   ![Classification](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Classification.png)  
   

**6. Collection Screen**
    <br>
   Users can view and manage their saved leaf images and plant details in their collection.

   ![Collection](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Collection.png)  
  

**7. Collection with Plant Info**
    <br>
   A detailed view of a saved plant image, showing the plant's botanical name, other names, medicinal uses, and more.

   ![Collection with Plant Info](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Collection_Plant_Info.png)  
   

**8. Help Screen**
    <br>
   The help section where users can get assistance and more information about using the site.

   ![Help](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/Help.png)  
   

**9. Information Screen**
    <br>
    A welcoming page that explains how to use the site to identify plants and save your favorites.

   ![INFO](https://github.com/ManasiBhosale/Leaf_Identification/blob/c701b100bc234646e86d04968bf4e66992c188d1/Site%20Screenshots/INFO.png)  
  
---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+  
- `virtualenv` or `venv`  
- Folders:  
  - `uploads/` (for incoming leaf images)  
  - `collect/` (to save favorites)

### Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/ManasiBhosale/Leaf_Identification.git
   cd Leaf_Identification
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Create needed folders**  
   ```bash
   # Create the necessary folders
   mkdir uploads               # Folder for uploaded images
   mkdir static/images/collect  # Folder for favorite images & data

   ```

5. **Run the app**  
   ```bash
   python app.py
   ```
   Then open: `http://127.0.0.1:5000/`

---

## 🎯 Usage

1. Load the site, enjoy a random plant fact.  
2. Click “Capture Live” or “Upload Image” to select your leaf.  
3. Wait a second, your leaf is now classified!  
4. Explore botanical details, medicinal uses, and location maps.  
5. Hit “Add to Collection” to bookmark for later.

---

## 📊 Dataset & Model Details

- **Classes (10 species):**  
  `Acer campestre`, `Acer ginnala`, `Acer negundo`, `Acer palmatum`,  
  `Acer platanoides`, `Aesculus flava`, `Ailanthus altissima`,  
  `Catalpa speciosa`, `Ficus carica`, `Ginkgo biloba`


| Set Type      | Data Split (%) | Accuracy Achieved (%) |
|---------------|----------------|------------------------|
| Training Set  | 80%            | 99%                   |
| Validation Set| 10% (of total) | 94%                   |
| Test Set      | 10% (of total) | 95%                   |

- Total images: **1,625** across **10 plant species**
- CNN-based image classification with high performance across all sets.

---

## 📂 Folder Structure

```
Leaf_Identification/
├── model/            # Directory for the ML model
├── Site Screenshots/ # Folder containing site screenshots
├── static/
│   ├── css/          # CSS files for styling
│   ├── images/       # Contains images used in the app
│   │   └── collect/  # Folder for images in the collection
│   ├── js/           # JavaScript files for interactivity
│   └── webfonts/     # Web font files
├── templates/        # HTML templates for different pages
├── Test/             # Folder for test images, categorized by plant species
│   ├── acer_campestre/
│   ├── acer_ginnala/
│   ├── acer_negundo/
│   ├── acer_palmatum/
│   ├── acer_platanoides/
│   ├── aesculus_flava/
│   ├── ailanthus_altissima/
│   ├── catalpa_speciosa/
│   ├── ficus_carica/
│   └── ginkgo_biloba/
└── uploads/          # Directory for uploaded images
```

---

## 🔮 Future Improvements

- Host the app on a public server  
- Expand to **more than 10 species**  
- Try other ML models (ResNet, MobileNet, etc.)  
- User accounts & authentication  
- Offline-capable PWA or mobile app version  
- Auto-cleanup of old uploads/collection items  

---

## 🤝 Contributing

Feel free to open issues or submit PRs! If you want to help add more species or improve the UI/UX, you’re very welcome.  

---

## 🙌 Credits

This project wouldn't be possible without the amazing open-source tools, libraries, and data resources. Big thanks to:

- **Flask** – for making Python web development quick and simple  
- **TensorFlow / Keras** – for powering the CNN model  
- **Pandas & NumPy** – for efficient data manipulation  
- **Pillow (PIL)** – for image handling  
- **Leaflet.js + OpenStreetMap** – for displaying plant locations interactively  
- **TQDM, scikit-learn** – for boosting training and preprocessing   
- **[Leafsnap Dataset](https://leafsnap.com/dataset/)** – A publicly available dataset used for training leaf recognition models.

---
