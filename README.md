# TIP-Jara-Ibarra-MasDespacioCerebrito

  # Tecnologies
  
    Front: Vue
    
    Model: Python
    
    Back: Mongo/flask

# Default admin creation
    For security, set up admin credentials to your database. (Maybe don’t make your password as “password”)
    use admin
    db.createUser(
      {
        user: "admin",
        pwd: "password",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
      }
    )
    db.adminCommand( { shutdown: 1 } )
    The last command will shut down our server. To launch the server with authentication enabled, run this from the terminal instead.
    mongod --auth
    
# Trello
https://trello.com/b/rCHBDBeE/mas-despacio-cerebrito

# Socket-io
https://socket.io/

# Flask-Socket-io documentation
https://flask-socketio.readthedocs.io/en/latest/

# Vue-Noty documentation
https://github.com/renoguyon/vuejs-noty

#Boostrap documentation version that we use
https://getbootstrap.com/docs/4.5/layout/grid/#how-it-works
