from flask import Flask, jsonify
app = Flask(__name__)
myData = [{'Customer':'ABC' , 'Q1':200, 'Q2':230, 'Q3':300},
          {'Customer':'XYZ' , 'Q1':120, 'Q2':320, 'Q3':200}]
@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"
@app.route('/data', methods=['GET'])
def getMyData():
    return jsonify({'myData':myData})

@app.route('/quarter/<quarter>')
def getQuarterData(quarter):
    result = ' '
    if quarter in ['Q1','Q2','Q3']:
        for dataLine in myData:
            result = result + f'{dataLine["Customer"]}: {dataLine[quarter]}<br>'
    return result 
if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)