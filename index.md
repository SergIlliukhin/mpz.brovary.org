---
layout: home
title: Головна
coverImage: /wp-content/uploads/2025/05/mpz3.png
---

# {{ site.title }}

{{ site.description }}

## [Головне]({{ "/tag/vibir-redaktsiyi/" | relative_url }})
{% include tagged-posts.html tag="vibir-redaktsiyi" limit=6 countOfCovers=3 %} 

## [Сторінки і проекти]({{ "/tag/homepage/" | relative_url }})
{% include tagged-pages.html tag="homepage" limit=6 countOfCovers=3 %}

## [Аналітика]({{ "/action/rozsliduvannya/" | relative_url }})
{% include categorized-posts.html category="rozsliduvannya" limit=6 countOfCovers=3 %}

## [Репортажі]({{ "/action/aktsiyi-zahodi/" | relative_url }})
{% include categorized-posts.html category="aktsiyi-zahodi" limit=6 countOfCovers=3 %}

## [Інтерв'ю]({{ "/action/interview/" | relative_url }})
{% include categorized-posts.html category="interview" limit=6 countOfCovers=3 %}

## [Блоги]({{ "/action/kolonka-avtora/" | relative_url }})
{% include categorized-posts.html category="kolonka-avtora" limit=6 countOfCovers=3 %}

## [Місто]({{ "/action/brovary/" | relative_url }})
{% include categorized-posts.html category="brovary" limit=6 countOfCovers=3 %}

## [Громада]({{ "/action/hromada/" | relative_url }})
{% include categorized-posts.html category="hromada" limit=6 countOfCovers=3 %}

## [Влада]({{ "/action/vlada/" | relative_url }})
{% include categorized-posts.html category="vlada" limit=6 countOfCovers=3 %}