---
layout: page
title: Pseudo-spectral vs. Finite-Difference Solvers
description: Relative accuracy of numerical schemes for long-time turbulence simulation.
img: assets/img/projects/fd_vs_spectral.jpg
importance: 2
category: research
---

Pseudo-spectral methods are the standard for simulating turbulence in periodic
domains. Their derivatives are exact for resolved fields, and a finite-difference
(FD) scheme needs roughly six times more grid points per direction to match
their accuracy. But spectral codes scale poorly: every 3-D FFT needs all-to-all
communication between processors, and walls and complex geometries are hard to
handle. FD codes need only nearest-neighbour communication and handle walls
naturally.

So does the extra accuracy of a single spectral time step actually show up over
a long turbulence simulation? This work, done at IIT Kanpur with Prof. Mahendra
K. Verma and Dr. Shashwat Bhattacharya, says largely no.

## Setup

- **Flow:** forced homogeneous turbulence in a $$(2\pi)^3$$ periodic box on a
  $$256^3$$ grid, driven by Taylor–Green forcing at Reynolds numbers 965,
  1231, 1515 and 1994.
- **Solvers:** Py-Tarang (pseudo-spectral) and Py-Saras (second-order central
  FD on a staggered grid, with a geometric-multigrid pressure Poisson solver).
  Both are Python codes accelerated on GPUs with CuPy.
- **Fair comparison:** both solvers start from the same fully developed
  turbulent field and use the same RK3 time stepping ($$\Delta t = 0.001$$)
  for 100 time units.
- **Cost:** about 0.8 s per step for the spectral code and 1.5 s for the FD
  code on one NVIDIA RTX 3090. The multigrid pressure solve makes FD slower on a
  single GPU, but on many GPUs the FFT's all-to-all communication is expected
  to reverse that.

## Findings

**Same energy, same statistics.** The time-averaged kinetic energies from the
two solvers agree to within about 4% at every Reynolds number. The flow
structures are not identical, because the solutions diverge as numerical errors
grow, but they are statistically the same: similar vortex sizes and densities,
and nearly identical PDFs of velocity and velocity gradients.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/fd-vs-spectral/vorticity.jpg" title="Vorticity fields" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Vertical vorticity with horizontal velocity vectors on the midplane at \(t = 60\) for the four Reynolds numbers: (a) pseudo-spectral and (b) finite-difference solver.
</div>

**Same spectra and fluxes.** Energy spectra and energy fluxes from the two codes
lie on top of each other across the energy-containing and inertial ranges. The
only difference is a small kink near $$k \approx 100$$ in the FD spectra,
where energy piles up at the smallest resolved scales.

<div class="row justify-content-sm-center">
  <div class="col-sm-9 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/fd-vs-spectral/spectra_flux.png" title="Energy spectra and fluxes" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Energy spectra \(E(k)\) (pseudo-spectral: solid blue; finite difference: dashed red) for the four Reynolds numbers, with the energy flux \(\Pi(k)\) in the insets.
</div>

## Why it works

A statistically steady turbulent flow lives on an attractor in phase space.
Both solvers produce trajectories confined to that attractor. Instead of piling
up, the per-step numerical errors largely cancel, so both codes sample the same
statistics even though their trajectories differ. This is similar to the
shadowing lemma for chaotic systems.

The practical point is that FD solvers are a credible, more scalable alternative
for very large turbulence simulations, where FFT communication dominates the
cost. I see this directly in my multi-GPU spectral code, where data transposes
take about a third of each time step
([more on my SC'26 page]({{ '/conferences/sc26/' | relative_url }})).

## Publication

- A. Rodhiya, S. Bhattacharya and M. K. Verma, "Relative accuracy of turbulence
  simulations using pseudo-spectral and finite difference solvers,"
  _Sādhanā_ **51**, 38 (2026).
  [doi:10.1007/s12046-025-03035-y](https://doi.org/10.1007/s12046-025-03035-y)

<p class="text-muted small">Figures reproduced from Rodhiya, Bhattacharya &amp; Verma, <em>Sādhanā</em> (2026), © Indian Academy of Sciences.</p>
