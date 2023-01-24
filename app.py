import flask
import paho.mqtt.client as mqtt
app = flask.Flask(__name__)

@app.route('/<motion>', methods=['GET'])
def index(motion):
    if motion == "motionStart":
        print("hello")   # publisher
        client = mqtt.Client()
        client.connect("localhost",1883,60)
        client.publish("homebridge/motion", "start");
        client.disconnect();
    elif motion == "motionEnd":
       print("goodbye")
       # do the same thing but end
       client = mqtt.Client()
       client.connect("localhost",1883,60)
       client.publish("homebridge/motion/reset", "end");
       client.disconnect();
#    with open('out.txt', 'a') as f:
#        f.write(motion)

    return f"{motion} stuff"

if __name__ == '__main__':
    app.run()
