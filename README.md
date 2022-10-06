# MyPass

MyPass is an attempt to develop a password manager aplication with command line interface for Linux. The use of Python language is for testing purpose and the final development should be done in C++.

So far, the aplication can store and recover passwords using encrypted JSON file. It only allows one user. The password must be defined during the first execution of the aplication and cannot be changed.

Usage: 
        mypass [OPTION] [KEY]
        
Option: 
        new: creates a new password entry
        list or ls: lists all saved password entries
        list [KEY] or ls [KEY]: lists all password entries that matches KEY
        up [KEY] or update [KEY]: edit password entry that matches KEY
        rm [KEY] or remove [KEY]: remove selected password entry that matches KEY
        help: show help
