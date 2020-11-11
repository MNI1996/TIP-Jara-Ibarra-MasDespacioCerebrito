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

# Boostrap documentation version that we use
https://getbootstrap.com/docs/4.5/layout/grid/#how-it-works

# Vue Test Utils (to load vue components to test)
https://vue-test-utils.vuejs.org/

# Mocha pack ( to run front end tests with mocha and webpack)
https://github.com/sysgears/mochapack

# Mocha dependency from mocha pack
https://mochajs.org/

# Chai ( we need this to assert in specs in frontend tests)
https://www.chaijs.com/guide/styles/

# JS DOM GLOBAL (we need this to run mocha)
https://github.com/rstacruz/jsdom-global
