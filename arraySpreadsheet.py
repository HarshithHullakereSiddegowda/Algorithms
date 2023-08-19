from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet

from typing import List, Tuple
import sys

import time
# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):
    

    def __init__(self):
        self._nrows= 0
        self._ncolumns=0
        # TO BE IMPLEMENTED
        self._cells=[[None]]


    def buildSpreadsheet(self, lCells: List[Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        #Construct the 2D data structure to store node
        max_row, max_column=0,0
        for cell in lCells:
            max_row=max(max_row, cell.row)
            max_column=max(max_column, cell.col)
            
        self._nrows=max_row+1
        self._ncolumns=max_column+1
        self._cells=[[None] * self._ncolumns for _ in range(self._nrows)]
        for cell in lCells:
            if cell.val is not None:
                self._cells[cell.row][cell.col]=float(cell.val)    
        

    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if self._nrows>sys.maxsize:
            return False
        
        else:
            self._nrows =self._nrows+1
            self._cells.append([None for j in range(self._ncolumns)])
        
            return True
        # # REPLACE WITH APPROPRIATE RETURN VALUE
        # return True

    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if self._ncolumns>sys.maxsize:
            return False
        
        for i in range(self._nrows):
            self._cells[i].append(None)
        self._ncolumns += 1
        
        return True
        
        #pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        #return True

    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        #time_start=time.time()
        if rowIndex < 0 or rowIndex > self._nrows:
            return False
        
        self._cells.insert(rowIndex, [None]*self._ncolumns)
        self._nrows+=1

        #time_end=time.time()
        #print("Time taken to insert row", time_end-time_start)
        return True
    
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE
        


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.
    
        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        #time_start=time.time()
        if colIndex<0 or colIndex>=self._ncolumns:
            return False
        
        for row in range(self._nrows):
            self._cells[row].insert(colIndex, None)
                    
        self._ncolumns+=1
        #time_end=time.time()
        #print("Time taken to insert column", time_end-time_start)
        return True
        
        pass

        # REPLACE WITH APPROPRIATE RETURN VALUE


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        #time_start=time.time()
        if rowIndex<0 or colIndex<0 or rowIndex>=self._nrows or colIndex>=self._ncolumns:
            
            return False
        
        
        self._cells[rowIndex][colIndex]=float(value)
        #time_end=time.time()
        #print("Time taken to update", time_end-time_start)
        return True
        
        # # TO BE IMPLEMENTED
        pass

    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        pass
        return self._nrows


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        pass

        return self._ncolumns



    def find(self, value: float) -> List[Tuple[int, int]]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        #time_start=time.time()
        search_cell=[]
        for i in range(self._nrows):
           for j in range(self._ncolumns):
                if self._cells[i][j]==float(value):
                    search_cell.append((i,j))
        #time_end=time.time()
        #print("Time taken to find ", time_end-time_start)
        
        return search_cell
       
        # pass

        # # REPLACE WITH APPROPRIATE RETURN VALUE
        # return []

    def entries(self) ->List[Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        have_val=[]
        for row in range(self._nrows):
            for column in range(self._ncolumns):
                if self._cells[row][column] is not None:
                    cell=Cell(row, column, self._cells[row][column])
                    have_val.append(cell)

        return have_val

        
        # pass

 