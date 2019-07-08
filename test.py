from per import percen
def testpercen():
   p=percen(100,10)
   assert p == 10
   a="10"
   b="0"
   p = percen(a,b)
   assert p == "Invalid"
