import plotly.graph_objects as go
def pingUrl(url):
    import requests
    response = requests.get(url)
    return (response.status_code)
    
def scrapePrice(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text.encode('utf-8'),'html.parser')
    table=soup.select('div[class="jumbotron__card-detail d-flex align-items-center"]')[0].select('li')[1]
    extractedText=table.text.replace(" ","").replace("\n","")
    if extractedText[-3:].isdigit()==False and "-" in extractedText:
        minPrice,maxPrice=extractedText[:-3].split("-")
        currency=extractedText[-3:]
    elif extractedText[-3:].isdigit()==False and "-" not in extractedText:
        minPrice=extractedText[:-3]
        maxPrice="NA"
        currency=extractedText[-3:]
    elif extractedText[-3:].isdigit()==True and "-" in extractedText:
        minPrice,maxPrice=extractedText.split("-")
        currency="NA"
    else:
        minPrice=extractedText
        maxPrice="NA"
        currency="NA"
    return ([minPrice, maxPrice, currency])



def display(inputDf):
    headerColor = 'grey'
    rowEvenColor = 'lightblue'
    rowOddColor = 'white'
    columnsToShow=[inputDf[i] for i in inputDf]
    fig = go.Figure(data=[go.Table(
        header=dict(
        values=list(inputDf.columns),
        line_color='darkslategray',
        fill_color=headerColor,
        align=['left','center'],
        font=dict(color='white', size=12)
        ),
        cells=dict(
        values=columnsToShow,
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color = [[rowOddColor,rowEvenColor]*450],
        align = ['left', 'center'],
        font = dict(color = 'darkslategray', size = 11)
        ))
    ])
    fig.show()

def scrapeOneCurrency(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text.encode('utf-8'),'html.parser')
    table=soup.select('span[id="currency-first-display"]')[0].text.split("=")[1][:-3]
    return 1/float(table.replace(",","."))
  
def scrapeAllCurrencies(update=False):
    import json
    if(update==True):
        usd=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_us-dollar")
        gbp=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_britische-pfund")
        hkd=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_hong-kong-dollar")
        eur=1
        sgd=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_singapur-dollar")
        dkk=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_daenische-krone")
        thb=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_thai-baht")
        twd=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_taiwanesischer-dollar")
        sek=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_schwedische-krone")
        krw=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_suedkoreanischer-won")
        mop=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_macau-pataca")
        brl=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_brasilianischer-real")
        nok=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_norweg-krone")
        huf=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_ungarischer-forint")
        hrk=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_kuna")
        czk=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_tschechische-krone")
        pln=scrapeOneCurrency("https://www.finanzen.net/waehrungsrechner/euro_polnischer-zloty")
        currencies={"USD":usd,"GBP":gbp,"HKD":hkd,"EUR":eur,"SGD":sgd,"DKK":dkk,"THB":thb,"TWD":twd,"SEK":sek,"KRW":krw,"MOP":mop,"BRL":brl,"NOK":nok,"HUF":huf,"HRK":hrk,"CZK":czk,"PLN":pln}
        json = json.dumps(currencies)
        f = open("currencies.json","w")
        f.write(json)
        f.close()
        return currencies
    else:
        with open('currencies.json') as json_file:
            currencies = json.load(json_file)
        return currencies    

def giveFxrate(c):
    currencies=scrapeAllCurrencies(False)
    return(currencies[c])



