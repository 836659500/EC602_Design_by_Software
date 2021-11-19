class Polynomial():
    def __init__(self,a=0):
        self.a = {}
        if a==0:
            self.a=0
        if isinstance(a,dict):
            for i in range(len(a)):
                self.a[-i-1] = a[-i-1]
        if isinstance(a,list):
            for i in range(len(a)):
                self.a[-i-1] = a[-i-1]
    def deriv(self):
        ori = [0 for i in range(len(self.a)-1)]
        for i in range(len(ori)):
            ori[-i-1] = self.a[-i-2]*(i+1)
        return Polynomial(ori)
    def eval(self,x):
        ori = 0
        for i in range(len(self.a)):
            ori =  self.a[-i-1]*x**i + ori 
        return ori
    def __getitem__(self,index):
        gget = self.a.get(-index-1,0)
        return gget
    def __setitem__(self,index,gget):
        self.a[-index-1] = gget
    def __eq__(self,value):
        return self.a==value.a
    def __add__(self,value):
        "Return self.a+value"
        if len(self.a) <= len(value.a):
            for i in range(len(self.a)):
                value.a[-i-1] = self.a[-i-1] +value.a[-i-1]
            return Polynomial(value.a)
        if len(self.a) > len(value.a):
            for i in range(len(value.a)):
                self.a[-i-1] = self.a[-i-1] + value.a[-i-1]
            return Polynomial(self.a)
    def __sub__(self,value):
        "Return self.a-value"
        if len(self.a) <= len(value.a):
            for i in range(len(self.a)):
                value.a[-i-1] = self.a[-i-1] - value.a[-i-1]
            for i in range(len(self.a),len(value.a)):
                value.a[-i-1] = - value.a[-i-1]
            return Polynomial(value.a)
        if len(self.a) > len(value.a):
            for i in range(len(value.a)):
                self.a[-i-1] = self.a[-i-1] - value.a[-i-1]
            return Polynomial(self.a)
    def __mul__(self,value):
        out = [0 for i in range(len(self.a)+len(value.a)-1)]
        "Return self.a*value"
        for i in range(len(value.a)):
            for o in range(len(self.a)):
                out[-i-o-1] = out[-i-o-1] + value.a[-i-1]*self.a[-o-1]
        return Polynomial(out)
