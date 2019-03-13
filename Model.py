import pyhdb
from flask import Flask,  render_template
from config import Hana
from pprint import pprint
import json

class Model():
    # connection = None

    def __init__(self):
        self.connection = pyhdb.connect(Hana.HOST, Hana.PORT, Hana.USER, Hana.PASS)
        self.cursor = self.connection.cursor()

    @property
    def get_regions(self):
        regions_data = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM SALES_TUTORIAL.REGION")
        result_set = cursor.fetchall()
        for result in result_set:
            regions_data.append({"regionId":result[0], "regionName":result[1], "subRegionName":result[2]})
        return regions_data

    @property
    def get_products(self):
        products_data = []
        self.cursor.execute("SELECT * FROM SALES_TUTORIAL.PRODUCT")
        result_set=self.cursor.fetchall()
        for result in result_set:
            products_data.append({"product_id":result[0], "product_name":result[1]})
        return products_data

    @property
    def get_sales_data(self):
        sales_data = []
        self.cursor.execute("SELECT * FROM SALES_TUTORIAL.SALES")
        result_set = self.cursor.fetchall()
        for result in result_set:
            sales_data.append({"regionId":result[0], "productId":result[1], "Sales_amount":result[2]})
        return sales_data


model=Model()
print(model.connection.isconnected())
pprint(model.get_regions)
pprint(model.get_products)
pprint(model.get_sales_data)
app = Flask("HanaToPython")

@app.route("/")
def home():
   return render_template('index.html')
@app.route("/api/getRegions")
def get_regions():
    return json.dumps(model.get_regions),200, {"Content-Type": "application/json"}
@app.route("/api/getProducts")
def get_product():
    return json.dumps(model.get_products),200, {"Content-Type": "application/json"}
@app.route("/api/getSalesData")
def get_salesdata():
    return json.dumps(model.get_sales_data),200, {"Content-Type": "application/json"}


if __name__ == "__main__":
   app.run (use_reloader=True, debug=True)
