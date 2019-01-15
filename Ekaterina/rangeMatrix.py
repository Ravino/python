import numpy as np;



def printMatrix (matrix):

  for i in np. arange (0, len (matrix)):

    print ("\nСтрока " + str (i + 1) + "\n");


    strElemsColumn = "";


    for j in matrix [i]:

      strElemsColumn = strElemsColumn + " " + str (j);


    print (strElemsColumn + "\n");


print ("Введите диапазон\n");


print ("\n\nОт\n");
aRange = int (input ());


print ("\n\nДо\n");
bRange = int (input ());


#Создаём диапазон для поиска вхождений


rangeForElem = np. arange (aRange, bRange + 1);


print ("\n\nЗадайте размерность матрицы\n\n");


print ("\n\nЧисло строк\n");
rows = int (input ());


print ("\n\nЧисло столбцов\n");
columns = int (input ());


#Создаём матрицу

matrix = np. empty ((rows, columns));


print ("\n\nЗаполните матрицу\n\n");


for i in np. arange (0, len (matrix)):

  print ("Строка " + str (i + 1));


  for j in np. arange (0, len (matrix [i])):

    print ("Столбец " + str (j + 1));


    matrix [i] [j] = int (input ());


print ("\n\nПечать исходной матрицы\n\n");


printMatrix (matrix);

#Создали массив для положительных элементов матрицы

arrPositive = np. array (());


print ("\n\nПодсчёт всех положительных элементов матрицы\n\n");


for i in np. arange (0, len (matrix)):

  for j in np. arange (0, len (matrix [i])):

    if (matrix [i] [j] >= 0):

      arrPositive = np. append (arrPositive, matrix [i] [j]);


print ("\n\n Вычисление среднего от общего числа положительных элементов матрицы\n\n");


arrElemMiddle = np. sum (arrPositive) / len (arrPositive);


print ("\n\nПроверка вхождения элемента в диапазон и его замена на среднее значение из общего числа положительных элементов\n\n");


for i in np. arange (0, len (matrix)):

  for j in np. arange (0, len (matrix [i])):

    if (matrix [i] [j] in rangeForElem):

      matrix [i] [j] = arrElemMiddle;


print ("\n\nПечать результирующей матрицы\n\n");


printMatrix (matrix);
