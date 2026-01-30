class Pokemon:
    def __init__(self, name, id, height, weight, type1, type2, gen):
        self.name = name
        self.id = id
        self.height = height
        self.weight = weight
        self.type1 = type1
        self.type2 = type2
        self.gen = gen

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight
    
    def get_type1(self):
        return self.type1
    
    def get_type2(self):
        return self.type2
    
    def get_gen(self):
        return self.gen
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_id(self, new_id):
        self.id = new_id
    
    def set_height(self, new_height):
        self.height = new_height
    
    def set_weight(self, new_weight):
        self.weight = new_weight
    
    def set_type1(self, new_type1):
        self.type1 = new_type1
    
    def set_type2(self, new_type2):
        self.type2 = new_type2
    
    def set_gen(self, new_gen):
        self.gen = new_gen

    def show(self):
        print("ID               : " + str(self.get_id()))
        print("Name             : " + str(self.get_name()))
        print("Type 1           : " + str(self.get_type1()))
        print("Type 2           : " + str(self.get_type2()))
        print("Height Meters    : " + str(self.get_height()))
        print("Weight Kilograms : " + str(self.get_weight()))
        print("Generation       : " + str(self.get_gen()))