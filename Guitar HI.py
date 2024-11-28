class Instrument:
    def type(self):
        print("This is a musical instrument.")

class StringInstrument(Instrument):
    def string_count(self):
        print("This instrument has 6 strings.")

class AcousticGuitar(StringInstrument):
    def body_type(self):
        print("This is an acoustic guitar.")

class ElectricGuitar(StringInstrument):
    def pickup_type(self):
        print("This is an electric guitar with humbucker pickups.")

class Guitar(AcousticGuitar, ElectricGuitar):
    pass

g = Guitar()

g.type()          # From Instrument
g.string_count()  # From StringInstrument
g.body_type()     # From AcousticGuitar
g.pickup_type()   # From ElectricGuitar
