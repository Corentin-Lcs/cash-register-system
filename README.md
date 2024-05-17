<h1 align="center">Cash Register System</h1>

The "Cash Register System" GitHub project is a simplified replica of a store's cash register system using a phpMyAdmin database. The program automatically manages the creation and operations between the information entered by the user and the database.

<p align="center">
  <img src="https://github.com/Corentin-Lcs/cash-register-system/blob/main/Cash_Register.png" alt="Cash_Register.png"/>
</p>

## Prerequisites

In order to facilitate the use of the project / system, I advise you to use `WampServer` (download [here](https://www.wampserver.com/en/download-wampserver-64bits)), a Windows web development environment (i.e. WAMP-like).

WampServer includes three servers (`Apache`, `MySQL` and `MariaDB`), a script interpreter (`PHP`), as well as `phpMyAdmin` for web administration of MySQL databases (Source : [Wikipedia](https://en.wikipedia.org/wiki/WampServer)).

It has an administration interface to manage and administer its servers through a tray icon (icon near the Windows clock).

## Installation

To install the `mysql-connector-python` module from the command prompt, run the following command :

```
pip install mysql-connector-python
```

> To learn more about the features of the module, here is a useful link :
> 
> https://pynative.com/python-mysql-database-connection [EN]

## Usage

To use the program from the command prompt, run the following command :

```
python main.py
```

> The user can now enter his contact details and start shopping.

## Further Information

The `main.py` file contains the following line :

```py
connector = mysql.connector.connect(host="localhost", user="root")
```

It represents the program's connection to the MySQL database server running on localhost, used in conjunction with the phpMyAdmin web management application. The user is named "root" and has no password. If you have a session with a different username and password, here is the modification to make :

```py
connector = mysql.connector.connect(host="localhost", user="username_here", password="password_here")
```

## Project's Structure

```
cash-register-system/
├─ README.md
├─ LICENSE
├─ Cash_Register.png
└─ src/
   ├─ main.py
   ├─ Customer.py
   ├─ Item.py
   ├─ Order.py
   ├─ Stock.py
   ├─ TableManager.py
   └─ Ticket.py
```

## Meta

Created by [@Corentin-Lcs](https://github.com/Corentin-Lcs). Feel free to contact me !

Distributed under the GNU GPLv3 license. See [LICENSE](https://github.com/Corentin-Lcs/cash-register-system/blob/main/LICENSE) for more information.
