---
layout: page
title: Hydrogen and its blend in Reheat Combustion
description: Detailed-chemistry DNS of hydrogen/methane flames at reheat gas-turbine conditions, and a high-order dimensionality-reduction method.
img: assets/img/projects/reheat_combustion.jpg
importance: 3
category: research
---

Sequential, or "reheat", gas turbines burn fuel in two stages. In the second
stage, fuel is injected into hot vitiated gas from the first and burns largely
by **spontaneous ignition**. These combustors are a promising route to burning
hydrogen for carbon-free power. In practice two modes coexist: spontaneous
ignition in the hot bulk flow, and **flame propagation** in the cooler layers
near the walls, which is also what controls flashback. How the balance between
them shifts with operating pressure and fuel blend had not been quantified, even
though burners are often developed with atmospheric-pressure tests.

For my M.Tech (Research) at IISc Bangalore, with Prof. Konduri Aditya, I studied
this with detailed-chemistry DNS. The work was a collaboration with SINTEF
Energy Research, ZHAW and Sandia's Combustion Research Facility.

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    <video class="img-fluid rounded z-depth-1" autoplay muted loop playsinline preload="metadata" poster="{{ '/assets/video/sc26/reheat_combustor.jpg' | relative_url }}" aria-label="Animation of the temperature field in a reheat combustor">
      <source src="{{ '/assets/video/sc26/reheat_combustor.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
</div>
<div class="caption">
  Temperature in the simplified reheat combustor from a 2-D DNS of a hydrogen flame at 5 bar.
</div>

## Simulations

- **Solver:** the massively parallel S3D code, a fully compressible solver
  with 8th-order central differences and 4th-order Runge–Kutta time stepping.
  It uses mixture-averaged transport through CHEMKIN and TRANSPORT.
- **Chemistry:** a 9-species, 21-reaction mechanism for hydrogen and a
  21-species, 42-reaction reduced San Diego mechanism for hydrogen/methane
  blends.
- **Configuration:** a simplified reheat combustor with a mixing duct opening
  into a combustion chamber, isothermal 750 K walls and turbulent inflow from a
  channel-flow DNS. The flame is resolved by at least 35 grid points, with
  5–22 μm grid spacing.
- **Parametric study:** nine cases covering 1, 5 and 10 bar and hydrogen
  fractions of 100%, 70% and 50%. Inlet temperatures were adjusted to keep the
  ignition delay, and hence the flame position, fixed.
- **Analysis:** chemical explosive mode analysis (CEMA) classifies each point
  as auto-ignition, assisted ignition (flame propagation) or extinction, so the
  fuel consumed by each mode can be measured directly.
- **Systems:** SahasraT (IISc), Fram (Sigma2, Norway), Summit (OLCF) and Cori
  (NERSC).

<div class="row justify-content-sm-center">
  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/reheat-combustion/setup.png" title="Combustor configuration" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/reheat-combustion/temperature_2d_3d.png" title="2-D vs. 3-D DNS" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Left: the simplified reheat combustor and its multi-block layout. Right: instantaneous temperature (K) from an earlier 3-D DNS of this configuration (top, Aditya et al. 2019) and from the 2-D DNS in this study (bottom).
</div>

## Key findings

**2-D DNS are a cheap, reliable guide to trends.** Compared with full 3-D DNS,
the 2-D simulations produce a W-shaped flame instead of a V-shaped one, because
of a thinner thermal boundary layer. The bias in the fraction of fuel burned by
spontaneous ignition, however, is only about 10%. That bias can be accounted
for, so affordable 2-D DNS can screen many burner variants and operating points
early in design.

**Higher pressure shifts combustion toward flame propagation.** At 1 bar, about
90% of the hydrogen is consumed by spontaneous ignition. At 10 bar the two modes
consume comparable shares, with assisted ignition, or propagation, slightly
ahead.

<div class="row justify-content-sm-center">
  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/reheat-combustion/pressure_modes.png" title="Effect of pressure" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
  <div class="col-sm-6 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/reheat-combustion/hydrogen_fraction.png" title="Effect of hydrogen fraction" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Combustion modes from CEMA (green: auto-ignition; red: assisted ignition; blue: extinction) and the fraction of fuel consumed in each. Left: 1, 5 and 10 bar. Right: hydrogen/methane blends, labelled (pressure in bar, H₂ fraction).
</div>

**More hydrogen does the same.** As the hydrogen fraction rises, the share of
fuel burned by spontaneous ignition falls and propagation grows, more strongly
at 5 bar than at 1 bar. This is counter-intuitive, since hydrogen is far more
reactive than methane. It happens because methane-rich blends need hotter
reactants to hold the flame in the same place. Since near-wall flame
propagation controls flashback, atmospheric-pressure tests can understate how a
hydrogen burner behaves at full load. That matters for designing
hydrogen-ready reheat combustors.

## Co-kurtosis PCA for reduced-order chemistry

Detailed chemistry makes these simulations expensive, and standard principal
component analysis (PCA), the usual way to compress the thermochemical state,
can miss rare but critical events such as ignition kernels. I co-authored
**co-kurtosis PCA (CoK-PCA)**, which takes its principal directions from the
fourth-order joint moment (the co-kurtosis tensor) instead of the covariance,
so it picks up these extreme-valued, stiff dynamics. On ethylene–air
auto-ignition and ethanol HCCI-engine datasets, it reconstructs species
production and heat-release rates more accurately than PCA where the chemistry
is active.

<div class="row justify-content-sm-center">
  <div class="col-sm-5 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/reheat-combustion/cokpca_synthetic.png" title="CoK-PCA on a synthetic dataset" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  A synthetic dataset with a small cluster of extreme-valued samples. Principal vectors from PCA (red) follow the bulk variance; those from CoK-PCA (blue) point toward the anomalous event.
</div>

## Publications

- A. Rodhiya, A. Gruber, M. R. Bothien, J. H. Chen and K. Aditya, "Spontaneous
  ignition and flame propagation in hydrogen/methane wrinkled laminar flames at
  reheat conditions: Effect of pressure and hydrogen fraction," _Combust.
  Flame_ **269**, 113695 (2024).
  [doi:10.1016/j.combustflame.2024.113695](https://doi.org/10.1016/j.combustflame.2024.113695)
- A. Rodhiya, K. Aditya, A. Gruber and J. H. Chen, "Simulations of flame
  structure in a reheat burner: pressure scaling," _AIAA Propulsion and Energy
  Forum_ (2021). [doi:10.2514/6.2021-3448](https://doi.org/10.2514/6.2021-3448)
- A. Jonnalagadda, S. Kulkarni, A. Rodhiya, H. Kolla and K. Aditya, "A
  co-kurtosis based dimensionality reduction method for combustion datasets,"
  _Combust. Flame_ **250**, 112635 (2023).
  [doi:10.1016/j.combustflame.2023.112635](https://doi.org/10.1016/j.combustflame.2023.112635)
- A. Rodhiya, M.Tech (Research) thesis, IISc (2022).
  [etd.iisc.ac.in/handle/2005/5760](https://etd.iisc.ac.in/handle/2005/5760)

<p class="text-muted small">Figures reproduced from Rodhiya et al., <em>Combust. Flame</em> 269 (2024) and Jonnalagadda et al., <em>Combust. Flame</em> 250 (2023), © The Combustion Institute.</p>

<script>
  // Respect reduced-motion preferences: show the still poster instead of looping video.
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('video[autoplay]').forEach(function(v) { v.removeAttribute('autoplay'); v.pause(); v.controls = true; });
  }
</script>
