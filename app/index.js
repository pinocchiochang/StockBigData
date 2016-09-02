// import http dependenccy
var http = require('http')
var redis = require('redis')
var express = require('express')
var socketio = require('socket.io')

// sys.argv
var argv = require('minimist')(process.argv.slice(2))
var redis_port = argv['redis_port']
var redis_host = argv['redis_host']
var subscribe_channel = argv['subscribe_channel']

// initialize express application
var app = express();
var server = http.createServer(app);
var io = socketio(server);

// create redis client
var redisClient = redis.createClient(redis_port, redis_host)
console.log('Subscribe to redis channel', subscribe_channel)
redisClient.subscribe(subscribe_channel)

// when 'message' happens, do something
redisClient.on('message', function(channel, message){
	console.log('message received %s', message)
	io.sockets.emit('data', message)
});

// setup express webapp routing
app.use(express.static(__dirname + '/public'));
// app.use('/socket.io', express.static(__dirname + '/node_modules/socket.io/lib'))
app.use('/jquery', express.static(__dirname + '/node_modules/jquery/dist'))
app.use('/smoothie', express.static(__dirname + '/node_modules/smoothie'))

server.listen(3000);

console.log('Server started at port 3000')
