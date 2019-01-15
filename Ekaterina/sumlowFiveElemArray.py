import numpy as np;

print ("Генерация массива\n");

arr = np. random. randint (0, 10, 100);


print ("\n\nПечать исходного массива\n");


for i in arr:

  print (i);


print ("\n\nПоиск последних пяти элементов массива меньше пяти и расчёт их суммы\n");


#Перевернули массив для удобства работы
#Задали счётчик
#Задали переменную суммы


arr = np. flip (arr);
count = 0;
sum = 0;


for i in arr:

  if (count == 5):
    break;


  if i > 5:
    continue;


  sum = sum + i;




print ("\n\nРезультат " + str (sum));
