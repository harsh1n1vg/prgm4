from flask import Flask
import os
app=Flask(__name__)
ENV=os.getenv("ENV","NOT FOUND")
PASS=os.getenv("PASS","NOT FOUND")

@app.route('/')
def hello():
    return f"hello {ENV} , {PASS}"
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)