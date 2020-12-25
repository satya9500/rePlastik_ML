# RePlastik
This project classifies types of plastics ad gives insights about the same to the users.
Also suggests recycling/reusing process after analyzing the plastic.
Generates Visual reports using plotly.

[Backend of this project](https://github.com/satya9500/rePlastik_backend)

[Frontend for this project](https://github.com/satya9500/rePlastik_frontend)

## Tech Stack
1. Frontend - Angular 
2. UI Component Library - [Nebular](https://akveo.github.io/nebular/docs/getting-started/what-is-nebular#what-is-nebular)
3. Graphs - PlotlyJS
4. Backend - NodeJS
5. DB - MongoDB
6. ML Models and APIs - Flask and fastai

## Screenshots
<hr>

### Registration Page
![Registration Page](Screenshots/register.png) 

### Login Page
![Login Page](Screenshots/login.png) 

### Home Page
![Home Page](Screenshots/home.png) 

### Classification Steps

**First**
![First Page](Screenshots/recycle1.png) 

**Second**
![Second Page](Screenshots/recycle2.png)

**Third**
 ![Third Page](Screenshots/recycle3.png)
 ![Third Page](Screenshots/recycle3_2.png)

### Classification History
![Classification History](Screenshots/history.png)

### Visual Report
![Visual Report](Screenshots/graph.png)

### Search Page
![Search Page](Screenshots/search.png)
<hr>

#### How to run 
**download final model from [here](https://drive.google.com/file/d/1OeMO43eeuBhalsvsfVe8f7mMbL1TTD-m/view?usp=sharing) and paste in the same directory, you should also have flask and flask sessions installed in your system.**
1. `git clone https://github.com/satya9500/rePlastik_ML.git`
2. `Download final model and paste in same directory`
3. `cd rePlastik_ML`
4. `pip3 install fastai==1.0.60`
5. `python3 app.py`
6. `Now run nodejs server and goto localhost:3000 to see the website up and running`

