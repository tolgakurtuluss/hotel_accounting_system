# Hotel Accounting System

A simple command-line application for managing hotel bookings, including adding, viewing, updating, and checking out customers. The system also allows for feedback submission and revenue calculation.

## Features

- **Add Booking**: Create a new booking for a customer.
- **View Bookings**: Display all current bookings.
- **Checkout Customer**: Remove a customer's booking upon checkout.
- **Calculate Revenue**: Calculate total revenue from all bookings.
- **Search Bookings**: Search for bookings by customer name or room number.
- **Update Booking**: Modify existing booking details.
- **Feedback**: Leave and view customer feedback.
- **Export Data**: Export booking data to a CSV file.

## Requirements

- Python 3.x
- No external libraries required.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hotel-accounting-system.git
   cd hotel-accounting-system
   ```

2. Run the application:
   ```bash
   python hotel_accounting_system.py
   ```

3. Follow the on-screen menu to navigate through the options.

## Data Storage

The application stores booking data in a JSON file named `hotel_data.json`. Feedback is also stored within the same structure.

## Exporting Data

You can export the booking data to a CSV file named `hotel_data.csv` for further analysis or reporting.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various hotel management systems.
- Thanks to the open-source community for their contributions.
