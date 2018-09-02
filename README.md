# qrcontrol

## important commands
flask run 

flask db init 

flask db migrate -m "users table"

flask db upgrade

## Some background infos
http://flask-sqlalchemy.pocoo.org/2.3/


## Add a user from CLI using flask shell
>>> u = User(username='susan', email='susan@example.com')
>>> u.set_password('cat')
>>> db.session.add(u)
>>> db.session.commit()