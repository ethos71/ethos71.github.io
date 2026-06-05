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

Field notes most weeks; longer case studies when the work earns it.

## All posts

{% assign posts = site.posts | sort: "date" | reverse %}
{% include post-list.html posts=posts %}

## By category

{% assign cats = site.categories | sort %}
{% for category in cats %}
{% assign cat_name = category[0] %}
{% assign cat_posts = category[1] %}
<h3 class="taxonomy-title" id="cat-{{ cat_name | slugify }}">{{ cat_name }} <span class="count">{{ cat_posts.size }}</span></h3>
{% include post-list.html posts=cat_posts %}
{% endfor %}

## By tag

{% assign tags = site.tags | sort %}
{% for tag in tags %}
{% assign tag_name = tag[0] %}
{% assign tag_posts = tag[1] %}
<h3 class="taxonomy-title" id="tag-{{ tag_name | slugify }}">{{ tag_name }} <span class="count">{{ tag_posts.size }}</span></h3>
{% include post-list.html posts=tag_posts %}
{% endfor %}
