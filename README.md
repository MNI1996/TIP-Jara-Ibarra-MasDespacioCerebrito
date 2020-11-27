# TIP-Jara-Ibarra-MasDespacioCerebrito

  # Tecnologias
  
    Front: Vue
    
    Model: Python
    
    Back: Mongo/flask

# Creacion de administrador por defecto
    Por seguridad, configura las credenciales de tu base de datos. (Y tal vez no usar como password "password")
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

# Documentaciond de la version de Boostrap que usamos
https://getbootstrap.com/docs/4.5/layout/grid/#how-it-works
