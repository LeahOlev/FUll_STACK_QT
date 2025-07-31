from flask import Flask, jsonify
from controllers.AttractionType_controller import AttractionType_blueprint
from controllers.Region_controller import Region_blueprint
from controllers.Visitor_controller import Visitor_blueprint
from controllers.VisitorPerAttraction_controller import VisitorPerAttraction_blueprint
from controllers.User_controller import User_blueprint
from controllers.TravelPerUser_controller import TravelPerUser_blueprint
from controllers.SavedTravels_controller import SavedTravels_blueprint
from controllers.Attractions_controller import Attractions_blueprint
from error_handlers.error_handlers import register_error_handlers
from config import Base, engine
import models.Attractions
import models.AttractionType
import models.Region
import models.SavedTravels
import models.TravelPerUser
import models.Users
import models.Visitors
import models.VisitorPerAttraction

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

app.register_blueprint(AttractionType_blueprint, url_prefix='/api/AttractionType')#
app.register_blueprint(Region_blueprint, url_prefix='/api/Region')#
app.register_blueprint(Visitor_blueprint, url_prefix='/api/Visitors')#v
app.register_blueprint(VisitorPerAttraction_blueprint, url_prefix='/api/VisitorPerAttraction')#[]
app.register_blueprint(User_blueprint, url_prefix='/api/Users')#
app.register_blueprint(TravelPerUser_blueprint, url_prefix='/api/TravelPerUser')#
app.register_blueprint(SavedTravels_blueprint, url_prefix='/api/SavedTravels')#[]
app.register_blueprint(Attractions_blueprint, url_prefix='/api/Attractions')#v
register_error_handlers(app)


@app.route('/')
def home():
    return "API Running"


@app.route('/whoami')
def whoami():
    with engine.connect() as conn:
        user = conn.execute("SELECT SYSTEM_USER").fetchone()
        return {'current_user': user[0]}


app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
