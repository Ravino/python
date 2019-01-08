import numpy as np;

matrix = np. loadtxt ("dataMatrix.txt", delimiter=",");
newMatrix = open ("dataMatrix.txt", "w+");


for i in np. arange ( len (matrix) ):

  print ("вывод строки " + str (i));


  temp = "";

  for j in np. arange ( len (matrix [i])):
    temp = temp + str (matrix [i] [j]) + ",";

  temp = temp [: len (temp)];
  print (temp);


  print ("Замена максимального элемента в строке " + str (i) + " на число 100");
  matrix [i] [np. argmax (matrix [i])] = 100;


  print ("Печать изменённых строк матрицы");

  temp = "";
  for k in np. arange ( len (matrix [i])):
    temp = temp + str (matrix [i] [k]) + ",";

  temp = temp [: len (temp) - 1];
  temp = temp + "\n";
  print (temp);


  print ("Запись строки в файл");
  newMatrix. write (temp);


newMatrix. close ();

