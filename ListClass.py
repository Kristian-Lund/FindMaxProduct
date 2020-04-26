from Functions import color
from colorama import init, Fore
init()
PrintColors = 1
InitReturnProduct = float('-inf')

# A class of the spreadsheet list. Constructed by the input string and the dim of the window (4x4 according to the task)

class ListClass:

    def __init__(self,SpreadSheetString, WindowDim):
        #Constructor,spredsheet string and window dim as parameters
        self.List = []
        self.Rows = 0
        self.Columns = 0
        self.WindowDim = WindowDim
        self.PrintableList = SpreadSheetString


        NumberOfColumnsTemp = []
        SpreadSheetList = SpreadSheetString.split('\n')
        self.Rows = len(SpreadSheetList)
        for i in range(len(SpreadSheetList)):
            #Appending line for line in the List
            NumberOfColumnsTemp.append(len(SpreadSheetList[i].split(' ')))
            self.List.append(list(map(int,SpreadSheetList[i].split(' '))))
        self.Rows = len(NumberOfColumnsTemp)

        #Validate that all Columns counted are equal in each row
        if(all(Columns == NumberOfColumnsTemp[0] for Columns in NumberOfColumnsTemp)):
            self.Columns = NumberOfColumnsTemp[0]
        else:
            self.Columns = -1
            print('The list doesnt have same same number of columns in each row')

    def __str__(self):
        #Trigger a run of the calculation, and "stringyfies" the results
        if self.Columns>self.WindowDim and self.Rows>self.WindowDim:
            CalculationMaxima = self.getWindowCalcultions()
            PrintableList = self.__makePrintableList(CalculationMaxima)
            PrintableResults = self.__stringifyDescriptionOfCalculcationMaxima((CalculationMaxima))

            ReturnString = (PrintableList + '\n\n' + 'Columns' + u'\u2192' + ':\t' + str(self.Columns) + '\nRows'+ u'\u2193' + ':\t\t' + str(self.Rows)
            + PrintableResults)
            return ReturnString
        else:
            return 'The list in invalid'

#-------Calculation Control Actions---------

    def getWindowCalcultions(self):
        #Run windowing in 4 cycles, horizontal, vertical, diagonal (\), and reverse diagonal(/)
        HorizontalCalculationWinner = self.__runHorizontalWindow()
        VerticalCalculationWinner = self.__runVerticalWindow()
        DiagonalCalculationWinner = self.__runDiagonalWindow()
        ReverseDiagonalCalculationWinner = self.__runReverseDiagonalWindow()
        CalculationWinner = self.__findCalculationWinner((HorizontalCalculationWinner, VerticalCalculationWinner ,DiagonalCalculationWinner ,ReverseDiagonalCalculationWinner ))
        return  CalculationWinner

    def __findCalculationWinner(self, CalculationWinners):
        #Finding the Winner score of the 4 windows (Target is maxima,defined in self.__checkProductAndUpdate(), change the definition of winner there...)
        GrandCalculationWinner = CalculationWinners[0]
        for CalculationWinner in CalculationWinners:
            GrandCalculationWinner = self.__checkProductAndUpdate(CalculationWinner,GrandCalculationWinner)
        return GrandCalculationWinner

#-------Window Actions---------

    def __runHorizontalWindow(self):
        ReturnProduct = InitReturnProduct
        ReturnFactors = []
        ReturnCoordinates = []
        for RowNo in range(self.Rows):
            for ColumnNo in range(self.Columns-self.WindowDim+1):
                Factors, Coordinates = self.__getHorizontalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                ReturnProduct, ReturnFactors, ReturnCoordinates = self.__checkProductAndUpdate((Product, Factors, Coordinates), (ReturnProduct, ReturnFactors, ReturnCoordinates))
        return ReturnProduct, ReturnFactors, ReturnCoordinates

    def __runVerticalWindow(self):
        ReturnProduct = InitReturnProduct
        ReturnFactors = []
        ReturnCoordinates = []
        for RowNo in range(self.Rows-self.WindowDim+1):
            for ColumnNo in range(self.Columns):
                Factors, Coordinates = self.__getVerticalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                ReturnProduct, ReturnFactors, ReturnCoordinates = self.__checkProductAndUpdate((Product, Factors, Coordinates), (ReturnProduct, ReturnFactors, ReturnCoordinates))
        return ReturnProduct ,  ReturnFactors, ReturnCoordinates

    def __runDiagonalWindow(self):
        ReturnProduct = InitReturnProduct
        ReturnFactors = []
        ReturnCoordinates = []
        for RowNo in range(self.Rows-self.WindowDim+1):
            for ColumnNo in range(self.Columns-self.WindowDim+1):
                Factors, Coordinates = self.__getDiagonalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                ReturnProduct, ReturnFactors, ReturnCoordinates = self.__checkProductAndUpdate((Product, Factors, Coordinates), (ReturnProduct, ReturnFactors, ReturnCoordinates))
        return ReturnProduct,  ReturnFactors, ReturnCoordinates

    def __runReverseDiagonalWindow(self):
        ReturnProduct = InitReturnProduct
        ReturnFactors = []
        ReturnCoordinates = []
        for RowNo in range(self.Rows-self.WindowDim+1):
            for ColumnNo in range(self.Columns-self.WindowDim+1):
                Factors, Coordinates = self.__getReverseDiagonalSubList(RowNo,ColumnNo)
                Product = self.__multiplyFactors(Factors)
                ReturnProduct, ReturnFactors, ReturnCoordinates = self.__checkProductAndUpdate((Product, Factors, Coordinates), (ReturnProduct, ReturnFactors, ReturnCoordinates))
        return ReturnProduct,  ReturnFactors, ReturnCoordinates

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

