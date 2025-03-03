from flask import request

def data_event(socketio):
    
    # data crowd realtimenya bubub
    @socketio.on("crowd-realtime")
    def realtime(data):
        sender_id = request.sid
        try:
            print("recived data", data, type(data))
            # print("sid recieved", sender_id)
            
            socketio.emit("crowd-realtime", {
                "data": data
            }, room=None)
            
            socketio.emit("predictive-realtime", {
                "data": data
            }, room=None)
            
        except Exception as e:
            socketio.emit("crowd-realtime", {
                "data": str(e)
            }, room = sid)
            
            socketio.emit("predictive-realtime", {
                "data": str(e)
            }, room = sid)
            
            print(str(e))
    
    # data reports bubub
    @socketio.on("data-reports")
    def datareport(data):
        try:
            socketio.emit("data-reports", {
                "data": data
            })
        except Exception as e:
            socketio.emit("data-reports", {
                "data": str(e)
            }, room=None)
            print(str(e))
    
    # data emergency bubub
    @socketio.on("emergency-data")
    def datareport(data):
        try:
            socketio.emit("emergency-data", {
                "data": data
            }, room=None)
        except Exception as e:
            socketio.emit("data-reports", {
                "data": str(e)
            })
            print(str(e))
    
    @socketio.on("test-usingid/<id>")
    def testusingid(id):
        print(id)