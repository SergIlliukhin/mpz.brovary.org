---
layout: home
title: Головна
coverImage: /wp-content/uploads/2025/05/mpz3.png
---

# {{ site.title }}

{{ site.description }}

## Сторінки

{% include tagged-pages.html tag="homepage" %}

## Публікації

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url | relative_url }}) - {{ post.date | date: "%d.%m.%Y" }}
{% endfor %}