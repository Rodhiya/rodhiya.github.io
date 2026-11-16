---
layout: post
title: Awarded 1.5 million ACCESS credits for multi-GPU turbulence simulations
date: 2026-07-28 11:28:00-0400
inline: false
related_posts: false
---

I've been awarded a **Discover allocation of 1.5 million credits** from [ACCESS](https://access-ci.org/), the NSF-funded program that provides computing resources at national supercomputing centers. **750,000 credits are available now**, with the remainder to follow.

The allocation supports developing and scaling my **multi-node, multi-GPU pseudo-spectral solver** for homogeneous isotropic turbulence. The code is written in C++/CUDA and uses cuFFTMp for distributed 3-D FFTs, NVSHMEM for GPU-to-GPU communication, and MPI. Each stage of the port has been validated to machine precision against independent reference solvers.

With these resources, I'm:

- testing and optimizing the code on NVIDIA A100 nodes at NCSA Delta;
- scaling it from a single node to many nodes; and
- working toward **8192³ direct numerical simulations** of decaying turbulence, well beyond the 4096³ grids I have run so far.

The latest results, including a 58× speedup over our CPU code on a single node, are on my [SC'26 page]({{ '/conferences/sc26/' | relative_url }}).
