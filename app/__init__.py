from flask import *

# ------------------------------ FLASK ---------------------------------
app = Flask(__name__)  

# ---------------------------CHAMADA DOS CONTROLLERS------------------------------
from app.controllers import consult


