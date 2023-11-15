def send_message():
    radio.send_string("Hello World!")
    basic.show_string("Send!")

def show_message(receivedString):
    basic.show_string(receivedString)

input.on_button_pressed(Button.A, send_message)
radio.on_received_string(show_message)