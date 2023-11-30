from abc import ABC
from datetime import datetime


class Szoba(ABC):

    def __init__(self, price, room_number):
        self.price = price
        self.room_number = room_number


class EgyagyasSzoba(Szoba):

    def __init__(self, room_number):
        super().__init__(10, room_number)
        self._number_of_beds = 1


class KetagyasSzoba(Szoba):

    def __init__(self, room_number):
        super().__init__(20, room_number)
        self._number_of_beds = 2


class Szalloda:

    def __init__(self, name):
        self._name = name
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def reserve(self, room_number, date):
        for room in self.rooms:
            if (room.room_number == room_number
                    and datetime.strptime(date, "%Y.%m.%d") > datetime.now()):
                reservation = Foglalas(room_number, date)
                self.reservations.append(reservation)
                print(f"Foglalás ára: {room.price}")
                return reservation

    def cancel_reservation(self, room_number, date):
        found_reservation = None
        for reservation in self.reservations:
            if reservation.room_number == room_number and reservation.date == date:
                found_reservation = reservation
                break
        if found_reservation:
            self.reservations.remove(found_reservation)
            print(f"Szobaszám: {found_reservation.room_number},"
                  f" dátum: {found_reservation.date} foglalása lemondva")
        else:
            print("Foglalás nem található")

    def list_reservations(self):
        for reservation in self.reservations:
            print(f"Szobaszám: {reservation.room_number},"
                  f" dátum: {reservation.date}")


class Foglalas:

    def __init__(self, room_number, date):
        self.room_number = room_number
        self.date = date


"""test_hotel = Szalloda("teszt szálloda")
test_hotel.add_room(EgyagyasSzoba(101))
test_hotel.add_room(KetagyasSzoba(102))

res1 = test_hotel.reserve(101, "2023.12.01")
res2 = test_hotel.reserve(102, "2023.11.29")

test_hotel.list_reservations()

test_hotel.cancel_reservation(101, "2023.12.01")"""


def create_hotel(name):
    hotel = Szalloda(name)
    hotel.add_room(EgyagyasSzoba(101))
    hotel.add_room(KetagyasSzoba(102))
    hotel.add_room(KetagyasSzoba(103))

    hotel.reserve(101, "2023.12.02")
    hotel.reserve(102, "2023.12.02")
    hotel.reserve(103, "2023.12.02")
    hotel.reserve(101, "2023.12.01")
    hotel.reserve(102, "2023.12.01")

    return hotel


def main():

    hotel = create_hotel("Hotel")

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Foglalás törlése")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        choice = input("Adja meg a választott művelet számát: ")

        if choice == "1":
            room_number = input("Adja meg a szobaszámot: ")
            date = str(input("Adja meg a foglalás dátumát (ÉÉÉÉ.HH.NN formátumban): "))
            hotel.reserve(room_number, date)

        elif choice == "2":
            if hotel.reservations:
                room_number = input("Adja meg a szobaszámot: ")
                date = input("Adja meg a foglalás dátumát (ÉÉÉÉ.HH.NN formátumban): ")
                hotel.cancel_reservation(room_number, date)
            else:
                print("Érvénytelen sorszám!")

        elif choice == "3":
            if hotel.reservations:
                hotel.list_reservations()
            else:
                print("Nincsenek foglalások")

        elif choice == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    main()

