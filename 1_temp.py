class temperature:
    def ConvertToF(self,c):
        self.c=c
        print("Temperature in Fahrenheit: ", round(self.c*1.8+32,3))
    def ConvertToC (self,f):
        self.f=f
        print("Temperature in Celsius: ",round((self.f-32)/1.8,3))
        
t=temperature()
c=float(input("Enter temperature in Celsius:"))
t.ConvertToF(c)
f=float(input("Enter temperature in Fahrenheit:"))
t.ConvertToC(f)
