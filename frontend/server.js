const http = require('http');
const app = require('./app');

// app sera éxecuté dans le port 3000
app.set(process.env.PORT || 3000);

// je cree mon server et je lui passe mon application
const server = http.createServer(app)

// ma constance port 
const port = process.env.PORT || 3000;

// le server est éxecuté dans le port 3000
server.listen(port, () => 
    { console.log(`le server est lancé sur le port ${port}`);
})