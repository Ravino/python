import numpy as np;print ("Введите чётное число отрицательных и положительных значений. Для завершения ввода нажмите 0");


inpList= [];


while (True):

  i = int (input ());

  if (i == 0):
    print ("Вы завершили ввод");
    break;


  print ("Вы ввели число: " + str (i));
  inpList. append (i);


arr = np. array (inpList);


arrMinus = [];
arrPlus = [];
arrGen = [];


global countGenExternal;
countGenExternal = 0;


def external ():

  print ("Вызов функции external");


  try:
    external. count += 1;
    countGenExternal += 1;


  except AttributeError:
    external. count = 1;
    countGenExternal = 1;


  print ("Печать исходного массива");


  for i in arr:
    print (i);


  print ("Разложение массива. Левая-правая сортировка.");


  for i in arr:

    if (i < 0):
      arrMinus. append (i);
      continue;

    arrPlus. append (i);


  print ("Создание чередования элементов массива");


  for i in np. arange (int (len (arr) / 2)):

    arrGen. append (arrMinus [i]);
    arrGen. append (arrPlus [i]);


  print ("Печать конечного массива");


  for i in arrGen:
    print (i);


  print ("Количество вызовов функции по значению атрибута функции: " + str (external. count));
  print ("Количество вызовов функций по количеству глобальной переменной: " + str (countGenExternal));




global countGenInternal;
countGenInternal = 0;


def internal (arr, arrMinus, arrPlus, arrGen):

  print ("Вызов функции internal");


  try:
    internal. count +=1;
    countGen += 1;


  except AttributeError:
    internal. count = 1;
    countGenInternal = 1;


  print ("Печать исходного массива");


  for i in arr:
    print (i);


  print ("Разложение массива. Левая-правая сортировка.");


  for i in arr:

    if (i < 0):
      arrMinus. append (i);
      continue;

    arrPlus. append (i);


  print ("Создание чередования элементов массива");


  for i in np. arange (int (len (arr) / 2)):

    arrGen. append (arrMinus [i]);
    arrGen. append (arrPlus [i]);


  print ("Печать конечного массива");


  for i in arrGen:
    print (i);


  print ("Количество вызовов функции по значению атрибута функции: " + str (internal. count));
  print ("Количество вызовов функций по количеству глобальной переменной: " + str (countGenInternal));




print ("Вызывается функция external");


external ();


print ("Вызывается функция internal");


internal (arr, arrMinus, arrPlus, arrGen);
