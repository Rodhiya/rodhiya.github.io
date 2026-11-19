---
layout: page
title: PCM Thermal Energy Storage
description: A phase-change-material thermal battery, from CAD to CFD to an instrumented test rig.
img: assets/img/projects/pcm_storage.jpg
importance: 4
category: engineering
---

Solar and waste heat are available at the wrong times. A phase-change material
(PCM) stores that heat as latent heat while it melts and releases it at a nearly
constant temperature when it freezes. This gives far more storage per unit
volume than heating water.

For my B.Tech project at IIT (BHU) Varanasi (2018), with Sourav Majumdar and
Ipshita and guided by Dr. Om Prakash Singh, we designed a paraffin-wax "thermal
battery" charged by hot water. We studied it with CFD and on a test rig we built
and instrumented.

## Design choices

From a literature review we chose:

- **Paraffin wax** as the PCM: high latent heat, little supercooling, chemically
  stable and non-corrosive. Its weakness is a very low thermal conductivity,
  about 0.2 W/m·K.
- **Water** as the heat-transfer fluid.
- **Copper tubes** to carry the heat into the wax.

The limiting step is conducting heat into the wax, so the work focused on
geometry, flow conditions and conductivity enhancement.

## Simulation

I built the CAD-to-CFD workflow: geometry in SolidWorks, surface meshing in
HyperMesh, and transient simulations in STAR-CCM+ with a volume-of-fluid
melting–solidification model. Hot water entered at 80 °C. We used the
simulations to choose:

- **the PCM layer thickness** in a compact cuboid design, where the PCM blocks
  also act as baffles for the water flow;
- **the water inlet velocity**;
- **the tube pitch** in a shell-and-tube design, using a 2-D axisymmetric model
  of one copper tube (0.5 inch) inside a 4-inch PCM annulus. This set the pitch
  at twice the annulus radius.

<div class="row">
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/pcm-storage/cuboid_cad.png" title="Cuboid PCM design" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/pcm-storage/serpentine_cad.jpg" title="Shell-and-tube design" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/pcm-storage/axisymmetric_model.png" title="Axisymmetric model" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Left to right: the cuboid design with PCM blocks (dark) as baffles in the water path; a serpentine copper tube in a PCM tank; and the 2-D axisymmetric model of one tube used to size the PCM annulus.
</div>

<div class="row justify-content-sm-center">
  <div class="col-sm-9 mt-3 mt-md-0">
    {% include figure.html path="assets/img/sc26/pcm_melt_curve.png" title="Solid fraction vs time" class="img-fluid rounded z-depth-1" zoomable=true %}
    {% include figure.html path="assets/img/sc26/pcm_melt_contour.png" title="Melt front" class="img-fluid rounded z-depth-1 mt-2" zoomable=true %}
  </div>
</div>
<div class="caption">
  STAR-CCM+ simulation of paraffin melting around a hot-water tube (80 °C inlet, 0.94 L/min). The solid volume fraction (svf) falls from 1 to about 0.35 in 2 hours. The contour shows the melt front (blue = liquid, red = solid).
</div>

## Experiments

We built a shell-and-tube test section: a 1-ft, 4-inch-diameter tube filled
with paraffin around a 10 mm copper pipe carrying hot water from a heated
reservoir. The inlet temperature was held constant by hand-controlling an
immersion heater. Nine T-type thermocouples, in three axial planes at 11, 22
and 33 mm from the pipe, tracked the melt front, and we computed the stored
sensible and latent heat from them. We tested four cases: horizontal and
vertical orientation, each at 1 and 1.5 L/min.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/pcm-storage/rig.jpg" title="Test rig" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  The test rig in vertical (left) and horizontal (right) orientation: pump and heated water reservoir, the PCM test section, and the thermocouple readout.
</div>

<div class="row justify-content-sm-center">
  <div class="col-sm-9 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/pcm-storage/temperature_horizontal.png" title="Temperature history" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Horizontal orientation at 1 L/min: temperature at 11, 22 and 33 mm from the pipe. The 11 mm reading levels off near 53 °C when the melt front reaches it, while the outer readings are still rising.
</div>

What we found:

- **Horizontal beats vertical.** In the horizontal orientation, natural
  convection in the melt raises the heat-transfer coefficient. Vertically at
  1 L/min, the melt front had not reached even the 11 mm thermocouple after
  5 hours.
- **Higher flow charges faster.** The pipe flow is turbulent, so raising the
  flow rate from 1 to 1.5 L/min raises the Nusselt number, and the inner
  thermocouple reached the melting plateau much sooner.
- **Convection in the melt matters.** In vertical runs, thermocouples at the same radius read
  higher near the top of the test section, because the melt melts faster there.

## Enhancing conductivity with particles

To tackle the wax's low conductivity, we mixed Al₂O₃ particles (0.05% and
1.18%) and graphene (0.05% and 0.71%) into 50 ml samples of molten paraffin.
We then melted them from a heated base and recorded the melt volume over time.
Graphene-loaded wax melted fastest, followed by Al₂O₃ and then plain wax,
although at 0.05% loading the differences were small. The lighter graphene also
settles less than metal-oxide particles.

<div class="row">
  <div class="col-sm mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/pcm-storage/melt_front.jpg" title="Melt front with Bénard cells" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Paraffin with 0.05% Al₂O₃ melting from below, 15 to 90 minutes after heating starts. The wavy solid–liquid interface comes from Bénard convection cells in the melt, which grow and merge as the melt layer thickens.
</div>
