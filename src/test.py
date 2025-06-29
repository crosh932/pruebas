import os

 
class Calculator :
    def  sum(self, a: int , b: int) -> int:
        return a + b
    

def test_sum():
    calc = Calculator()
    assert calc.sum(1, 2) == 3