from app import app

@app.shell_context_processor
def make_shell_context():
    return {}
#    return {'db': db, 'User': User, 'Post': Post}
