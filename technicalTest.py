import unittest

#simulasi data dari database field booking
class TestBookingSystem(unittest.TestCase):

    def setUp(self):
        self.bookings = [
            {"id": 1001, "Booking_id": "BK/000001", "venue_id": 15, "User_id": 12, "date": "2022-12-10", "Start_time": "09:00:00", "end_time": "11:00:00", "price": 1200000},
            {"id": 1005, "Booking_id": "BK/000005", "venue_id": 15, "User_id": 12, "date": "2022-12-10", "Start_time": "09:00:00", "end_time": "11:00:00", "price": 1000000}
        ]

        self.schedule = [
            {"id": 11, "venue_id": 15, "date": "2022-12-10", "start_time": "07:00:00", "end_time": "09:00:00", "price": 800000},
            {"id": 12, "venue_id": 15, "date": "2022-12-10", "start_time": "09:00:00", "end_time": "11:00:00", "price": 1000000},
            {"id": 13, "venue_id": 15, "date": "2022-12-10", "start_time": "11:00:00", "end_time": "13:00:00", "price": 1200000}
        ]

    def test_double_booking(self):
        booked_slots = set()

        for booking in self.bookings:
            booking_slot = f"{booking['venue_id']}_{booking['date']}_{booking['Start_time']}_{booking['end_time']}"
            if booking_slot in booked_slots:
                self.fail(f"Double booking detected (not allowed): {booking_slot}")
            booked_slots.add(booking_slot)

    def test_incorrect_price(self):
        for booking in self.bookings:
            for slot in self.schedule:
                if (slot["venue_id"] == booking["venue_id"] and
                        slot["date"] == booking["date"] and
                        slot["start_time"] == booking["Start_time"]):
                    expected_price = slot["price"]
                    actual_price = booking["price"]
                    self.assertEqual(expected_price, actual_price,
                                 f"Incorrect price detected for booking: {booking}. "
                                 f"Expected price: {expected_price}, Actual price: {actual_price}")
                    
if __name__ == '__main__':
    unittest.main()

