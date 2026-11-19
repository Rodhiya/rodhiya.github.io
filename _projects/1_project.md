---
layout: page
title: Decaying Turbulence via DNS
description: The asymptotic state of decaying homogeneous turbulence, resolved with record-duration direct numerical simulations.
img: assets/img/projects/decaying_turbulence.jpg
importance: 1
category: research
---

How does turbulence die out once nothing is stirring it? If the kinetic energy
decays as a power law, $$E_n \sim t^{-n}$$, classical theory gives two answers
that depend on the largest scales of the initial flow. A Birkhoff–Saffman (BS)
spectrum, $$E(k) \sim k^2$$ at small $$k$$, gives $$n = 6/5$$. A
Loitsianskii–Kolmogorov–Batchelor (LKB) spectrum, $$E(k) \sim k^4$$, gives
$$n = 10/7$$. Experiments and earlier simulations report anything from
$$n \approx 1.15$$ to $$1.45$$. They are limited by short run times, initial
spectra that aren't controlled, and the finite size of the domain.

My PhD research, with Prof. K. R. Sreenivasan at NYU, settles this with direct
numerical simulations (DNS) that are long enough, large enough and controlled
enough to reach the asymptotic state. It also uses the results to test
Alexander Migdal's recent field-theoretic solution of decaying turbulence.

<div class="row justify-content-sm-center">
  <div class="col-sm-6 mt-3 mt-md-0">
    <video class="img-fluid rounded z-depth-1" autoplay muted loop playsinline preload="metadata" poster="{{ '/assets/video/sc26/decaying_turbulence.jpg' | relative_url }}" aria-label="Animation of a velocity field in decaying turbulence">
      <source src="{{ '/assets/video/sc26/decaying_turbulence.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
</div>
<div class="caption">
  A velocity component on a plane through a 256³ decaying-turbulence DNS. With no forcing, the small eddies die first and the remaining structures grow larger.
</div>

## Simulations

- **Solver:** a pseudo-spectral Navier–Stokes solver in a triply periodic box,
  with phase-shift de-aliasing and semi-implicit time stepping.
- **Controlled initial conditions:** random Gaussian fields with a model
  spectrum whose low-wavenumber slope is set exactly ($$k^2$$ for BS,
  $$k^4$$ for LKB). The initial integral scale is about 1% of the box, and
  0.54–0.58% for the longest runs, to delay confinement effects.
- **Scale:** initial $$Re_\lambda$$ from 30 to 145 on grids from $$512^3$$
  to $$4096^3$$, with 3–10 independent realizations per case.
- **Duration:** up to about **200,000 initial eddy-turnover times**. Earlier
  studies ran for around 1,000.
- **Systems:** TACC (through an ACCESS allocation), NYU's HPC cluster and
  KAUST's Shaheen III.

### Dynamic regridding

As turbulence decays, the smallest (Kolmogorov) scale grows and a fixed grid
becomes wastefully over-resolved. I designed a regridding scheme that halves
the grid whenever the resolution parameter $$k_{max}\eta$$ exceeds 6, which
resets it to about 3, still double the usual DNS requirement. Each step removes
7/8 of the degrees of freedom and roughly doubles the time step, which is about
16× cheaper per unit of simulated time. Over a full run this cut the cost by
more than 5×. A sensitivity study showed that more aggressive thresholds
distort the decay rate, while $$k_{max}\eta = 6$$ is indistinguishable from
the run without regridding.

<div class="row justify-content-sm-center">
  <div class="col-sm-7 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/decaying-turbulence/regridding.png" title="Validation of grid modification" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Validating the regridding scheme at \(Re_\lambda = 93\) on a \(2048^3\) grid: the local decay exponent \(n(t)\) with and without grid modification. Lower thresholds drift away from the reference; \(k_{max}\eta = 6\) overlaps it exactly.
</div>

## Key findings

