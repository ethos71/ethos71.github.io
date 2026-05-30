---
permalink: /topics/
title: "Browse Posts"
layout: single
author_profile: true
classes: wide
---

Everything I've written, grouped two ways — by category, then by tag. Pick a thread and pull.

## By category

<div class="entries-list">
{% assign cats = site.categories | sort %}
{% for category in cats %}
  {% assign cat_name = category[0] %}
  <h3 id="cat-{{ cat_name | slugify }}" style="margin-bottom:0.3em;">{{ cat_name }} <small style="font-weight:400;color:#6b6259;">({{ category[1].size }})</small></h3>
  <ul style="margin-top:0;">
  {% for post in category[1] %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <small style="color:#6b6259;">· {{ post.date | date: "%b %-d, %Y" }}</small></li>
  {% endfor %}
  </ul>
{% endfor %}
</div>

## By tag

<div class="entries-list">
{% assign tags = site.tags | sort %}
{% for tag in tags %}
  {% assign tag_name = tag[0] %}
  <h3 id="tag-{{ tag_name | slugify }}" style="margin-bottom:0.3em;">{{ tag_name }} <small style="font-weight:400;color:#6b6259;">({{ tag[1].size }})</small></h3>
  <ul style="margin-top:0;">
  {% for post in tag[1] %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <small style="color:#6b6259;">· {{ post.date | date: "%b %-d, %Y" }}</small></li>
  {% endfor %}
  </ul>
{% endfor %}
</div>
