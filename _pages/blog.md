---
permalink: /blog/
title: "Blog"
layout: single
author_profile: true
classes: wide
redirect_from:
  - /topics/
---

I write here about engineering at scale, AI in production, and the parts everyone leaves out of the pitch deck. Twenty-five years of doing this and I'm still surprised at how often the interesting story is the one nobody mentions until two beers in.

Most posts come out of work I've actually shipped — the four pending patents, the platform decompositions, the fraud system that prevented enough loss to fund a small country, the AI workshop I ran last year for fifty engineers who promptly built better agents than I had. Posts run long, usually 1,500 words or more, because the interesting parts always do.

## All posts

<ul class="entries-list" style="margin-top:0;">
{% assign posts = site.posts | sort: "date" | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <small style="color:#6b6259;">· {{ post.date | date: "%b %-d, %Y" }}</small></li>
{% endfor %}
</ul>

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
