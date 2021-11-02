import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    ice_cream_sales=[]
    cold_drink_sales=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for i in csv_reader:
            ice_cream_sales.append(float(i["Marks In Percentage"]))
            cold_drink_sales.append(float(i["Days Present"]))
    return {"x":ice_cream_sales,"y":cold_drink_sales}
def FindCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("The Correlation value is: ",correlation[0,1])
def Setup():
    data_path="Project_106.csv"
    dataSource=getDataSource(data_path)
    FindCorrelation(dataSource)
Setup()
        