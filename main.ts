input.onButtonPressed(Button.A, function send_message() {
    radio.sendString("Hello World!")
    basic.showString("Send!")
})
radio.onReceivedString(function show_message(receivedString: string) {
    basic.showString(receivedString)
})
