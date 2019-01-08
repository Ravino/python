import numpy as np;

arrFile = open ("./arrayStar.txt", "w+");
arr = np. random. randint (0, 100, 100);


print ("Печать исходного массива");


for i in arr:
  print (i);


print ("Запись исходного массива в файл");


temp = "";
for i in arr:
  temp = temp + str (i) + ",";


temp = temp [: len (temp) - 1];
arrFile. write (temp);
arrFile. close ();


arr = None;
arrFile = None;


def createArray ():

  arr = np. loadtxt ("./arrayStar.txt", delimiter=",");

  return arr;


def searchIndexMax ():

  print ("Поиск индекса максимального элемента");


  arr = createArray ();


  indMax = np. argmax (arr);


  print ("Индекс максимального элемента: " + str (indMax));


  return indMax;


def starElemsLow (arr):

  print ("Домножение последних пяти положительных элементов массива на индекс максимального элемента");


#перевернули массив для удобства работы
 #Задали счётчик для поиска пяти положительных элементов 
  def reverseArray (arr):
    arr = np. flip (arr);
    j = 0;


    indMax = searchIndexMax ();


    for i in np. arange ( len (arr)):

      if j >= 5:
        break;


      if arr [i] > 0:
        arr [i] = arr [i] * indMax;
        j += 1;


#Переворачиваем массив обратно, в исходное положение
    arr = np. flip (arr);


    print ("Запись данных из подфункции в файл");


    arrFile = open ("./starArray.txt", "w+");


    temp = "";
    for i in arr:
      temp = temp + str (i) + ",";


    temp = temp [: len (temp) - 1];
    arrFile. write (temp);
    arrFile. close ();


    arr = None;
    arrFile = None;


  print ("Вызов подфункции");


  reverseArray (arr);


  print ("Функция считывает данные из файла с результатом и возвращает");


  arr = np. loadtxt ("./starArray.txt", delimiter=",");


  return arr;


print ("Вызов функции");


arr = createArray ();


arr = starElemsLow (arr);


print ("Печать результирующего массива");


for i in arr:
  print (i);
