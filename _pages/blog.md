---
permalink: /blog/
title: "Blog"
author_profile: true
---

<div class="grid__wrapper">
{% for post in paginator.posts %}
  {% include archive-single.html type="grid" %}
{% endfor %}
</div>

{% include paginator.html %}