#-------Calculation Actions---------

    def __checkProductAndUpdate(self,NewValues, PreviousReturnValues):
        #Check if the new product has a higher value than the already found maxima, if so update MaxProduct, MaxFactors and MaxCoordinates. The return values are related to the max found
        #Expecting NewVal/ReturnVal is in the format (product, factors[], Coordinates[])
        if(NewValues[0]>PreviousReturnValues[0]):
            ReturnProduct = NewValues[0]
            ReturnFactors = NewValues[1]
            ReturnCoordinates = NewValues[2]
            return ReturnProduct, ReturnFactors, ReturnCoordinates
        else: return PreviousReturnValues

    def __multiplyFactors(self,Factors):
            product = 1
            for i in range(len(Factors)):
                product = product*Factors[i]
            return product

#-------String Actions---------

    def __stringifyDescriptionOfCalculcationMaxima(self, CalculationMaxima):
        #Making a string with the Product, calculation and adding the Coordinates of the factors
        ResultString = '\n\nTargetProduct:\t' + str(CalculationMaxima[0]) + '\t('
        for i in range(len(CalculationMaxima[1])):
            #Making a string of the calculation
            if(i==0):
                ResultString = ResultString + str(CalculationMaxima[1][i])
            else:
                ResultString = ResultString + '*' + str(CalculationMaxima[1][i])
        ResultString = ResultString + ')\n\nLocated :\t' + str(CalculationMaxima[2])
        return ResultString

    def __makePrintableList(self,CalculationMaxima):
        returnSpreadSheetString = ''
        if(PrintColors):
            #Rewriting the spreadheet string number by number and adding colors if they are a factor or not in the max product
            for Row in range(self.Rows):
                for Column in range(self.Columns):
                    if (self.__checkIfCoordinatesAreInCalculation(Row,Column,CalculationMaxima)):
                        #Putting colors red to factors in Maxima
                        if (PrintColors):returnSpreadSheetString = returnSpreadSheetString + Fore.RED +str(self.List[Row][Column]).zfill(2) +Fore.RESET
                            #<For not using colorama>returnSpreadSheetString = returnSpreadSheetString + color.RED +str(self.List[Row][Column]).zfill(2) + color.END
                        else:returnSpreadSheetString = returnSpreadSheetString + str(self.List[Row][Column]).zfill(2)
                    else:
                        #Putting colors green to factors not in Maxima
                        if(PrintColors): returnSpreadSheetString = returnSpreadSheetString + Fore.GREEN +str(self.List[Row][Column]).zfill(2) +Fore.RESET
                            #<For not using colorama>returnSpreadSheetString = returnSpreadSheetString + color.GREEN +str(self.List[Row][Column]).zfill(2) + color.END
                        else: returnSpreadSheetString = returnSpreadSheetString + str(self.List[Row][Column]).zfill(2)
                    returnSpreadSheetString = returnSpreadSheetString + ' '
                returnSpreadSheetString = returnSpreadSheetString + '\n'
            return returnSpreadSheetString
        else:
            return self.PrintableList

    def __checkIfCoordinatesAreInCalculation(self,RowNo, ColumnNo, CalculationMaxima):
        #Helper for coloring the factors in the product
        for i in range(len(CalculationMaxima[2])):
            if(CalculationMaxima[2][i][0] == RowNo and CalculationMaxima[2][i][1] == ColumnNo):
                return True
        return False