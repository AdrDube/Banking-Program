from selenium import webdriver
import re
import sys
from selenium.webdriver.common.by import By
from tabulate import tabulate

#esketit

import time
def main():
    if len(sys.argv)>1:
         account=sys.argv[1]+".csv"
    else:
         account=(input("Enter your account name ")).strip()+".csv"
    new_file(account)
    print("Welcome to the Dube Express bank account service")
    choice=input(f"what would you like to do today:\na) View Balance\nb) View Transactions\nc) Withdraw/Deposit ").strip().lower()
    match choice:
            case "a": print("Your balance is: USD", balance(account))
            case "b": view_transactions(account)
            case "c":
              try:
                  amount=float(input("Enter the amount you want to withdraw/deposit "))
              except TypeError:
                  sys.exit("Invalid amount try again ")
              if input("Is it USD? y/n ").strip().lower()=="n":
                  currency=input("Enter a valid currency XXX ").strip().upper()
                  while not re.fullmatch("^[A-Z]{3}?", currency):
                        currency=input("The format used is not recognized. Try again ")
                  amount=convert(amount, currency, "USD")
              while True:
                   match input("a) Deposit or b) Withdraw or c) Cancel ").strip().lower():
                        case "a": 
                            deposit(amount, account)
                            break
                        case "b": 
                             withdrawal(amount, account)
                             break
                        case "c": 
                             print("Transaction cancelled. Thank you")
                             break
                        case _: print("Invalid response. Try again")
              
            case _: print("Invalid response")     
def new_file(n):
    '''
    Creates a new .CSV file n with a balance of 100

    :param n: Name of file
    :type n: str
    :raise TypeError If n is not a str
    :return: None
    '''
    try:
         with open(n, "x") as file:
            file.write("Transaction, Amount(USD), Balance(USD)\n")
            file.write("Sign on bonus,100.00 ,100.00\n")
    except FileExistsError:
         pass
    return None
def convert(a, c1, c2):
    '''
    Converts a from currency c1 to currency c2

    :param a: amount to be converted
    :type a : float
    :param c1: original currency of a
    :type c1: str
    :param c2: final currency of a after conversion
    :SystemExit if the currency is invalid
    :return: a converted into another currency
    :rtype: float
    '''
    driver = webdriver.Chrome()
    try:
        driver.get(f"https://www.xe.com/currencyconverter/convert/?Amount={a}&From={c1}&To={c2}")
        original_info=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[1]").text
        converted_info=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div/p[2]").text
        time.sleep(8)
    except:

        sys.exit("Invalid currency")
    print(f"{original_info} {converted_info}")
    return float(converted_info.split()[0])
def balance(f):
    '''
    Returns balance in the account file f

    :param f: Name of file
    :type f: str
    :raise FileNotFoundError file does not exist
    :return: balance found in a file
    :rtype: float
    '''

    with open(f) as file:
                 for line in file:
                     pass
                 return float(line.split(",")[2].strip())
def deposit(a, f):
     '''
    Deposits an amount into the balance of a file f and appends the transaction into the file.

    :param a: amount to be deposited
    :type a : float
    :param f: Name of file
    :type f: str
    :raise FileNotFoundError If file does not exist
    :return: the new balance
    : rtype: float
    '''
     new_balance= balance(f)+ a
     with open(f, "a") as file:
          file.write(f"Deposit,{a:.2f},{new_balance:.2f}\n")
     return new_balance     
def withdrawal(a, f):
     '''
    Withdraws an amount from the balance in a file and appends the transaction into the file.

    :param a: amount to be withdrawn
    :type a : float
    :param f: Name of file
    :type f: str
    :raises FileNotFoundError If file does not exist
    :return: the new balance
    : rtype: float
    '''
     new_balance= balance(f) - a
     with open(f, "a") as file:
          file.write(f"Withdrawal,{a:.2f}, {new_balance:.2f}\n")
     return new_balance
def view_transactions(f):
     '''e
    Shows all transactions found in file f and tabulates the results

    :param f: Name of file
    :type f: str
    :raises FileNotFoundError If file does not exist
    :return: None
    '''
     transactions=[]
     with open(f) as file:
          for line in file:
               transactions.append(line.strip().split(","))
     print(tabulate(transactions, tablefmt="grid"))


if __name__=="__main__":
     main()
