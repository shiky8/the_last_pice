from flask import Flask, render_template,request
from model.the_last_pice import LastPice

app = Flask(__name__)
app._static_folder = 'static'
def Convert(cipher):
        cipher = cipher.replace("[",'').replace("]",'').replace("'",'').replace(",",'')
        li = list(cipher.split()) 
        return li 
  
@app.route('/')
def index():
    return render_template('index.html',ehidden="hidden",dhidden="hidden")

@app.route('/encode',methods=['POST'])
def encode():
    plain = str(request.form.get("plain_text"))
    print(plain)
    key,cipher = LastPice.encode(plain)
    key = str(key).replace("b'",'').replace("'",'')
    return render_template('index.html',key=key,cipher=cipher,ehidden="hidde",dhidden="hidden")

@app.route('/decode',methods=['POST'])
def decode():
    cipher = str(request.form.get("ciphertext"))
    key = str(request.form.get("key"))
    print(key,cipher)
    cipher = Convert(cipher)
    print(cipher)
    plain_text = LastPice.decode(key,cipher)
    return render_template('index.html',plain_text=plain_text,ehidden="hidden",dhidden="hidde")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 