from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

person = 0
dog = 0

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json(silent=True)

    global person
    if 'person' in data.keys():
        person = int(data['person'])
    else:
        person = person
    global dog
    if 'dog' in data.keys():
        dog = int(data['dog'])
    else:
        dog = dog

    return jsonify({'person': person, 'dog': dog})

@app.route('/check', methods=['GET'])
def check():
    return jsonify({'person': person, 'dog': dog})

@app.route('/')
def index():
    return render_template('index.html', person=person, dog=dog)

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=8000)
