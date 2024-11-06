import json
import os
import csv

DATA_FILE = 'hotel_data.json'

def load_data():
    """Load hotel data from JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    """Save hotel data to JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_booking(customer_name, room_number, nights, rate_per_night):
    """Add a new booking."""
    data = load_data()
    total_charge = nights * rate_per_night

    booking = {
        "customer_name": customer_name,
        "room_number": room_number,
        "nights": nights,
        "rate_per_night": rate_per_night,
        "total_charge": total_charge,
        "feedback": None  # Initialize feedback as None
    }

    data[customer_name] = booking
    save_data(data)
    print(f"Booking added for {customer_name} in room {room_number}.")

def view_bookings():
    """View all bookings."""
    data = load_data()
    if not data:
        print("No bookings found.")
        return

    for customer, details in data.items():
        print(f"\nCustomer: {customer}")
        for key, value in details.items():
            print(f"  {key}: {value}")

def checkout(customer_name):
    """Checkout a customer and remove their booking."""
    data = load_data()
    if customer_name in data:
        del data[customer_name]
        save_data(data)
        print(f"Checked out {customer_name}.")
    else:
        print(f"No booking found for {customer_name}.")

def calculate_revenue():
    """Calculate total revenue from bookings."""
    data = load_data()
    total_revenue = sum(booking["total_charge"] for booking in data.values())
    print(f"Total Revenue: ${total_revenue:.2f}")

def search_bookings(search_term):
    """Search for bookings by customer name or room number."""
    data = load_data()
    results = {customer: details for customer, details in data.items() if search_term in customer or str(details["room_number"]) == search_term}
    
    if not results:
        print("No bookings found for the search term.")
        return

    for customer, details in results.items():
        print(f"\nCustomer: {customer}")
        for key, value in details.items():
            print(f"  {key}: {value}")

def update_booking(customer_name):
    """Update an existing booking."""
    data = load_data()
    if customer_name not in data:
        print(f"No booking found for {customer_name}.")
        return

    print("Current booking details:")
    view_bookings()

    try:
        nights = int(input("Enter new number of nights (or press Enter to keep current): ") or data[customer_name]["nights"])
        rate_per_night = float(input("Enter new rate per night (or press Enter to keep current): ") or data[customer_name]["rate_per_night"])
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    data[customer_name]["nights"] = nights
    data[customer_name]["rate_per_night"] = rate_per_night
    data[customer_name]["total_charge"] = nights * rate_per_night
    save_data(data)
    print(f"Booking updated for {customer_name}.")


def leave_feedback(customer_name):
    """Allow customers to leave feedback."""
    data = load_data()
    if customer_name not in data:
        print(f"No booking found for {customer_name}.")
        return

    print("Please rate your stay with us:")
    print("1. Excellent")
    print("2. Good")
    print("3. Fair")
    print("4. Poor")

    rating = input("Enter your rating (1-4): ")

    # Validate rating input
    while rating not in ['1', '2', '3', '4']:
        print("Invalid rating. Please enter a number from 1 to 4.")
        rating = input("Enter your rating (1-4): ")

    rating_map = {
        '1': 'Excellent',
        '2': 'Good',
        '3': 'Fair',
        '4': 'Poor'
    }

    feedback = input("Enter your feedback: ")

    data[customer_name]["feedback"] = {
                "rating": rating_map[rating],
        "comment": feedback
    }

    save_data(data)
    print("Thank you for your feedback!")

def view_feedback():
    """View all feedback."""
    data = load_data()
    if not data:
        print("No bookings found.")
        return

    for customer, details in data.items():
        if details["feedback"]:
            print(f"\nCustomer: {customer}")
            print(f"Rating: {details['feedback']['rating']}")
            print(f"Comment: {details['feedback']['comment']}")

def display_feedback_menu():
    """Display the feedback menu."""
    print("\n--- Feedback Menu ---")
    print("1. Leave Feedback")
    print("2. View Feedback")
    print("3. Back to Main Menu")

def feedback_menu():
    """Display the feedback menu and handle user input."""
    while True:
        display_feedback_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            customer_name = input("Enter customer name to leave feedback: ")
            leave_feedback(customer_name)

        elif choice == '2':
            view_feedback()

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

def display_menu():
    """Display the main menu."""
    print("\n--- Hotel Accounting System ---")
    print("1. Add Booking")
    print("2. View Bookings")
    print("3. Checkout Customer")
    print("4. Calculate Revenue")
    print("5. Search Bookings")
    print("6. Update Booking")
    print("7. Feedback")
    print("8. Export Data to CSV")
    print("9. Exit")

def export_data():
    """Export hotel data to a CSV file."""
    data = load_data()
    if not data:
        print("No data to export.")
        return

    with open('hotel_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['customer_name', 'room_number', 'nights', 'rate_per_night', 'total_charge', 'feedback']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for customer, details in data.items():
            writer.writerow({
                'customer_name': customer,
                'room_number': details['room_number'],
                'nights': details['nights'],
                'rate_per_night': details['rate_per_night'],
                'total_charge': details['total_charge'],
                'feedback': details['feedback']['rating'] if details['feedback'] else None
            })

    print("Data exported to hotel_data.csv successfully.")

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        display_menu()
        choice = input("Choose an option (1-9): ")

        if choice == '1':
            customer_name = input("Enter customer name: ")
            room_number = input("Enter room number: ")
            nights = input("Enter number of nights: ")
            rate_per_night = input("Enter rate per night: ")

            # Validate inputs
            try:
                room_number = int(room_number)
                nights = int(nights)
                rate_per_night = float(rate_per_night)
                add_booking(customer_name, room_number, nights, rate_per_night)
            except ValueError:
                print("Invalid input. Please enter numeric values for room number, nights, and rate per night.")

        elif choice == '2':
            view_bookings()

        elif choice == '3':
            customer_name = input("Enter customer name for checkout: ")
            checkout(customer_name)

        elif choice == '4':
            calculate_revenue()

        elif choice == '5':
            search_term = input("Enter customer name or room number to search: ")
            search_bookings(search_term)

        elif choice == '6':
            customer_name = input("Enter customer name to update booking: ")
            update_booking(customer_name)

        elif choice == '7':
            feedback_menu()

        elif choice == '8':
            export_data()

        elif choice == '9':
            print("Exiting the system. Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main_menu()
