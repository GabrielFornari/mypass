# MyPass

MyPass is an attempt to develop a password manager aplication with command line interface for Linux. The use of Python language is for testing purpose and the final development should be done in C++.

So far, the aplication can store and recover passwords using encrypted JSON file. It only allows one user. The password must be defined during the first execution of the aplication and cannot be changed.

Usage: <br>
> mypass [OPTION]
<br><br>
- OPTION can be: <br>
  - new: creates a new password entry <br>
  - ls or list: lists all saved password entries <br>
  - ls [KEY] or list [KEY]: lists all password entries that matches KEY <br>
  - up [KEY] or update [KEY]: edit password entry that matches KEY <br>
  - rm [KEY] or remove [KEY]: remove selected password entry that matches KEY <br>
  - help: show help <br>
