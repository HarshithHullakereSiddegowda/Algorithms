from spreadsheet.baseSpreadsheet import BaseSpreadsheet
from spreadsheet.cell import Cell

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

from typing import List, Tuple
import sys

from bisect import bisect_left



class CSRSpreadsheet(BaseSpreadsheet):

    def __init__(self):
        self.colA=[]
        self.valA=[]
        self.sumA=[0]
        self.spreadsheet=[[0]]
        self.nrows=0
        self.ncolumns=0
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
        
        self.spreadsheet=[[0]*self.ncolumns for _ in range(self.nrows)]
        
        for cell in lCells:
            if cell.val is not None:
                self.spreadsheet[cell.row][cell.col]=float(cell.val)

        cum_sum=0
        for i, row in enumerate(self.spreadsheet):
            row_sum=0
            for j, val in enumerate(row):
                if val!=0:
                    self.colA.append(j)
                    self.valA.append(val)
                    row_sum+=val
            cum_sum+=row_sum
            self.sumA.append(cum_sum)
        print(self.colA)
        print(self.valA)


        pass


    def appendRow(self):
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if not self.colA or not self.valA or not self.sumA:
            return False  
        
        self.nrows =self.nrows+1
        self.spreadsheet.append([0 for j in range(self.ncolumns)])

        
        self.sumA.append(self.sumA[-1])

        return True
        # TO BE IMPLEMENTED
        pass


    def appendCol(self):
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        if not self.colA or not self.valA or not self.sumA:
            return False
        
        num_rows=len(self.sumA)-1

        for row in range(len(self.spreadsheet)):
            self.spreadsheet[row].append(0)
        self.ncolumns +=1
        return True


        # Update sumA to include a new element with the same value as the previous last element
        # last_sum = self.sumA[-1]
        # self.sumA.append(last_sum)
        return True

        # TO BE IMPLEMENTED
        pass


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        if rowIndex<0 or rowIndex>=len(self.sumA):
            return False
        
        self.spreadsheet.insert(rowIndex, [0]*self.ncolumns)
        self.nrows+=1

        if rowIndex>0:#If rowIndex is greater than 0, the code sets prev_sum to the sum of the row immediately preceding the new row. It then inserts prev_sum
            prev_sum=self.sumA[rowIndex-1]
            self.sumA.insert(rowIndex, prev_sum)
        else:
            self.sumA.insert(rowIndex,0)

        # for i in range(rowIndex+1, len(self.sumA)):
        #     row_sum = sum(self.spreadsheet[i-1])
        #     self.sumA[i] = self.sumA[i-1] + row_sum


        return True
        
    
        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """

        # REPLACE WITH APPROPRIATE RETURN VALUE
        if colIndex<0 or colIndex>=self.ncolumns:
            return False
        
        for j in range(self.nrows):
            self.spreadsheet[j].insert(colIndex, 0)
        self.ncolumns+=1

        for i in range(len(self.colA)):#The code iterates over each element in colA and increments any element that is greater than or equal to colIndex by 1.
            if self.colA[i]>=colIndex:
                self.colA[i]+=1

        # for i in range(len(self.valA)):
        #     if self.colA[i]>=colIndex:
        #         self.colA[i]+=1

        print(self.sumA)

        return True

    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        if rowIndex<0 or colIndex<0 or rowIndex >= int(len(self.sumA)-1) or colIndex >= int(self.ncolumns):
            return False
        
         
        self.spreadsheet[rowIndex][colIndex]=float(value)

        #It then checks if the column index already exists in the "colA" list which stores the column indices that have values.
        try:
            idx = self.colA.index(colIndex)
            self.valA[idx] = value
        except ValueError:
            for i in range(len(self.colA)):
                if self.colA[i] > colIndex:
                    self.colA.insert(i, colIndex)
                    self.valA.insert(i, value)
                    break
            else:
                self.colA.append(colIndex)
                self.valA.append(value)
        

        cumulative_sum = 0
        for i, row in enumerate(self.spreadsheet):
            row_sum = sum(row)
            cumulative_sum += row_sum
            self.sumA[i+1] = round(cumulative_sum,2)

        return True
       
        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return len(self.sumA)-1


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        # TO BE IMPLEMENTED
        return self.ncolumns



 
    def find(self, value: float) -> List[Tuple[int, int]]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        # cells = []
        # for i, val in enumerate(self.valA):
        #     if val == value:
        #         row = 0
        #         while self.sumA[row] <= i:
        #             row += 1
        #         row -=1
        #         col = self.colA[i]
        #         cells.append((row, col))
        # return cells
        
        results=[]
        for i, row in enumerate(self.spreadsheet):
            for j, val in enumerate(row):
                if val==value:
                   results.append((i,j))
        
        return results
        
        # TO BE IMPLEMENTED

        # REPLACE WITH APPROPRIATE RETURN VALUE
        return []

    def entries(self) -> List[Cell]:
        """
        return a list of cells that have values (i.e., all non None cells).
        """
        results=[]
        for i, row in  enumerate(self.spreadsheet):
            for j,val in  enumerate(row):
                if val!=0:
                    cell=Cell(i, j, val)
                    results.append(cell)

        return results

        



