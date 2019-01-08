import numpy as np;


arr = np. random. randint (0, 100, 10);


print ("Печать исходного массива");


for i in arr:
  print (i);


print ("Поиск индекса максимального элемента");


indMax = np. argmax (arr);


print ("Индекс максимального элемента: " + str (indMax));


print ("Домножение последних пяти положительных элементов массива на индекс максимального элемента");


#перевернули массив для удобства работы
 #Задали счётчик для поиска пяти положительных элементов 
arr = np. flip (arr);
j = 0;


for i in np. arange ( len (arr)):

  if j >= 5:
    break;


  if arr [i] > 0:
    arr [i] = arr [i] * indMax;
    j += 1;


#Переворачиваем массив обратно, в исходное положение
arr = np. flip (arr);


print ("Печать результирующего массива");


for i in arr:
  print (i);
