var express = require('express');
var http = require('http');
var io = require('socket.io');
var SerialPort = require("serialport");
var abc;
var serialport = new SerialPort("COM5",{
    baudRate:9600
    }); 
    
   serialport.on('open', function(){
  console.log('Serial Port Opend');
  serialport.on('data', function(data1){ 
  
      var abc =data1;
       if (abc==51)
       {
       console.log(abc);}
  });

  });    

var app = express();
app.use(express.static('./public'));
//Specifying the public folder of the server to make the html accesible using the static middleware
 
var server =http.createServer(app).listen(8124);
//Server listens on the port 8124
io = io.listen(server); 
/*initializing the websockets communication , server instance has to be sent as the argument */
 
io.sockets.on("connection",function(socket){
    /*Associating the callback function to be executed when client visits the page and 
      websocket connection is made */
      
      var message_to_client = {
        data:"Connection with the server established"
      }
      socket.send(JSON.stringify(message_to_client)); 
      /*sending data to the client , this triggers a message event at the client side */
    console.log('Socket.io Connection with the client established');
    
    socket.on("message",function(data){
        /*This event is triggered at the server side when client sends the data using socket.send() method */
        data = JSON.parse(data);
        serialport.write(data);
        console.log(data);
        
        /*Printing the data */
        var ack_to_client = {
            data:"Recieved"
        }
        
      socket.send(JSON.stringify(ack_to_client));
        /*Sending the Acknowledgement back to the client , this will trigger "message" event on the clients side*/
    });
});


  

      
       
