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

# Vue-Socket-io
https://github.com/MetinSeylan/Vue-Socket.io
