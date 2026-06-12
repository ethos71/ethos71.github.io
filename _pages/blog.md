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
