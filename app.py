from flask import Flask, request
# flask for api, request for input, jsonify for output
import pickle
app=Flask(__name__)
model= pickle.load(open('model.pk1','rb'))

# home route
@app.route('/')
def home():
    return "API running!!"

# prediction route
@app.route('/predict',methods=['POST'])
def predict():
    data = request.json
    
    result = model.predict([[exp]])
    
    return jsonify({
        "salary": int(result[0])
    })

if __name__ == "__main__":
    app.run(debug=True)