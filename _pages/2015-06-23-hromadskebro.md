---
title: "Громадське телебачення Броварів"
date: 2015-06-23
author: 
  username: "pravoZnaty"
  display_name: "Маєш право знати"
---

<div class="video-posts-grid">
{% assign video_posts = site.posts | where: "tags", "hromadskebro-tv" | sort: "date" | reverse %}
{% for post in video_posts limit:100 %}
  <div class="video-post-card">
    <a href="{{ post.url | relative_url }}">
      {% if post.image %}
        <img src="{{ site.url }}{{ site.baseurl }}/{{ post.coverImage }}" alt="{{ post.title }}" class="video-thumbnail">
      {% endif %}
      <h3>{{ post.title }}</h3>
      <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}</p>
    </a>
  </div>
{% endfor %}
</div>
