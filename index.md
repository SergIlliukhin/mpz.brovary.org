---
layout: home
title: Головна
coverImage: /wp-content/uploads/2025/05/mpz3.png
---

# {{ site.title }}

{{ site.description }}

{% include tagged-pages.html tag="homepage" %}

## Головне
{% include tagged-posts.html tag="vibir-redaktsiyi" limit=6 %} 

## Місто
{% include categorized-posts.html category="brovary" limit=6 %}

## Громада
{% include categorized-posts.html category="hromada" limit=6 %}

## Влада
{% include categorized-posts.html category="vlada" limit=6 %}

## Блоги
{% include categorized-posts.html category="kolonka-avtora" limit=6 %}