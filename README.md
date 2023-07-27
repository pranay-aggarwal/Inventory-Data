
# Inventory Tracker with CSV Data Storage

This is a simple Inventory Tracker program written in Python. The program allows users to add and track products, view the total cost of products by brand, and provides admin settings to manage product data. The data is stored and retrieved using a CSV file, enabling users to save and load their product records even after closing the program.

## How to Use

1. When you run the program, you will be presented with a menu that offers several options:


   ===========Inventory Tracker===========
   1. Open User Options
   2. Open Admin Settings
   3. Memory Options
   4. Quit
   =====================================


2. Choose an option by entering the corresponding number.

### User Options

1. **Add Product:** Allows the user to add a new product. You need to enter the brand name, the product name, and the price.

2. **View Total Price of products:** Displays the total cost of all products of a specific brand. Enter the brand name to view the total cost.

3. **View Prices by product:** Shows prices of all products of a specific brand. Enter the brand name to view the prices.

### Admin Settings

1. **Print all the Products:** Requires the admin password to access. Once authenticated, it displays the brand names and their respective products with prices.

2. **Change Password:** Requires the current admin password for authentication. If the current password is correct, you can set a new admin password. Note that the password will reset to the default when the program is run again.

### Memory Options

1. **Save Data:** Saves all the products in a CSV file named "inventory.csv".

2. **Load Data:** Loads previously saved products from the "inventory.csv" file.

### Important Note

- The default admin password is set to "1234". The admin password can be changed using the "Change Password" option.

- When you run the program again, the password will be reset to the default value, and any saved data will be loaded.

### Data Storage

All the product data is stored in a CSV file named "inventory.csv" in the same directory as the Python script. The data is written and read from this file using the CSV module, allowing for easy storage and retrieval of product records.

### How to Run

1. Save the provided Python script in a file, for example, "inventory_tracker.py".

2. Make sure you have Python installed on your system.

3. Open a terminal or command prompt in the same directory as the Python script.

4. Run the script using the following command:

5. Follow the on-screen instructions to use the Inventory Tracker.

### Dependencies

This program uses the built-in `csv` module in Python, which does not require any additional installation.

### Limitations and Future Improvements

- The program currently stores all data in memory while the program is running. For larger datasets, it may be more efficient to use a database or other persistent storage methods.

- Adding authentication for individual users could enhance security and privacy.

- The program could be improved with features like product modification, stock tracking, and graphical analysis of product data.

- Error handling and input validation could be added to make the program more robust.

- It's essential to keep the "inventory.csv" file secure and avoid sharing it publicly to protect sensitive product data.

Remember that this is a simple inventory tracker program meant for educational purposes and may not be suitable for real-world inventory management.

