# Zliczanie liczby samogłosek i spółgłosek w zadanym ciągu


# %%
# Utwórz zmienne "vowels" (samogłoski) i "consonants" (spółgłoski) i przypisz każdej z nich wartość 0

vowels = 0
consonants = 0

# Utwórz pętlę i przeiteruj łańcuch znaków „Programowanie Pythona”

name = "Programowanie Pythona"

# Utwórz instrukcję warunkową IF-ELSE, która wyliczy liczbę samogłosek i spółgłosek w danym łańcuchu znaków

for char in name.lower():
    if char.isalpha():
        if char in "aeiouyąęó":
            vowels += 1
        else:
            consonants += 1

# Wydrukuj łączną liczbę samogłosek i spółgłosek w danym łańcuchu znaków

print("Liczba samogłosek:", vowels)
print("Liczba spółgłosek:", consonants)





# Tworzymy symulator ciekawskiego dziecka za pomocą pętli

# Program Symulujący Ciekawskiego Malucha

# Wszyscy wiemy, że dzieci są z natury ciekawe i ciągle zadają pytania. Często nie przekonują ich odpowiedzi, więc wciąż pytają: dlaczego?

# Spróbujmy to odtworzyć i zbudować program w Pythonie, który symuluje zachowanie ciekawego malucha przy użyciu pętli while…

# Maluch będzie ciągle powtarzał „dlaczego”, dopóki rodzic nie powie „to wszystko!”

# Zatem spróbujmy zbudować logikę opartą na tym, używając pętli while.

# %%
# Użyj modułu random

import random

# Stwórz listę "questions" składającą się z 3 pytań, które często zadają dzieci

questions = ["Why is the sky blue?\n", "Why is the sun round?\n", "Where are all the dinosaurs?\n"]

# Wybierz losowe pytanie z danej listy za pomocą instrukcji warunkowej

question = random.choice(questions)

# Zadaj wybrane pytanie za pomocą funkcji input()
# Pytania muszą zachować jednolite formatowanie
# Aby to uzyskać, przekonwertuje wszystkie odpowiedzi na małe litery i usuń wszelkie nadmiarowe spacje

answer = input(question).strip().lower()

# Poczekaj do czasu, aż użytkownik wprowadzi hasło „To wszystko”

while answer != "to wszystko":
    answer = input("Czekam\n").strip().lower()

# Wyświetl wiadomość

print('To wszystko')


# Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):
   return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b == 0:
        return "Dzielenie przez zero"
    return a / b

# Wyświetl listę operacji
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

# Pozwól użytkownikowi wybrać żądane działanie
op = input("Please enter choice (a/ b/ c/ d): ").lower()

# Przechwyć 2 liczby wprowadzone przez użytkownika i przekonwertuj je na format liczby całkowite
a = float(input("Pierwsza liczba: "))
b = float(input("Druga liczba: "))

# Logika do wykonywania określonej operacji za pomocą instrukcji IF -ELIF -ELSE.

if op == "a":
    print("Result:", add(a, b))
elif op == "b":
    print("Result:", subtract(a, b))
elif op == "c":
    print("Result:", multiply(a, b))
elif op == "d":
    print("Result:", divide(a, b))
 # Jeśli użytkownik wybierze operację, która nie jest dostępna, wyświetl komunikat o błędzie
else:
    print("Invalid operation selected.")
