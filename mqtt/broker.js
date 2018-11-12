var mosca = require('mosca');
var server = new mosca.Server(settings);

server.on('ready', function() {
console.log("ready");
});

server.on('published', function(packet, client) {
    if(client!==undefined&&client!==null){
	console.log("client", client.id);
    }
});
