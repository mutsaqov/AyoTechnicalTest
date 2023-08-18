# AyoTechnicalTest

======================================================================
FAIL: test_double_booking (__main__.TestBookingSystem.test_double_booking)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Arga Noufal\Downloads\Ativ\technicaltest\technicalTest.py", line 25, in test_double_booking
    self.fail(f"Double booking detected (not allowed): {booking_slot}")
AssertionError: Double booking detected (not allowed): 15_2022-12-10_09:00:00_11:00:00

======================================================================
FAIL: test_incorrect_price (__main__.TestBookingSystem.test_incorrect_price)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Arga Noufal\Downloads\Ativ\technicaltest\technicalTest.py", line 36, in test_incorrect_price
    self.assertEqual(expected_price, actual_price,
AssertionError: 1000000 != 1200000 : Incorrect price detected for booking: {'id': 1001, 'Booking_id': 'BK/000001', 'venue_id': 15, 'User_id': 12, 'date': '2022-12-10', 'Start_time': '09:00:00', 'end_time': '11:00:00', 'price': 1200000}. Expected price: 1000000, Actual price: 1200000

----------------------------------------------------------------------




Setelah di running itu ditemukan 2 error berbeda tetapi identik:
Error pertama : [AssertionError: Double booking detected (not allowed): 15_2022-12-10_09:00:00_11:00:00]
1. Disebabkan karena ketika melakukan pengecekan apakah ada data yang double booking berdasarkan dummy data pada self.bookings 
2. Pada data dummy diatas ditemukan bahwa terdapat venue, date, start time, and end time: "15_2022-12-10_09:00:00_11:00:00".
3. Ketika case pengujian melakukan pengecekan pada data booking kedua, case uji akan mencoba melakukan penambahan slot booking yang sama ke set booked_slots, tetapi karena slot ini sudah ada yang mengisi dan identik data maka kasus uji dinyatakan gagal
4. Perlu adanya tambahan logic untuk case ini sesuai dengan ketentuan dari sistem dan datanya itu sendiri ketika menangani case double booking dengan data identik
5. Seharusnya ini sudah terhandle jika di hapus salah satu datanya maka tidak akan ada error ketika run, tetapi karena dua dummy data yang identik tadi di hardcode pada script maka ada fail ketika run testnya

Error Kedua: [Expected price: 1000000, Actual price: 1200000]
1. Hal ini disebabkan karena assertion terus gagal ketika melakukan perbandingan antara harga expected dengan actual price pada data terkait ada missmatch data
2. pada data dummy ditemukan bahwa price yang terinput adalah 1200000 sedangkan pada database dummynya seharusnya untuk venue id : 15, tanggal 10-12-2022, dan waktu start 09:00:00 berakhir pada 11:00:00 pricenya adalah 1000000
3. Perlu adanya tambahan logic untuk case ini sesuai dengan ketentuan dari sistem dan datanya itu sendiri ketika menangani case jika harga yang terinput tidak sesuai dengan base data dari harga lapangan tersebut
4. Seharusnya ini sudah terhandle jika di hapus salah satu datanya maka tidak akan ada error ketika run, tetapi karena dua dummy data yang identik tadi di hardcode pada script maka ada fail ketika run testnya atau menggunakan harga yang sesuai dengan base dari harga terkait
