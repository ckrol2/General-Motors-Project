# General Motors Preternship

File: LinkedList.py

This file creates a linked list data structure in Python. The linked list was created to preserve memory when compared to Python lists and dictionaries, which function as dynamic arrays and hash tables, respectively. A linked list can reduce memory usage by up to 50% of that of a Python list and up to 70% of a Python dictionary. 

The Node class contains attributes corresponding to Event Data Recording (EDR) for a given vehicle, which is identified by its VIN. These attributes can be changed depending on what it is you wish to store in the linked list. 

The Linked List class contains two added funtions, the first of which is add_first(), which adds a new Node at the head of the Linked List. This allows for more efficient time complexity, giving the linked list a O(1) insert rather than O(n), saving valuable time as the linked list grows in size. This also allows for a built-in cache when iterating through the linked list, in that the most recently stored nodes will be at the front.

The second function is remove_node(), which allows the user to query by VIN and remove the corresponding node from the linked list. This allows for easy data maintenance and is helpful when deleting data that is not useful from the linked list, saving both space in memory and time for future iterations through the linked list.

---------------------------------------------------------------

File: dataRead.py

This file creates a function called readIn() which reads in raw data from csv files and inserts it into the linked list data structure. The function can be altered to fit the user's needs by reading data from different files and querying by different columns.

---------------------------------------------------------------

File: plotter.py

This file visualizes EDR data from GM Advanced Driving Assistance Systems by plotting a bar graph showing the percentage distribution of gap settings in cars that reach three different speed ranges. The axes being plotted can be altered to visualize different data. The current structure of the graph is three touching bars representing the three gap settings (Near, Medium, and Far) which is in turn being measured at three different speed ranges.
