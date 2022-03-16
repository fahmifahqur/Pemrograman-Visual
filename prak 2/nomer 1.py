class LuasKeliling:
    def __init__(self, isLuas, data):
        self.isLuas = isLuas
        self.data = data

    # persegi
    def r0(self):
        try:
            if self.isLuas == True:
                result = self.data['sisi'] * self.data['sisi']
            else:
                result = self.data['sisi'] * 4
        except:
            return 'invalid data'
        return result
    
    # segitiga 
    def r1(self):
        try:
            if self.isLuas == True:
                result = 0.5 * self.data['alas'] * self.data['tinggi']
            else:
                result = self.data['sisi ke-1'] + self.data['sisi ke-2'] + self.data['sisi ke-3']
        except:
            return 'invalid data'
        return result
    
    # jajargenjang 
    def r2(self):
        try:
            if self.isLuas == True:
                result = self.data['alas'] * self.data['tinggi']
            else:
                result = (self.data['alas'] + self.data['tinggi']) * 2
        except:
            return 'invalid data'
        return result

r = LuasKeliling(False, {'sisi ke-1': 6, 'sisi ke-2': 15, 'sisi ke-3': 29})
funct = 'print(str(r.r1()))'
eval(funct)