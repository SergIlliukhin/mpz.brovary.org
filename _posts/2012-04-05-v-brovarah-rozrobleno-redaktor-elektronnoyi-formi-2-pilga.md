---
title: "У Броварах розроблено редактор електронної форми \"2-пільга\""
date: 2012-04-05
author: 
  username: "sergilliukhin"
  display_name: "Сергій Іллюхін"
categories: 
  - "kolonka-avtora"
tags: 
  - "brovary"
  - "vibir-redaktsiyi"
  - "osbb"
  - "pilgoviki"
  - "sotsialniy-zahist"
---

[![](https://mpz.brovary.org/wp-content/uploads/2012/04/Upravlinnya-Pratsi.jpg "Управління Праці")](https://mpz.brovary.org/wp-content/uploads/2012/04/Upravlinnya-Pratsi.jpg)Нещодавно до мене звернулась бухгалтер нашого ОСББ "Шевченко 4-А", вона перебувала у відчаї: з квітня Управління праці та соціального захисту населення Броварської міської ради відмовляється приймати форму для розрахунку пільг у паперовому вигляді - натомість вимагають подавати звітність у цифровому вигляді, [затвердженому наказом Міністерства](https://zakon2.rada.gov.ua/laws/show/z1172-07 "Наказ Міністерства").

Після ознайомлення із законодавчою базою виявилось, що дійсно, вже давно підприємства та організації зобов'язані подавати форму "2-пільга" у паперовому та електронному вигляді. Формат файлів Міністерством затверджено, але жодного програмного забезпечення, яке могло б бути використано для редагування таких файлів, не розроблено. <!--more-->

Ця проблема виникла не лише в нашому місті. Фактично підприємства та організації поставлені перед вибором: або розробляйте власне програмне забезпечення, або купуйте готові програми сторонніх виробників. В Броварах мені відомо принаймні про 2 розробників, які вже пропонують своє програмне забезпечення для таких потреб: один "править" близько 400грн, інший - 100грн. Можливо, для великого підприємства це дрібниці, але для ОСББ-шників навіть 100грн - це вже проблема!

З технічної точки зору створення такого файлу є дуже нескладним завданням. Міністерство затвердило 2 формати файлів: dbf та txt. При чому на відміну від dbf-файлу, txt-файл може бути без проблем відредаговано у будь-якому текстовому редакторі, але потрібно бути дуже обережним, щоб не зробити помилку.

Оскільки для рідного ОСББ все-рівно необхідно було розробляти програмне забезпечення, я вирішив одразу зробити його загальнодоступним для всіх бажаючих, хто стикнувся з тією самою проблемою по редагуванню електронної версії форми "2-пільга".

Редактор доступний за адресою: **[https://zvit.mpz.brovary.org/](https://zvit.mpz.brovary.org/ "Електронна версія форми \"2-пільга\"")**

Якщо Вас переконуватимуть, що звіти можна подавати виключно у dbf-форматі, не вірте! Ми перевірили: текстові файли чудово завантажуються у систему Міністерства праці та соціальної політики. Просто зазвичай всі це роблять у застарілому dbf-форматі.

> **Важливо!** Інформація, яку Ви вводите на сторінці, жодним чином не зберігається на сервері. Я приділив безпеці даних особливу увагу: дані використовуються для генерації файлу і одразу видаляються.

**P.S.** Це лише перша версія, найближчим часом планується зробити інтерфейс більш зручним та зрозумілим. Прошу використовувати, а найбільшою подякою для команди "Маєш Право Знати" буде Ваш \[Like\] або \[Share\] в соціальних мережах :)
