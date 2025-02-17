from flask import Flask 

#factory
def create_app(): 
    app = Flask(__name__)
    
    from . import pet
    app.register_blueprint(pet.bp)
    
    from . import fact
    app.register_blueprint(fact.bp)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax! Mike should make less typos'
    
    #return the app
    return app