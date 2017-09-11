class Allergies(object):
    def __init__(self, number):
        allergyList = ['eggs',
                       'peanuts', 
                       'shellfish',
                       'strawberries',
                       'tomatoes', 
                       'chocolate', 
                       'pollen',
                       'cats'] 
        
        # Obtain 2s complement of input to create a
        #    bit array.
        bits = []
        self.allergicTo = []
                    
        while number > 0:            
            bits.append(number % 2)
            number //= 2
        
        i = 0
        while i < len(bits) and i < len(allergyList):
            if bits[i] == 1:
                self.allergicTo.append(allergyList[i])
            i += 1
            

    def is_allergic_to(self, string):
        if string in self.allergicTo:
            return True
        return False
    

    @property
    def lst(self):  
        return self.allergicTo
