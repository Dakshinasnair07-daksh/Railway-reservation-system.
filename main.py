import random
import string

# ─────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────
TOTAL_SEATS = 50

# Stores bookings: { booking_id: { "name", "age", "seat" } }
reservations = {}

# Tracks which seat numbers are taken
booked_seats = set()


# ─────────────────────────────────────────
#  Helper – generate unique booking ID
# ─────────────────────────────────────────
def generate_booking_id():
    while True:
        bid = "RR" + "".join(random.choices(string.digits, k=6))
        if bid not in reservations:
            return bid


# ─────────────────────────────────────────
#  Feature 1 – Check Availability
# ─────────────────────────────────────────
def check_availability():
    available = TOTAL_SEATS - len(booked_seats)
    print(f"\n{'='*40}")
    print(f"  Total Seats   : {TOTAL_SEATS}")
    print(f"  Booked Seats  : {len(booked_seats)}")
    print(f"  Available     : {available}")
    if available > 0:
        free = [s for s in range(1, TOTAL_SEATS + 1) if s not in booked_seats]
        print(f"  Free Seat Nos : {free}")
    else:
        print("  *** Train is FULLY BOOKED ***")
    print(f"{'='*40}")


# ─────────────────────────────────────────
#  Feature 2 – Book Ticket
# ─────────────────────────────────────────
def book_ticket():
    if len(booked_seats) >= TOTAL_SEATS:
        print("\n  Sorry! No seats available. Train is fully booked.")
        return

    print("\n--- Book Ticket ---")
    name = input("  Enter passenger name : ").strip()
    if not name:
        print("  Name cannot be empty.")
        return

    age_str = input("  Enter passenger age  : ").strip()
    if not age_str.isdigit() or int(age_str) <= 0:
        print("  Invalid age.")
        return
    age = int(age_str)

    # Assign the lowest available seat
    seat = next(s for s in range(1, TOTAL_SEATS + 1) if s not in booked_seats)
    booked_seats.add(seat)

    bid = generate_booking_id()
    reservations[bid] = {"name": name, "age": age, "seat": seat}

    print(f"\n  ✅ Ticket Booked Successfully!")
    print(f"  Booking ID : {bid}")
    print(f"  Seat No.   : {seat}")
    print(f"  Passenger  : {name} (Age: {age})")


# ─────────────────────────────────────────
#  Feature 3 – View Ticket
# ─────────────────────────────────────────
def view_ticket():
    print("\n--- View Ticket ---")
    bid = input("  Enter Booking ID : ").strip().upper()

    if bid not in reservations:
        print("  ❌ Booking ID not found.")
        return

    info = reservations[bid]
    print(f"\n  {'─'*30}")
    print(f"  Booking ID : {bid}")
    print(f"  Name       : {info['name']}")
    print(f"  Age        : {info['age']}")
    print(f"  Seat No.   : {info['seat']}")
    print(f"  {'─'*30}")


# ─────────────────────────────────────────
#  Feature 4 – Cancel Ticket
# ─────────────────────────────────────────
def cancel_ticket():
    print("\n--- Cancel Ticket ---")
    bid = input("  Enter Booking ID to cancel : ").strip().upper()

    if bid not in reservations:
        print("  ❌ Booking ID not found.")
        return

    info = reservations.pop(bid)
    booked_seats.discard(info["seat"])

    print(f"\n  ✅ Booking {bid} cancelled successfully.")
    print(f"  Seat {info['seat']} is now available again.")


# ─────────────────────────────────────────
#  Main Menu
# ─────────────────────────────────────────
def main():
    print("\n" + "=" * 40)
    print("   🚆 RAILWAY RESERVATION SYSTEM 🚆")
    print("=" * 40)

    menu = {
        "1": ("Check Availability", check_availability),
        "2": ("Book Ticket",        book_ticket),
        "3": ("View Ticket",        view_ticket),
        "4": ("Cancel Ticket",      cancel_ticket),
        "5": ("Exit",               None),
    }

    while True:
        print("\n  MENU")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        choice = input("\n  Enter your choice (1-5): ").strip()

        if choice == "5":
            print("\n  Thank you for using Railway Reservation System. Goodbye! 👋\n")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("  ⚠️  Invalid choice. Please enter 1–5.")


if __name__ == "__main__":
    main()
