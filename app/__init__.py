from flask import *
from flask_caching import Cache




config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  
    "CACHE_DEFAULT_TIMEOUT": 300
}

# -------------------------------- FLASK -----------------------------------
app = Flask(__name__)
# ----------------------------- FLASK-CACHE --------------------------------
app.config.from_mapping(config)
cache = Cache(app)

# -------------------------CHAMADA DOS CONTROLLERS---------------------------
from app.controllers import stock



