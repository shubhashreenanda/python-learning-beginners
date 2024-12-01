class Flight:
    def __init__(self,engine):
        self.engine = engine

    def startEngine(self): #Ducktyping
        self.engine.start();

class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")

class BoingEngine:
    def start(self):
        print("Starting Boing engine")

ae = AirbusEngine()
f = Flight(ae)
f.startEngine()

be = BoingEngine()
f = Flight(be)
f.startEngine()