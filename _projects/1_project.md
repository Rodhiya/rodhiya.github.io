---
layout: page
title: Decaying Turbulence via DNS
description: The asymptotic state of decaying homogeneous turbulence, resolved with record-duration direct numerical simulations.
img: assets/img/12.jpg
importance: 1
category: research
related_publications: true
---

My PhD research investigates the long-time evolution of decaying homogeneous
turbulence — a fundamental open problem in fluid dynamics.

Using massively parallel pseudo-spectral Direct Numerical Simulations (up to
$$4096^3$$ grids) run over roughly 200,000 initial eddy-turnover times at
$$Re_\lambda = 30\text{–}145$$, I resolve the asymptotic decay exponent by
cleanly separating the Birkhoff–Saffman ($$E(k)\sim k^2$$) and
Loitsianskii–Kolmogorov–Batchelor ($$E(k)\sim k^4$$) initial-spectrum regimes.
These results provide empirical benchmarks for Migdal's recent field-theoretic
predictions for decaying turbulence.

Highlights:

- Designed a dynamic regridding scheme (coarsening the grid as scales grow) that
  cut computational cost by more than $$5\times$$ while preserving turbulence
  statistics.
- Built a modular single-GPU pseudo-spectral Navier–Stokes solver in C++/CUDA
  (cuFFT, RK2, divergence-free projection), now being extended to a multi-node
  multi-GPU solver with cuFFTMp/NVSHMEM and validated to machine precision.
- Developing machine-learning surrogates that couple energy-spectrum forecasting
  with conditional velocity-field generation, validated against DNS.
- Ran production campaigns on TACC (via ACCESS), NYU Greene, and KAUST
  Shaheen III, with reproducibility data and figure scripts released publicly.
