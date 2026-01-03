---
layout: page
permalink: /publications/
title: publications
description: publications by categories in reversed chronological order.
#years: [2025, 2024, 2023, 2022, 2021, 2020] 
pubyears:  [2025, 2024, 2023, 2022, 2021]
talkyears: [2025, 2021, 2020]
nav: true
nav_order: 0 
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.pubyears %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>

---
## Talks
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.talkyears %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f talks -q @*[year={{y}}]* %}
{% endfor %}

</div>

