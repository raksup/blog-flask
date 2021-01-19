from app import create_app  #create_app is the name of the function created in __init__.py

app = create_app()
                            
if __name__ == '__main__':
    app.run(debug=True)