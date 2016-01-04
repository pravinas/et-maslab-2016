## pubsub.py
#
# Publisher-Subscriber framework for MASLAB 2016 Team 6.

class Publisher:

    def __init__(self):
        self.subscribers = []   # A list of callback functions subscribed to this publisher.
        self.most_recent = null # The most recent message sent to this publisher.

    ## Do something with a message when sent
    # 
    # @param callback_fn The function to be carried out when the message is recieved.
    def subscribe(self, callback_fn):
        self.subscribers.append(callback_fn)

    ## Send a message
    #
    # @param message The message to be sent
    def publish(self, message):
        most_recent = message
        notify(message)

    ## Get the most recent message sent.
    #
    # @return The most recent message
    def get_most_recent(self):
        return most_recent

    ## Run all callback functions on the message
    #
    # @param message The message to process.
    def notify(self, message):
        for (callback : subscribers):
            callback(message)