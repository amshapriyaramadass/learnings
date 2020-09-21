
from flask import Flask, render_template, request, json, jsonify
# import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('currency.html')

@app.route('/ajax', methods=['POST'])
def getValue():
    # amount = 0.0
    amount = int(request.form['amount'])
    base_currency = request.form['base_currency']
    convert_currency = request.form['convert_currency']
    result = getcurrencydetails(amount,base_currency,convert_currency)
    # return 'Converted from %s to %s is %f <br/> <a href="/">Back Home</a>' % (base_currency, convert_currency,result)
    # return render_template('results.html', results='Converted from %s to %s is %f <br/> <a href="/">Back Home</a>' % (base_currency, convert_currency,result) )
    # return render_template('results.html', results=result)
    return  jsonify(results=result)

def getcurrencydetails(amount,base_currency,convert_currency):

    urlData = "https://v6.exchangerate-api.com/v6/4fec4d7e0120961576923e9c/latest/{0}".format(base_currency)
   # response = urllib.request.urlopen(urlData)
  #  data1 = response.read()
  #  print(data1)
  #  data = json.loads(response.content)
  #  print(data)

    response = requests.get(urlData)
    data = json.loads(response.content)

    converted_rate = data['conversion_rates']

    #print(converted_rate)
    #print(len(converted_rate))
  
    for i in range (1,len(converted_rate)):
        
        if convert_currency in converted_rate:
            converted_Amt = amount*converted_rate[convert_currency]
    return(converted_Amt) 

if __name__ == '__main__':
    app.run()