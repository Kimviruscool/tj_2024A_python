
from app import app
from service import *

@app.route("/getaptread", methods=['get'])
def getapt():
    result2 = readapt('부평아파트(전월세)_실거래가')
    return result2
