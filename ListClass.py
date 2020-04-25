
#from termcolor import colored

from Functions import color

# A class of the spreadsheet list. Constructed by the input string and the dim of the window (4x4 according to the task)

class ListClass:

    def __init__(self,SpreadSheetString, WindowDim):
        #Constructor,spredsheet strign and window dim as parameters
        self.List = []
        self.Rows = 0
        self.Columns = 0
        self.WindowDim = WindowDim
        self.PrintableList = SpreadSheetString#colored(SpreadSheetString, 'red')

        NumberOfColumnsTemp = []
        SpreadSheetList = SpreadSheetString.split('\n')
        self.Rows = len(SpreadSheetList)
        for i in range(len(SpreadSheetList)):
            #Asserting line for line in the final lis
            NumberOfColumnsTemp.append(len(SpreadSheetList[i].split(' ')))
            self.List.append(list(map(int,SpreadSheetList[i].split(' '))))
        self.Rows = len(NumberOfColumnsTemp)

        #Validate that all Columns counted are equal
        if(all(Columns == NumberOfColumnsTemp[0] for Columns in NumberOfColumnsTemp)):
            self.Columns = NumberOfColumnsTemp[0]
        else:
            self.Columns = -1
            print('The list doesnt have same same number of columns in each row')

    def __str__(self):
        if self.Columns>self.WindowDim and self.Rows>self.WindowDim:
            CalculationMaxima = self.runWindowCalcultions()
            PrintableResults = self.__stringifyCalculcationMaxima((CalculationMaxima))
            PrintableList = self.__makePrintableList(CalculationMaxima)

            ReturnString = (PrintableList + '\n\n' + 'Columns' + u'\u2192' + ':\t' + str(self.Columns) + '\nRows'+ u'\u2193' + ':\t\t' + str(self.Rows)
            + PrintableResults)
            return ReturnString
        else:
            return 'The list in invalid'


    def runWindowCalcultions(self):
        HorizontalCalculations = self.__runHorizontalWindow()
        VerticalCalculations = self.__runVerticalWindow()
        DiagonalCalculations = self.__runDiagonalWindow()
        ReverseDiagonalCalculations = self.__runReverseDiagonalWindow()
        return  self.__findCalculationMaxima(HorizontalCalculations, VerticalCalculations ,DiagonalCalculations ,ReverseDiagonalCalculations )


    def __findCalculationMaxima(selfself, HorizontalCalculations, VerticalCalculations, DiagonalCalculations, ReverseDiagonalCalculations):
        MaxList = [HorizontalCalculations[0], VerticalCalculations[0], DiagonalCalculations[0], ReverseDiagonalCalculations[0]]
        MaxIndex = MaxList.index(max(MaxList))
        if(MaxIndex == 0):
            return 'horizontally', HorizontalCalculations
        elif(MaxIndex == 1):
            return 'vertically', VerticalCalculations
        elif(MaxIndex == 2):
            return 'diagonally', DiagonalCalculations
        elif(MaxIndex == 3):
            return 'reverse diagonally', ReverseDiagonalCalculations
        else:
            assert ("error")
            return ''

    def __stringifyCalculcationMaxima(self, CalculationMaxima):
        resultstring = '\n\nMaxProduct:\t' + str(CalculationMaxima[1][0]) + '\t('
        for i in range(len(CalculationMaxima[1][1])):
            if(i==0):
                resultstring = resultstring + str(CalculationMaxima[1][1][i])
            else:
                resultstring = resultstring + '*' + str(CalculationMaxima[1][1][i])
        return resultstring + ')\n\nLocated ' +CalculationMaxima[0 ]+ ':\t' + str(CalculationMaxima[1][2])

    def __makePrintableList(self,CalculationMaxima):
        returnSpreadSheetString = ''
        for Row in range(self.Rows):
            for Column in range(self.Columns):
                if (self.__checkIfCoordinatesAreInCalculation(Row,Column,CalculationMaxima)):
                    returnSpreadSheetString = returnSpreadSheetString + color.RED +str(self.List[Row][Column]).zfill(2) + color.END#colored(str(self.List[Row][Column]).zfill(2), 'red')
                    #returnSpreadSheetString = returnSpreadSheetString + str(self.List[Row][Column]).zfill(2)
                else:
                    returnSpreadSheetString = returnSpreadSheetString + color.GREEN +str(self.List[Row][Column]).zfill(2) + color.END#colored(str(self.List[Row][Column]).zfill(2), 'green')
                    #returnSpreadSheetString = returnSpreadSheetString + str(self.List[Row][Column]).zfill(2)
                returnSpreadSheetString = returnSpreadSheetString + ' '
            returnSpreadSheetString = returnSpreadSheetString + '\n'
        return returnSpreadSheetString

    def __checkIfCoordinatesAreInCalculation(self,RowNo, ColumnNo, CalculationMaxima):
        for i in range(len(CalculationMaxima[1][2])):
            if(CalculationMaxima[1][2][i][0] == RowNo and CalculationMaxima[1][2][i][1] == ColumnNo):
                return True
        return False

    def __runHorizontalWindow(self):
        Max = 0
        for RowNo in range(self.Rows):
            for ColumnNo in range(self.Columns-self.WindowDim+1):
                Factors, Coordinates = self.__getHorizontalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                if(Product>Max):
                    Max = Product
                    MaxFactors = Factors
                    MaxCoordinates = Coordinates
        return Max,  MaxFactors, MaxCoordinates

    def __runVerticalWindow(self):
        Max = 0
        for RowNo in range(self.Rows-self.WindowDim+1):
            for ColumnNo in range(self.Columns):
                Factors, Coordinates = self.__getVerticalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                if(Product>Max):
                    Max = Product
                    MaxFactors = Factors
                    MaxCoordinates = Coordinates
        return Max,  MaxFactors, MaxCoordinates

    def __runDiagonalWindow(self):
        Max = 0
        for RowNo in range(self.Rows-self.WindowDim+1):
            for ColumnNo in range(self.Columns-self.WindowDim+1):
                Factors, Coordinates = self.__getDiagonalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                if(Product>Max):
                    Max = Product
                    MaxFactors = Factors
                    MaxCoordinates = Coordinates
        return Max,  MaxFactors, MaxCoordinates

    def __runReverseDiagonalWindow(self):
        Max = 0
        for RowNo in range(self.Rows-self.WindowDim+1):
            for ColumnNo in range(self.Columns-self.WindowDim+1):
                Factors, Coordinates = self.__getReverseDiagonalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                if(Product>Max):
                    Max = Product
                    MaxFactors = Factors
                    MaxCoordinates = Coordinates
        return Max,  MaxFactors, MaxCoordinates


    def __multiplyFactors(self,Factors):
        product = 1
        for i in range(len(Factors)):
            product = product*Factors[i]
        return product

    def __getHorizontalSubList(self,RowNo, ColumnNo):
        Factors = []
        Coordinates = []
        for i in range(self.WindowDim):
            Coordinates.append([RowNo, ColumnNo+i])
            Factors.append(self.List[RowNo][ColumnNo+i])
        return Factors , Coordinates

    def __getVerticalSubList(self,RowNo,ColumnNo):
        Factors = []
        Coordinates = []
        for i in range(self.WindowDim):
            Coordinates.append([ RowNo+i, ColumnNo])
            Factors.append(self.List[RowNo+i][ColumnNo])
        return Factors, Coordinates

    def __getDiagonalSubList(self,RowNo,ColumnNo):
        Factors = []
        Coordinates = []
        for i in range(self.WindowDim):
            Coordinates.append([RowNo+i, ColumnNo+i])
            Factors.append(self.List[RowNo+i][ColumnNo+i])
        return Factors, Coordinates

    def __getReverseDiagonalSubList(self,RowNo,ColumnNo):
        Factors = []
        Coordinates = []
        for i in range(self.WindowDim):
            Coordinates.append([RowNo+i, ColumnNo+self.WindowDim-1-i])
            Factors.append(self.List[RowNo+i][ColumnNo+self.WindowDim-1-i])
        return Factors, Coordinates


