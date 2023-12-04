import socket
import tornado

import temperature_and_humidity
import leds
import buzzer
import distance_sensor
import motors
import auto_drive


class WSHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    # the function used to open a new WebSocket
    def open(self):
        print('Socket has been opened')

    # the function used to receive a message through an open WebSocket
    async def on_message(self, message):
        # check to see which message has been sent
        if message == 'distance':
            distance = str(distance_sensor.read_distance())
            # after we created the string with all necessary info, send back a response message
            await self.write_message(distance)

        if message == 'temp_hum':
            temperature, humidity = temperature_and_humidity.read_temperature_and_humidity()
            temperature = str(temperature)
            humidity = str(humidity)
            # create a string with both parameters read before
            info_string = humidity + '|' + temperature
            # after we created the string with all necessary info, send back a response message
            await self.write_message(info_string)

        if message == 'front':
            # moving forward
            print('front')
            motors.move_forward(0.5)

        if message == 'back':
            # moving backward
            print('back')
            motors.move_backward(0.5)

        if message == 'right':
            # turning left
            print('right')
            motors.turn_right(0.25)

        if message == 'left':
            # turning right
            print('left')
            motors.turn_left(0.25)

        if message == 'leds_on':
            # turn the leds on
            print('leds on')
            leds.leds_on()

        if message == 'leds_off':
            # turn the leds off
            print('leds off')
            leds.leds_off()

        if message == 'buzzer':
            # ring the buzzer for 3 seconds
            print('buzzer')
            buzzer.buzzer(3)

        if message == 'auto':
            # activate the auto drive mode
            print('auto drive')
            auto_drive.auto_drive()
            sleep(100)
            motors.turn_off()

    # the function used to close a WebSocket
    def on_close(self):
        print('Socket connection has been closed')


# creating an application object that will handle the routing table
application = tornado.web.Application([
    (r'/ws', WSHandler),
])

# in the main function we will open the server using Raspberry IP and port 8888
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()
