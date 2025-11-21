# Zapytaj użytkownika o nazwisko

name = input("Jak masz na nazwisko?: ")

# Zapytaj użytkownika o wiek
age = input("Ile masz lat?: ")

# Zapytaj użytkownika o miasto

city = input("Gdzie mieszkasz?: ")

# Zapytaj użytkownika o jego zainteresowania

interest = input("Czym sie interesujesz: ")

# Utwórz tekst wyjściowy za pomocą formatowania ciągów

string = "Czesc {}, Masz {} lat. Mieszkasz w {}, interesujsz się {} "

output = string.format(name,age,city,interest)

# Wydrukuj tekst wyjściowy

print(output)