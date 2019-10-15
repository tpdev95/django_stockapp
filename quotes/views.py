from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json
    # pk_e97f024cd4db4721b8efdf233635ee5a
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_e97f024cd4db4721b8efdf233635ee5a")
        output = []
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html', {'ticker':"Enter a ticker symbol Above..."})


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json
    symbol_list = []
    fullinfo = requests.get("https://cloud.iexapis.com/beta/ref-data/symbols?token=pk_e97f024cd4db4721b8efdf233635ee5a")
    info_request = json.loads(fullinfo.content)
    for i in info_request:
        symbol_list.append(i['symbol']+ " - " + i['name'])

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_e97f024cd4db4721b8efdf233635ee5a")
            try:
                api = json.loads(api_request.content)
                api['idpk']=ticker_item.pk
                output.append(api)
            except Exception as e:
                api = "Error"
        return render(request, 'add_stock.html', {'ticker':ticker, 'output':output,'symbol_list':symbol_list})

def delete(request, stock_id):
            item = Stock.objects.get(pk=stock_id)
            item.delete()
            messages.success(request, ("Stock Has Been Deleted!"))
            return redirect(add_stock)
