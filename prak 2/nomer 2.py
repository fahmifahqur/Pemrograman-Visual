class Volume:
    def __init__(self, data):
        self.data = data

    # tabung 
    def v0(self):
        try:
            result = 3.14 * self.data['jari-jari']
            return result
        except:
            return 'invalid data parameter'

    # balok 
    def v1(self):
        try:
            result = self.data['panjang'] * self.data['lebar'] * self.data['tinggi']
            return result
        except:
            return 'invalid data parameter'

    # prisma 
    def v2(self):
        try:
            result = 1.5 * self.data['alas'] * self.data['tinggi']
            return result
        except:
            return 'invalid data parameter'

volumePrisma = Volume({'alas': 44, 'tinggi': 69})
print(str(volumePrisma.v2()))