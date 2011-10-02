from gplusblog import create_app, create_manager


app = create_app()
manager = create_manager(app)

def run_manager():
    manager.run()
