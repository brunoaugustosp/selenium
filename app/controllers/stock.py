from app import *
from app.models.query import Stock



@app.route("/stocks/<string:region>", methods=['GET'])
@cache.cached(timeout=193)
def stocks(region):

    region = (region).title()

    result = Stock(region).web_crawler()

    return (result)