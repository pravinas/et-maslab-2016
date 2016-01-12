from tamproxy import Sketch, Timer

class SerialConnect(Sketch):

    def setup(self):
        self.timer = Timer()

    def loop(self):
        if (self.timer.millis() > 5000):
            self.stop()

if __name__ == "__main__":
    sketch = SerialConnect()
    sketch.run()
