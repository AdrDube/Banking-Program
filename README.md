# Banking-Program
Uses webscraping for transfer rates. This allows for real time currency conversion
# International Banking Program
#### Video Demo: https://youtu.be/LC2e9LARi1s
#### Description Banking Program with Selenium WebDriver

Overview:
A robust banking program that offers essential functionalities such as viewing account balances, making withdrawals and deposits, and accessing transaction history. 

Key Features:
1.	Currency Conversion: Customers can input transactions in various currencies. Selenium WebDriver automates the fetching of real-time exchange rates from “https://www.xe.com/” to convert these currencies to USD. Ensures accurate and up-to-date conversion rates without manual intervention.
2. Transaction History Storage and Tabulation: Transaction data is stored in a CSV file. Simplifies data management and retrieval. Utilizes the Tabulate library to present transaction details in a clean and organized table format. Includes relevant information such as transaction type and amount.
3.	User-Friendly: Allows for input errors, prompting the user to try again. Regex has been used to ensure the currency is in the correct format. Hides the complexity of web extraction and conversion and outputs data clearly and efficiently. If a user changes their mind, it gives them the ability to cancel a transaction. 

Advantages of the Approach:
1.	Real-time Currency Conversion: The program ensures that currency conversion rates are always current. It also eliminates the need for manual rate updates, reduces errors, and improves customer satisfaction. 
2.	Reduced Storage Space: Minimizes the storage space required compared to storing a large database of historical rates, optimizing resource utilization.
3.	Enhanced User Experience: Tabulate is used to neatly organize transaction history into a table format, making it easier for customers to track their financial activities and understand transaction details at a glance. 
4.	Scalability: The program's architecture allows for scalability, accommodating future updates or expansions in banking functionalities without significant overhead.
5.	Efficiency: Automation through Selenium WebDriver streamlines the currency conversion process, saving customers and the banking system time.
6.	Accuracy and Reliability: Real-time exchange rates ensure customers receive precise conversion values, enhancing trust and credibility in the banking 

##### Documentation
Modules:
selenium.webdriver, re, sys, tabulate
 
Functions:
      	 	
balance(f)
Returns balance in the account file f

:param f: Name of file
:type f: str
:raise FileNotFoundError file does not exist
:return: balance found in a file
:rtype: float

convert(a, c1, c2)

Converts a from currency c1 to currency c2
 
:param a: amount to be converted
:type a : float
:param c1: original currency of a
:type c1: str
:param c2: final currency of a after conversion
:SystemExit if the currency is invalid
:return: a converted into another currency
:rtype: float

deposit(a, f)

Deposits an amount into the balance of a file f and appends the transaction into the file.
 
:param a: amount to be deposited
:type a : float
:param f: Name of file
:type f: str
:raise FileNotFoundError If file does not exist
:return: the new balance
: rtype: float

new_file(n)

Creates a new csv file n with a balance of 100
 
:param n: Name of file
:type n: str
:raise TypeError If n is not a str
:return: None
view_transactions(f)
Shows all transactions found in file f and tabulates the results
 
:param file: Name of file
:type file: str
:raises FileNotFoundError If file does not exist
:return: None

withdrawal(a, f)

Withdraws an amount from the balance in a file and appends the transaction into the file.
 
:param a: amount to be withdrawn
:type a : float
:param f: Name of file
:type f: str
:raises FileNotFoundError If file does not exist
:return: the new balance
:rtype: float

