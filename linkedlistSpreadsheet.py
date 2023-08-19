from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell


# class ListNode:
#     '''
#     Define a node in the linked list
#     '''
#
#     def __init__(self, word_frequency: WordFrequency):
#         self.word_frequency = word_frequency
#         self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------
from typing import List, Tuple
import sys


import time

class node_column:
    def __init__(self, column, value=None):
        self.column_next=None
        self.column_prev=None
        self.value=value
        self.column=column#stores the column index of the node.
        self.row_nodes = []# stores the row nodes that correspond to this column node.

class list_column:
    def __init__(self):
        self.head=None
        self.tail=None

class node_row:
    def __init__(self, row, value=None):
        self.row=row
        self.row_next=None
        self.row_prev=None
        self.columns=list_column()#stores the column nodes that correspond to this row node.


    def listcolumn(self, column_max):#initializes the columns attribute with column nodes
        self.columns=list_column()
        column_max=column_max+1
        for i in range(column_max):
            current_node=node_column(i)#0 to column_max, and for each index, it creates a new node_column

            if not self.columns.head:
                self.columns.head=current_node
                self.columns.tail=current_node
                self.columns.head.column_prev=None
                self.columns.tail.column_next=None

            else:
                self.columns.tail.column_next=current_node
                current_node.column_prev=self.columns.tail
                self.columns.tail=current_node
                self.columns.tail.column_next=None
    
class LinkedListSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.nrows=0
        self.ncolumns=0
        self.head=None
        self.tail=None
        
        # TO BE IMPLEMENTED
        pass

    def buildSpreadsheet(self, lCells: List[Cell]):
        """ 
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        max_row, max_column=0,0
        for cell in lCells:
            max_row=max(max_row, cell.row)
            max_column=max(max_column, cell.col)

        self.nrows=max_row+1
        self.ncolumns=max_column+1

        # the number of row and columns
        # for cell in lCells:
        #     if cell.row>self.nrows:
        #         self.nrows=cell.row
        #     if cell.col>self.ncolumns:
        #         self.ncolumns=cell.col

        #create an a empty row and column

        for i in range(self.nrows):
            current_node=node_row(i)#creates a new node_row for each row. For each node_row, it also calls the listcolumn method to initialize the columns attribute with column nodes.
            current_node.listcolumn(max_column)

            if not self.head:
                self.head=current_node
                self.tail=current_node
                self.tail.row_next=None
                self.head.row_prev=None
            
            else:
                self.tail.row_next=current_node
                current_node.row_prev=self.tail
                self.tail=current_node
                self.tail.row_next=None

        for cell in lCells:
            cell_node=self.head
            row=cell.row
            for r in range(row):#finds the corresponding node_row by iterating through the row linked list using the row_next pointer.
                cell_node=cell_node.row_next

            cell_column=cell_node.columns.head
            column=cell.col
            for r in range(column):
                cell_column=cell_column.column_next
            cell_column.value=cell.val
        
        # TO BE IMPLEMENTED
        pass


    def appendRow(self): 
        """
        Appends an empty row to the spreadsheet.
        """
        if self.head is None:
            return False
        
        self.nrows+=1
        cell_node=self.head#The method then iterates through the row linked list by starting at the head and following the row_next pointer until it reaches the end of the linked list.
        while cell_node.row_next !=None:
            cell_node=cell_node.row_next
        current_node=node_row(self.ncolumns)#creates a new node_row called current_node
        current_node.listcolumn(self.ncolumns)#objects initialized by calling the listcolumn method.
        cell_node.row_next=current_node
            

        return True
        
        # TO BE IMPLEMENTED
        pass


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if self.head is None:
            return False
        
        self.ncolumns += 1
        current_node = node_column(self.ncolumns)# It creates a new node_column called current_node
        
        row_node = self.head
        while row_node is not None:
            column_node = row_node.columns.tail#For each row, it gets the tail of the columns linked list by accessing the columns.tail attribute of the node_row
            column_node.column_next = current_node
            current_node.column_prev = column_node
            row_node.columns.tail = current_node
            row_node = row_node.row_next
            
        return True


        # TO BE IMPLEMENTED
        pass


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        time_start=time.time()
        if rowIndex < 0 or rowIndex > self.nrows:
            return False

        self.nrows += 1
        current_node = node_row(self.ncolumns)#The method creates a new node_row object with an empty list of columns.
        current_node.listcolumn(self.ncolumns)

        # find node before the insert position
        cell_node = self.head
        for _ in range(rowIndex):
            cell_node = cell_node.row_next

        # insert new node into the list
        current_node.row_next = cell_node.row_next
        if cell_node.row_next is not None:
            cell_node.row_next.row_prev = current_node
        cell_node.row_next = current_node
        current_node.row_prev = cell_node
        
        time_end=time.time()
        print("The time taken to insert row:", time_end-time_start)
        return True

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be before the newly inserted row.  If inserting as first column, specify colIndex to be -1.   If inserting a column after the last one, specify colIndex to be colNum()-1.
        
        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if colIndex < -1 or colIndex > self.ncolumns - 1:
            return False

        self.ncolumns += 1
        new_column = node_column(self.nrows)

        # if inserting as first column
        if colIndex == -1:
            # set column_next of new node to the current head of columns
            new_column.column_next = self.head
            # if head exists, set column_prev of head to new node
            if self.head:
                self.head.column_prev = new_column
            # set new node as head
            self.head = new_column
        # else:
        #     # find node before the insert position
        #     column_node = self.head
        #     for _ in range(colIndex-1):
        #         column_node = column_node.column_next

        #     # insert new node into the list
        #     new_column.column_next = column_node.column_next
        #     if column_node.column_next is not None:
        #         column_node.column_next.column_prev = new_column
        #     column_node.column_next = new_column
        #     new_column.column_prev = column_node

        
        return True

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        time_start=time.time()
        # Check if the row and column indices are within the range of the spreadsheet
        if rowIndex < 0 or rowIndex >= self.nrows or colIndex < 0 or colIndex >= self.ncolumns:
            return False

        # Traverse the rows to get to the row node
        row_node = self.head
        for i in range(rowIndex):
            row_node = row_node.row_next
    
        # Traverse the columns to get to the column node
        col_node = row_node.columns.head
        for i in range(colIndex):
            col_node = col_node.column_next

        # Update the value of the cell
        col_node.value = value
        

        time_end=time.time()
        print("The time taken to update:", time_end-time_start)
        return True

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """

        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return self.nrows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        if self.head is None:
            return 0
        # TO BE IMPLEMENTED
        pass

        # TO BE IMPLEMENTED
        return self.ncolumns



    def find(self, value: float) -> List[Tuple[(int, int)]]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        time_start=time.time()
        result = []
        cell_node = self.head
        while cell_node is not None:
            column_node = cell_node.columns.head
            while column_node is not None:
                if column_node.value == value:
                    result.append((cell_node.row, column_node.column))
                column_node = column_node.column_next
            cell_node = cell_node.row_next
        
        time_end=time.time()
        print("The time taken to find:", time_end-time_start)
        return result
        

        # TO BE IMPLEMENTED
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []



    def entries(self) -> List[Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        result = []
        node = self.head
        while node is not None:
            column_node = node.columns.head
            for i in range(self.ncolumns):
                if column_node is not None and column_node.value is not None:
                    result.append(Cell(node.row, i, column_node.value))
                if column_node is None:
                    break
                column_node = column_node.column_next
            node = node.row_next
        return result
        
        # TO BE IMPLEMENTED
        return []
