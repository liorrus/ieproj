from polls.models import *
import pandas as pd
from datetime import datetime
import random


def createPdForAnalysis(): 
    df = pd.DataFrame(columns=createCols())
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    total=[None]*12
    count = 0 
    for par in Part.objects.all():
        for i in range(0,12):
            year = currentYear
            month=currentMonth-i-1
            if month<=0:
                year=currentYear-1
                month=12-month
            total[i] = getNumberOfPartsUsedOnMonth(year,month,par)
        row=[par.pdes]
        for i in range(0,12):
            row.append(float(total[i])+1+random.uniform(0, 1))
        row.append(1) #append part price, do we need it?
        row.append(float(par.lt))
        row.append(2) #append part selling price, do we nned it?
        row.append(int(par.stock))
        row.append(10)
        df.loc[count]=row
        count+=1
    return df
            

def getallPartsDemand():  
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    count = 0 
    for par in Part.objects.all():
        for i in range(0,1):
            year = currentYear
            month=currentMonth-i-1
            if month<=0:
                year=currentYear-1
                month=12-month
            total = getNumberOfPartsUsedOnMonth(year,month,par)
            print(par, total)    


def getNumberOfPartsUsedOnMonth(year,month,par):
    total=0
    list=getListOfProuductWithPart(par)
    if(list==None):
        return total 
    for prod in list:
        total=total+(getNumberOfProductOrdersInMonth(year,month,prod)*getQuant(prod,par))
    return total

def getQuant(prod,par):
    return Pip.objects.filter(part=par,product=prod)[0].quant


def getNumberOfProductOrdersInMonth(year,month,prod):
    orderp1=Order.objects.filter(product1=prod,ifSupplied=True,orderPick__month=month,orderPick__year=year)
    orderp2=Order.objects.filter(product2=prod,ifSupplied=True,orderPick__month=month,orderPick__year=year)
    orderp3=Order.objects.filter(product3=prod,ifSupplied=True,orderPick__month=month,orderPick__year=year)
    return orderp1.count()+orderp2.count()+orderp3.count()


def getListOfProuductWithPart(par):
    
    count = 0
    qs=None
    pips=Pip.objects.filter(part=par)
    if(pips.count() > 0):
        qs=Product.objects.filter(pk=pips[0].product.pk)
    else:
        return qs
    for pip in pips:
        if(count == 0):
            count+=1
            continue
        qs=qs.union(Product.objects.filter(pk=pip.product.pk))

    return qs

def createCols():
    last12Months=createLast12Month()
    cols=['Sku']
    tempcols = ['cost','lead_time','sale_price','stock','backlog']
    for i in range (0,12):
        cols.append(last12Months[i])
    for i in range (0,5):
        cols.append(tempcols[i])
    return cols 

def createLast12Month():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    last12Months = [None]*12
    for i in range(0,12):
        year = currentYear
        month=currentMonth-i-1
        if(month <= 0):
            month = 12-month
            year = year - 1 
        last12Months[i] = str(month)+ "." + str(year)
    return last12Months


import matplotlib.pyplot as plt
import pandas as pd
from supplychainpy.model_inventory import analyse
from supplychainpy.model_demand import simple_exponential_smoothing_forecast
from supplychainpy.sample_data.config import ABS_FILE_PATH
from decimal import Decimal

def createSupplyChainAnalysis(pdesc):
    raw_df = createPdForAnalysis()
    orders_df = raw_df
    analyse_kv =dict(
        df=raw_df,
        start=1,
        interval_length=12,
        interval_type='months',
        z_value=Decimal(1.28),
        reorder_cost=Decimal(400),
        retail_price=Decimal(455),
        file_type='csv',
        currency='USD'
    )
    print(raw_df)
    
    analysis_df = analyse( **analyse_kv)
    
    analysis_rev = analysis_df[['sku', 'revenue']]
    
    row_ds = raw_df[raw_df['Sku']==pdesc].squeeze()
    ses = simple_exponential_smoothing_forecast(demand=list(row_ds[1:12]), alpha=0.5, forecast_length=6, initial_period=18)
    forecast_breakdown_df = pd.DataFrame(ses.get('forecast_breakdown', 'UNKNOWN'))
    regression = {'regression': [(ses.get('statistics')['slope']* i ) + ses.get('statistics')['intercept'] for i in range(1,12)]}
    print(regression)
    forecast_breakdown_df['regression'] = regression.get('regression')
    forecast_breakdown_df.plot(x='t', y=['one_step_forecast','demand', 'regression'])
    plt.show()
    
getallPartsDemand()

#createSupplyChainAnalysis("tomato")
