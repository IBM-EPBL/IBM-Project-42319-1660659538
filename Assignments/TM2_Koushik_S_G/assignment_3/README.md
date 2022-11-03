# flask-with-ibm-cloud-object-storage

Create a `.env` file and type down the important credentials for IBM Bucket.

It would look like this:

```python
COS_ENDPOINT="https://s3.jp-tok.cloud-object-storage.appdomain.cloud/"
COS_API_KEY_ID="5438b65746574-i46b436464CT_gnuveye54874-7"
COS_INSTANCE_CRN="crn:v1:bluemix:public:cloud-object-storage:global:a/7b487h46464w8765bv756nmh386535:c22fe22d-22c4-4cc1-a2db-b54b37f43::"
```
Working with IBM Cloud Storage 

Step 1 : install Python SDK for Cloud Object Storage

```
pip install ibm-cos-sdk
```

Read Document - https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-python 

Step 2 : Clone or download this flask repo

```
git clone git@github.com:kshyam/flask-with-ibm-cloud-object-storage.git
```

Download Zip - https://github.com/kshyam/flask-with-ibm-cloud-object-storage/archive/refs/heads/main.zip 

Stpe 3 : Run flask app in debug mode 

```
flask --debug run
```

OR 

```
 export FLASK_ENV=development
 flask run

```

Open the application

```
http://127.0.0.1:5000/


