movies = {
    "Finding Nemo": [5, 2],
    "Moana": [6, 3],
    "Batman": [18, 5],
    "The Lion King": [10, 4]
}
while True:

    title = input("Podaj tytuł filmu (wpisz 'koniec' aby zamknac): ").strip().title()

    if title.lower() == "koniec":
        print("Koniec")
        break

    if title in movies:
        age = int(input("Podaj wiek: "))

        min_age, tickets = movies[title]

        if age >= min_age:

            if tickets > 0:
                movies[title][1] -= 1
                print(f"Bilet zarezerwowany! Pozostało biletów: {movies[title][1]}")
            else:
                print("Brak dostępnych biletów")

        else:
            print("Masz za malo lat.")

    else:
        print("Brak filmu")
