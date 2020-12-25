import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from fastai.vision import *
import pandas as pd
from PIL import Image
import fastai;
from fastai.basic_train import load_learner
from fastai.vision import open_image
from flask_session.__init__ import Session

SESSION_TYPE = 'memcache'
sess = Session()

app = Flask(__name__)

UPLOAD_FOLDER = os.getcwd() + '/files/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'img' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['img']
        print(file)
        # if user does not select file, browser also
        # submit an empty part without filename
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            img = open_image(file)
            #pred, _, losses = learner.predict(img)
            pred_class, pred_idx, outputs = learner.predict(img)
            print("********",
                  learner.data.classes,
                  "********")
            pred_probs = outputs / sum(outputs)
            pred_probs = pred_probs.tolist()
            predictions = []
            info_df = pd.read_csv("plastic.csv")
            facts = pd.read_csv("Plastic_facts.csv")
            for image_class, output, prob in zip(learner.data.classes, outputs.tolist(), pred_probs):
                output = round(output, 1)
                prob = round(prob, 2)
                plastic_class = info_df[info_df['Name'] == image_class]['Abbreviation'].values[0]
                recycability = facts[facts['Abbreviation'] == plastic_class]['Recycability'].values[0]
                description = facts[facts['Abbreviation'] == plastic_class]['Description'].values[0]
                globalProduction = facts[facts['Abbreviation'] == plastic_class]['GlobalProduction'].values[0]
                hazard = facts[facts['Abbreviation'] == plastic_class]['EnvironmentHazard'].values[0]
                carbon_footprint = facts[facts['Abbreviation'] == plastic_class]['CarbonFootprint'].values[0]
                full_name = facts[facts['Abbreviation'] == plastic_class]['ChemicalName'].values[0]
                time_to_degrade = facts[facts['Abbreviation'] == plastic_class]['Timetodegrade'].values[0]
                predictions.append(
                    {"class": image_class.replace("_", " ").replace("pet", "").capitalize(),
                     "output": output, "p_type": plastic_class, "recycability": recycability,
                     "description": description, "globalProduction": globalProduction, "hazard": hazard,
                     "carbon_footprint": carbon_footprint, "time_to_degrade": time_to_degrade, "full_name": full_name}
                )
            predictions = sorted(predictions, key=lambda x: x["output"], reverse=True)
            predictions = predictions[0:1]

            return jsonify({"class": str(pred_class), "predictions": predictions})
    return '''
       <!doctype html>
       <title>Upload new File</title>
       <h1>Upload new File</h1>
       <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=Upload>
       </form>
       '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # return send_from_directory(app.config['UPLOAD_FOLDER'],
    #                            filename)
    return 'File updated!'

if __name__ == '__main__':
    defaults.device = torch.device('cuda')
    learner = load_learner('.')
    app.secret_key = 'verysupersecretketitis'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = False
    app.run()
