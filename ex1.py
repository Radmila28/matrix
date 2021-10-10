#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # Добавляем модуль math
import numpy # Добавляем модуль numpy
import matplotlib.pyplot as mpp # Импортируем модуль pyplot из matplotlib и обозначаем его как mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': # Проверяем на запуск кода как программы
    arguments = numpy.arange(0, 200, 0.1) # Задаем массив из элементов от 0 до 200 с шагом 0.1
    mpp.plot( # Открываем функцию, которая описывает график
        arguments, # Передаем функции список элементов из массива, это значения по X
        [math.sin(a) * math.sin(a/20.0) for a in arguments] # Задаем значение Y для каждого элемента массива
    )
    mpp.show() # Выводим графика