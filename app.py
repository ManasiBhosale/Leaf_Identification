from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import os
import subprocess
import shutil
import base64
from datetime import datetime
import random
import json


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure you have a secret key set

UPLOAD_FOLDER = 'uploads/'
COLLECT_FOLDER = 'static/images/collect/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'gif', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['COLLECT_FOLDER'] = COLLECT_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


COLLECTION_FILE = 'collection.json'


def load_collection():
    if not os.path.exists(COLLECTION_FILE):
        return []
    with open(COLLECTION_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_collection(collection):
    with open(COLLECTION_FILE, 'w') as f:
        json.dump(collection, f)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def index():
    trivia_facts = [
        "Did you know? Some plants can live for thousands of years!",
        "Did you know? The tallest tree in the world is a coast redwood!",
        "Did you know? Bamboo can grow up to 35 inches in a single day!",
        "Did you know? The world's largest flower is the Rafflesia arnoldii!",
        "Did you know? Bananas are berries, but strawberries are not!"
    ]
    random_trivia = random.choice(trivia_facts)
    images = os.listdir(COLLECT_FOLDER)
    return render_template('index.html', images=images, random_trivia=random_trivia)



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # Traditional file upload
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            img_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(img_filename)
            session['img'] = filename  # Store the uploaded image's filename in session
            return render_template('upload.html', filename=filename)
    return render_template('upload.html')



@app.route('/camera')
def camera():
    # Render the live capture page
    return render_template('camera.html')



@app.route('/upload_camera', methods=['POST'])
def upload_camera():
    # Receive base64 image data from the camera page and save it
    base64_image = request.form.get('base64image')
    if not base64_image:
        flash("No image captured.")
        return redirect(url_for('camera'))
    
    # The base64 string is typically prefixed with "data:image/jpeg;base64,"
    header, encoded = base64_image.split(',', 1)
    data = base64.b64decode(encoded)
    # Generate a unique filename based on timestamp
    filename = f"camera_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(filepath, "wb") as f:
        f.write(data)
    session['img'] = filename  # Save filename in session
    flash("Image captured and uploaded successfully!")
    return redirect(url_for('compute'))



@app.route('/display_image/<filename>')
def display_image(filename):
    # Ensure the filename is passed correctly and Flask can serve the file
    #print("filename :", filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/compute', methods=['POST', 'GET'])
def compute():
    img_file = session.get('img')
    if not img_file:
        return redirect(url_for('index'))

    # Call the classification scripts
    item = subprocess.run(['python', 'leaf_species.py', img_file], capture_output=True, text=True)
    item_name = item.stdout.strip()
    plant_info = subprocess.run(['python', 'plant.py', item_name], capture_output=True, text=True)
    plant_data = plant_info.stdout.strip()

    arr = plant_data.split("+")
    titles = ["Plant Name", "Botanical Name", "Other Names", "Medicinal Uses", "Locations"]
    if len(arr) != len(titles):
        raise ValueError(f"Unexpected data format. Expected {len(titles)} items, but got {len(arr)} items.")

    plant_details = {}
    for i, title in enumerate(titles):
        val = arr[i].strip('["\]').replace('"', '').replace("'", '')
        plant_details[title] = val

    # Combine and clean all locations into one list
    location_string = plant_details.get("Locations", "")
    raw_parts = location_string.split('-') if '-' in location_string else [location_string]
    location_list = []
    for part in raw_parts:
        location_list.extend([loc.strip() for loc in part.split(',') if loc.strip()])

    session['item'] = item_name
    session['plant_details'] = plant_details
    session['img_file'] = img_file

    return render_template('compute.html',
                           plant_details=plant_details,
                           img_file=img_file,
                           item=item_name,
                           locations=location_list)



@app.route('/add_to_collection', methods=['POST'])
def add_to_collection():
    # Retrieve image and plant details from session
    img_file = session.get('img')
    plant_details = session.get('plant_details')

    if img_file and plant_details:
        # Copy image from upload folder to collection folder
        img_file_path = os.path.join(app.config['UPLOAD_FOLDER'], img_file)
        collect_img_path = os.path.join(app.config['COLLECT_FOLDER'], img_file)
        shutil.copy(img_file_path, collect_img_path)
        
        # Create a collection record with current datetime
        new_record = {
            'image': img_file,
            'plant_details': plant_details,
            'date_added': datetime.now().isoformat()  # Store as ISO string
        }
        
        # Load existing collection from file, append the new record, and save
        collection = load_collection()
        collection.append(new_record)
        save_collection(collection)
        
        flash("Item added to collection!")
    else:
        flash("No image or details found to add to collection.")
    
    # Redirect back to compute view (or any other page as needed)
    # Pass locations as before if needed.
    locations = plant_details.get('Locations', '').split(', ') if plant_details.get('Locations') else []
    return render_template('compute.html', plant_details=plant_details, img_file=img_file, locations=locations)
    
    
@app.route('/collection_item/<int:item_id>')
def collection_item(item_id):
    collection = load_collection()
    if item_id < 0 or item_id >= len(collection):
        flash("Invalid collection item")
        return redirect(url_for('index'))
    item = collection[item_id]
    return render_template('collection_item.html', item=item)
  

  
@app.context_processor
def inject_collection():
    return dict(load_collection=load_collection)



# New route to mimic try.php functionality
@app.route('/try_route')
def try_route():
    category = request.args.get('category')
    if not category:
        flash("No category provided")
        return redirect(url_for('index'))
    
    # Run plant.py with the provided category (plant name)
    plant_output = subprocess.run(['python', 'plant.py', category], capture_output=True, text=True).stdout.strip()
    titles = ["Plant Name", "Botanical Name", "Other Names", "Medicinal Uses", "Locations"]
    arr = plant_output.split("+")
    if len(arr) != len(titles):
        flash("Error processing plant details")
        return redirect(url_for('index'))
    plant_details = {}
    for i, title in enumerate(titles):
        plant_details[title] = arr[i].strip('["\]').replace('"', '').replace("'", '')
    
    trivia_facts = [
        "Did you know? Some plants can live for thousands of years!",
        "Did you know? The tallest tree in the world is a coast redwood!",
        "Did you know? Bamboo can grow up to 35 inches in a single day!",
        "Did you know? The world's largest flower is the Rafflesia arnoldii!",
        "Did you know? Bananas are berries, but strawberries are not!"
    ]
    random_trivia = random.choice(trivia_facts)
    images = os.listdir(COLLECT_FOLDER)
    # Render the index template including a new section with plant details.
    return render_template('index.html',
                           plant_category=category,
                           plant_info=plant_details,
                           images=images,
                           random_trivia=random_trivia)


@app.route('/identify/<image>')
def identify(image):
    return render_template('identify.html', image_name=image)



@app.route('/help')
def help():
    return render_template('help.html')



if __name__ == '__main__':
    app.run(debug=True)
