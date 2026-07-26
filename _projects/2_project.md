---
layout: page
title: Pseudo-spectral vs. Finite-Difference Solvers
description: Relative accuracy of numerical schemes for long-time turbulence simulation.
img: assets/img/3.jpg
importance: 2
category: research
---

While spectral solvers are theoretically more accurate per timestep, this work
demonstrated that pseudo-spectral and finite-difference methods yield nearly
identical results for long-term turbulence simulations.

Simulating forced homogeneous turbulence on $$256^3$$ grids at Reynolds numbers
up to $$\sim 2000$$, I compared the pseudo-spectral solver Py-Tarang against the
finite-difference solver Py-Saras. Despite higher per-timestep error, the
finite-difference solver matched spectral accuracy across energy evolution,
spectra, energy flux, and velocity-derivative PDFs.

The central finding: within a turbulence attractor, numerical errors tend to
cancel rather than accumulate, supporting the use of more scalable
finite-difference solvers for large-grid DNS. Simulations were GPU-accelerated
using in-house CuPy frameworks on NVIDIA hardware.
