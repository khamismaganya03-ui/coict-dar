print ("=== Day 6: smart Grader ===")
jina = input ("weka jina la mwanafunzi: ")
alama = int(input("weka alama (0-100): "))
if alama >= 80:
   grade = "A"
   maoni = "Excellent!"
elif alama >= 60: 
   grade = "B"
   maoni = "Vizuri sana"
elif alama >= 40:
  grade = "C"
   maoni = "Jitahidi zaidi"
else:
  grade = "F"
    maoni = "Umefeli, usikate tamaa"
# Decision ya ziada 
if alama >= 40:
   status = "Amefaulu"
else: 
status = "Amefeli"
print (f"/nMwanafunzi: {jina}")
print (f"Alama: {alama} -> Grade: {grade}")
print (f"Status: {status} - {maoni}")