**Clean power laws with exponents that depend on the initial condition.** After
a short transient, both families decay as clean power laws. BS runs settle at
$$n \approx 1.25$$ at the highest Reynolds numbers. LKB runs hold
Kolmogorov's $$n = 10/7$$ for more than 2,000 turnover times. The decay
exponent depends on the large-scale structure of the initial flow, so it is not
universal.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/decaying-turbulence/energy_decay.png" title="Kinetic energy decay" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Kinetic energy decay for BS (left, reference slope −5/4) and LKB (right, reference slope −10/7) initial spectra, across initial Reynolds numbers.
</div>

**The finite box sets the limit.** In every case the power law breaks down when
the integral length grows to about 10–15% of the box. A smaller initial integral
scale lengthens the self-similar decay; that is why the long runs started with
such small energetic scales.

**How the spectrum evolves.** The low-wavenumber $$k^2$$ range of the BS case
survives throughout the decay, as the "permanence of large eddies" predicts. The
initial $$k^{-5/3}$$ range disappears within a few turnover times and is
replaced by a $$k^{-1}$$ range. Scaled by the energy and the integral length,
spectra from all times collapse onto one curve.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/decaying-turbulence/spectra.png" title="Energy spectra" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Energy spectra for a BS run at \(Re_\lambda = 105\): raw spectra over time (left) and in self-similar coordinates \(E(k)/(E_n L)\) against \(kL\) (right).
</div>

**A test of Migdal's theory.** For the BS case the agreement is excellent. The
Migdal length grows as $$t^{0.53}$$ against a predicted $$t^{1/2}$$, the
energy–length relation follows the predicted slope, and the scaling exponent of
the second-order structure function collapses onto the theoretical curve. For
the LKB case the energy decay departs from the predicted $$n = 5/4$$, but the
structure-function shape still matches the theory. The predicted $$k^{-7/2}$$
high-wavenumber tail is not visible at these Reynolds numbers.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/decaying-turbulence/migdal_zeta2.png" title="Comparison with Migdal's theory" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Local scaling exponent of the second-order structure function, \(\zeta_2\), against \(\log(r/L_M)\) for the BS run at \(Re_\lambda = 145\): at several times (left) and time-averaged with its spread (right), compared with Migdal's prediction.
</div>

**Where universality may lie.** Removing the lowest few wavenumbers changes the
"bulk" energy decay noticeably, but barely changes the enstrophy decay. Energy
decay is shaped by these large-scale boundary effects, so universality is more
likely to show up in the enstrophy.

## Ongoing work

- **Non-equilibrium energy flux** (manuscript in preparation). In decaying
  turbulence the energy flux through the inertial range is not constant. I show
  that, normalized by the instantaneous dissipation, it collapses onto a single
  curve that grows with $$kL$$. A self-similar analysis predicts it with no
  free parameters. This explains why the inertial-range spectrum is shallower
  than $$-5/3$$.
- **A multi-GPU solver for $$8192^3$$.** I'm writing a CUDA pseudo-spectral
  solver to push these simulations to higher Reynolds numbers. Progress and
  benchmarks are on my [SC'26 page]({{ '/conferences/sc26/' | relative_url }}).
- **ML surrogate models** (planned). The goal is data-driven surrogates that
  forecast how the energy spectrum evolves and generate velocity fields
  consistent with it, trained and validated on DNS ensembles.

## Publication and data

- A. Rodhiya and K. R. Sreenivasan, "The asymptotic state of decaying
  turbulence," _Phil. Trans. R. Soc. A_ **384**, 20250021 (2026).
  [doi:10.1098/rsta.2025.0021](https://doi.org/10.1098/rsta.2025.0021) (open
  access)
- Data and figure scripts:
  [doi:10.5281/zenodo.20397371](https://doi.org/10.5281/zenodo.20397371)

<p class="text-muted small">Figures reproduced from Rodhiya &amp; Sreenivasan (2026) under the CC BY 4.0 licence.</p>

<script>
  // Respect reduced-motion preferences: show the still poster instead of looping video.
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('video[autoplay]').forEach(function(v) { v.removeAttribute('autoplay'); v.pause(); v.controls = true; });
  }
</script>
