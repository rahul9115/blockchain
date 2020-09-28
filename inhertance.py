global a
class A:
    a = 0
    def __init__(self,son):
        self.a=son
        
        
    def display(self):
      pass  
        
class B(A):
    def __init__(self,son):
        self.son=100
        super().__init__(100)
        
        
    def balance(self):
        self.total=self.a+self.son
        
    def display(self):
        print("Sons total",self.total)       


b=B(100)


b.balance()
b.display()
