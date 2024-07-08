from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)

app.config['SECRET_KEY'] = 'cc36e909fbe851eca8de84699919c8b6e13d3b77'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)
migrate = Migrate(app,db)


from blogbook import routes