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
<h3 class="taxonomy-title" id="cat-{{ category[0] | slugify }}">{{ category[0] }} <span class="count">{{ category[1].size }}</span></h3>
{% include post-list.html posts=category[1] %}
{% endfor %}

## By tag

{% assign tags = site.tags | sort %}
{% for tag in tags %}
<h3 class="taxonomy-title" id="tag-{{ tag[0] | slugify }}">{{ tag[0] }} <span class="count">{{ tag[1].size }}</span></h3>
{% include post-list.html posts=tag[1] %}
{% endfor %}
