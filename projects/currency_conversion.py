import json
import requests


def getcurrencydetails(amt,bc,cc):

    urlData = "https://v6.exchangerate-api.com/v6/4fec4d7e0120961576923e9c/latest/{0}".format(bc)
   # response = urllib.request.urlopen(urlData)
  #  data1 = response.read()
  #  print(data1)
  #  data = json.loads(response.content)
  #  print(data)

    response = requests.get(urlData)
    data = json.loads(response.content)

    converted_rate = data['conversion_rates']

    print(converted_rate)
    print(len(converted_rate))
  
    for i in range (1,len(converted_rate)):
        
        if cc in converted_rate:
            converted_Amt = amt*converted_rate[cc]
    print(converted_Amt)    

    

def main():
    # get input amount to be converted, base currency, convert_currency
    amt,bc,cc = int(input()),str(input()),str(input())

    result = getcurrencydetails(amt,bc,cc)

if __name__ == "__main__":
    main()