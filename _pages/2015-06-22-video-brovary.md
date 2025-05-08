---
title: "Відео Бровари"
date: 2015-06-22
author: 
  username: "pravoZnaty"
  display_name: "Маєш право знати"
---

<div class="video-posts-grid">
{% assign video_posts = site.posts | where: "tags", "videoreportazh" | sort: "date" | reverse %}
{% for post in video_posts limit:100 %}
  <div class="video-post-card">
    <a href="{{ post.url | relative_url }}">
      {% if post.coverImage %}
        <img src="{{ post.coverImage | relative_url}}" alt="{{ post.title | escape }}" class="video-thumbnail">
      {% endif %}
      <h3>{{ post.title | escape }}</h3>
      <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}</p>
    </a>
  </div>
{% endfor %}
</div>

<style>
.video-posts-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin: 20px 0;
}

.video-post-card {
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s;
}

.video-post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.video-post-card a {
  text-decoration: none;
  color: inherit;
}

.video-thumbnail {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.video-post-card h3 {
  padding: 15px;
  margin: 0;
  font-size: 1.1em;
  line-height: 1.4;
}

.post-date {
  padding: 0 15px 15px;
  margin: 0;
  color: #666;
  font-size: 0.9em;
}

@media (max-width: 768px) {
  .video-posts-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .video-posts-grid {
    grid-template-columns: 1fr;
  }
}
</style>
