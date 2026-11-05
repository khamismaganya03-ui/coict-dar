# Day 8 - List na Loop ya wanafunzi wengi

def get_grade(alama):
    if alama >= 80:
      return "A"
    elif alama >= 65:
      return "B+"
    elif alama >= 50:
      return "B"
    elif alama >= 45:
      return "C"
    elif alama >= 35:
      return "D"
    else:
      return "F"

# Orodha ya wanafunzi wote 
wanafunzi = []

# Uliza wanafunzi wangapi 
idadi = int(input("wanafunzi wangapi? "))

# Loop kuchagua data 
for i in range(idadi):
print(f"/n--- mwanafunzi {i+1} ---")
jina = input("jina: ")
alama = int(input("Alama (0-100): "))
grade = get_grade(alama)

# Hifadhi kama dictionary kwenye list 
wanafunzi = {
  "jina" : jina,
  "alama" : alama,
  "grade" : grade
} 
wanafunzi.append(mwanafunzi)                                                                   

# --- print matokeo yote ---
print("n\n\ ===== ORODHA KAMILI =====")
print("Jina\t\tAlama\tGrade")
print("-------------------------------")
for m in wanafunzi:
  print(f"{m['jina']}\t\t{m['alama']}\t{m['grade']}")                                         

# Tafuta alama kubwa zaidi
alama_kubwa = max(wanafunzi, key=lambda x: x['alama'])
print(f"\nMwanafunzi bora: {alama_kubwa ['jina']} na alama {alama_kubwa['alama']})
