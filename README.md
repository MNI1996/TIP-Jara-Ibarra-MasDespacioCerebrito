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

# Documentacion de Flask-Socket-io 
https://flask-socketio.readthedocs.io/en/latest/

# Documentacion de Vue-Noty 
https://github.com/renoguyon/vuejs-noty

# Documentacion de la version de Boostrap que usamos
https://getbootstrap.com/docs/4.5/layout/grid/#how-it-works

# Vue Test Utils (para carga de componentes en los test)
https://vue-test-utils.vuejs.org/

# Mocha pack ( para correr test Mocha y webpack)
https://github.com/sysgears/mochapack

# Mocha dependency de mocha pack
https://mochajs.org/

# Chai (necesario para aserciones en pruebas de front)
https://www.chaijs.com/guide/styles/

# JS DOM GLOBAL (para correr Mocha)
https://github.com/rstacruz/jsdom-global

# Sinon y Sinon-chai
https://www.chaijs.com/plugins/sinon-chai/

# Vue-Cookies 
https://github.com/cmp-cc/vue-cookies#readme
