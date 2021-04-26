# flask-to-do
to-do app builded with flask and firestore

to run server:
flask run

to config environment:  
source venv/bin/activate  
export FLASK_APP=main,py  

remember to set up for debug mode  
export FLASK_ENV=development  

for gclud using:  
gcloud auth login  
gclooud config list   
gclooud projects list  
gcloud config set project flask-to-do-310603
export GOOGLE_CLOUD_PROJECT=flask-to-do-310603
