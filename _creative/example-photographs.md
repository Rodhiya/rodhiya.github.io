---
# TEMPLATE: copy this file, rename it, and change published to true (or delete the line).
published: false
title: Example photo post
description: Where and when the photos were taken.
category: photographs
date: 2026-10-16
# The first photo is used as the card image unless you set img.
photos:
  # Photos stored in the site: run bin/compress_photos.py, then paste its output here.
  # Paths are relative to assets/img/creative/.
  - src: example-gallery/1.jpg
    caption: A caption under the photo (optional)
  - src: example-gallery/3.jpg
  - src: example-gallery/7.jpg
  # Photos from Flickr: open the photo on Flickr, Share -> Embed, and copy the
  # https://live.staticflickr.com/... address from the code. Use the _b (1024px)
  # or _k (2048px) size. "link" is the photo's Flickr page (adds "View on Flickr").
  # - src: https://live.staticflickr.com/65535/12345678901_abcdef1234_b.jpg
  #   caption: A photo hosted on Flickr
  #   link: https://www.flickr.com/photos/your-username/12345678901/
---

A few words about the photos. This text appears above the gallery.

<!--
To show a whole Flickr album as a slideshow instead, open the album on Flickr,
choose Share -> Embed, and paste the code it gives you here, outside this comment.
-->
