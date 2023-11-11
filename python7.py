a = str(input("Enter Pre monsoon or Post monsoon"))
b = str(input("Soil Quality"))
c = 0
while a == "pre monsoon" and b == "dry":
    c = str(input("Enter bottom Soil Quality"))
    break
if a == "pre monsoon" and c == "dry":
    print("plantable crops= Rice, maize, cotton")
elif a == "pre monsoon" and c == "wet":
    print("Cannot plant crops")
elif a == "post monsoon":
    print("plantable crops=  padyy, millets, maize, moong, groudnut, red chillies, cotton, soyabean, sugarcane")
