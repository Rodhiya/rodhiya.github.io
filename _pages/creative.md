---
layout: page
title: Creative Space
permalink: /creative/
description: Blogs, poems, photographs and videos from outside the lab.
nav: true
nav_order: 3
# Order of the filter buttons. A button only appears once that category has a post.
display_categories: [blogs, poems, photographs, videos]
---

<!-- pages/creative.md -->
{%- assign creative_posts = site.creative | sort: "date" | reverse -%}
<div class="projects creative">
{%- if creative_posts.size > 0 %}
  <div class="creative-filters" role="group" aria-label="Filter posts">
    <button type="button" class="creative-filter active" data-filter="all" aria-pressed="true">All</button>
    {%- for category in page.display_categories %}
    {%- assign category_posts = creative_posts | where: "category", category -%}
    {%- if category_posts.size > 0 %}
    <button type="button" class="creative-filter" data-filter="{{ category }}" aria-pressed="false">{% include creative_label.html category=category %}</button>
    {%- endif %}
    {%- endfor %}
  </div>

  <div class="creative-grid">
    {%- for post in creative_posts -%}
      {% include creative_card.html %}
    {%- endfor %}
  </div>
{%- else %}
  <p class="creative-empty">New posts coming soon.</p>
{%- endif %}
</div>

<script src="{{ '/assets/js/creative_filter.js' | relative_url }}?v={{ site.time | date: '%s' }}"></script>
