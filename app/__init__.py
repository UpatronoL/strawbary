from flask import Flask
from flask.cli import with_appcontext
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'strawbary.sqlite'),
    )

    if test_config is None:
    
        app.config.from_pyfile('config.py', silent=True)
    else:
       
        app.config.from_mapping(test_config)

    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    from . import table
    app.register_blueprint(table.bp)

    from . import home
    app.register_blueprint(home.bp)

    from . import summary
    app.register_blueprint(summary.bp)

    from . import analysis
    app.register_blueprint(analysis.bp)

    
    try:
        os.makedirs(os.path.join(app.root_path, 'data'))
    except OSError:
        pass

   
    @app.route('/')
    def index():
        from flask import redirect, url_for
        return redirect(url_for('home.home'))

    return app