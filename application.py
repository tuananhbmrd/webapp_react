from app import create_app

application = create_app()

if __name__ == '__main__':
    application.run(host='localhost', port=5000, debug=True)