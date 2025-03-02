def data_event(socketio):
    
    @socketio.on('feeddata')
    def feedata():
        print("Received 'feeddata' event!")
        socketio.emit("forserver", {
            "data": "test send data"
        }, room=None)
