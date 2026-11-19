---
layout: page
title: Vapor Chamber for Fiber-Laser Cooling
description: A vapor-chamber and heat-sink assembly to air-cool a high-power fiber laser.
img: assets/img/projects/vapor_chamber.jpg
importance: 5
category: engineering
---

High-power fiber lasers concentrate their waste heat in a few small, hot spots.
In a summer internship (May–July 2018) at a defense research lab, I designed an
air-cooled assembly to remove **800 W from two heat sources**, using only a
**450 × 250 × 120 mm** space.

The design spreads each source's heat with a two-phase **vapor chamber**, so a
shared **pin-fin heat sink** can reject it to forced air at a modest air speed.

<div class="row justify-content-sm-center">
  <div class="col-sm-7 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/vapor-chamber/diagram.png" title="Vapor chamber and pin-fin heat sink" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
  <div class="col-sm-5 mt-3 mt-md-0">
    {% include figure.html path="assets/img/projects/vapor-chamber/assembly_cad.jpg" title="Assembly envelope" class="img-fluid rounded z-depth-1" zoomable=true %}
  </div>
</div>
<div class="caption">
  Left: my design in cross-section (not to scale). Two water-filled copper vapor chambers spread the heat from each source into a shared aluminum pin-fin array cooled by forced air. Right: the assembly envelope, with the vapor chambers (blue) above and below the fins.
</div>

## How a vapor chamber works

A vapor chamber is a flat heat pipe. Under the heat source, the working fluid
(water) evaporates. The vapor spreads across the chamber and condenses on the
cooler face, giving up its latent heat, and a porous wick pumps the liquid back
by capillary action. The vapor space stays almost isothermal, so the chamber
behaves like a plate with a conductivity well above solid copper's.

## Choosing the wick

The wick has to pump liquid across the full 250 mm width of the chamber. It
works only if its **capillary pressure** ($$2\sigma/r$$) exceeds the **viscous
pressure drop** of the liquid flowing through it, which I estimated with Darcy's
law integrated over the chamber, accounting for evaporation and condensation
along the path. Fine pores raise the capillary pressure but also the flow
resistance, so the choice is a real trade-off:

<div class="table-responsive" markdown="1">

| Wick (copper) | Pore radius | Permeability | Porosity | Capillary pressure | Liquid pressure loss | Verdict |
|---|---|---|---|---|---|---|
| Sintered powder | 0.009 mm | 1.7 × 10⁻¹² m² | 52% | 15,100 Pa | 44,500 Pa | fails |
| Foam | 0.21 mm | 1.9 × 10⁻⁹ m² | 91% | 647 Pa | 41 Pa | works |
{: .table .table-sm .scaling-table}

</div>

The final chamber has a 1 mm copper wall, a 0.5 mm copper-foam wick and a 2 mm
vapor space. Treating the wall and wick as series thermal resistances, with the
vapor phase nearly isothermal, gives an effective conductivity of about
**637 W/m·K** with the foam wick (458 W/m·K with sintered powder), against
401 W/m·K for solid copper.

## Sizing the heat sink

I compared two heat-sink families within the same envelope:

- **Rectangular fins:** spaced at twice the thermal boundary-layer thickness at
  the fin's trailing edge, so neighbouring boundary layers don't merge, with the
  fin thickness chosen to maximise fin effectiveness.
- **Staggered pin fins:** heat transfer from tube-bank correlations for flow
  across pin arrays, with row-count corrections and adiabatic-tip fin
  efficiency. I wrote a small C++ program to sweep pin diameter and air speed.

<div class="sc-page">
  <figure class="sc-chart">
    <div class="sc-legend">
      <span><i class="sc-swatch sc-s1"></i>Pin fins, 10 mm</span>
      <span><i class="sc-swatch sc-s2"></i>Pin fins, 15 mm</span>
      <span><i class="sc-swatch sc-s3"></i>Pin fins, 20 mm</span>
      <span><i class="sc-swatch sc-s4"></i>Rectangular fins, 2 mm</span>
    </div>
    <svg viewBox="0 0 680 280" role="img" aria-labelledby="hs-title hs-desc">
      <title id="hs-title">Heat rejected by candidate heat sinks vs. air velocity</title>
      <desc id="hs-desc">Pin-fin arrays reach the 800 W target at about 2.3 to 5.2 metres per second depending on pin diameter; rectangular 2 mm fins stay below 800 W even at 10 metres per second.</desc>
      <g class="sc-grid">
        <line x1="70" y1="230.0" x2="610" y2="230.0"/>
        <line x1="70" y1="195.0" x2="610" y2="195.0"/>
        <line x1="70" y1="160.0" x2="610" y2="160.0"/>
        <line x1="70" y1="125.0" x2="610" y2="125.0"/>
        <line x1="70" y1="90.0" x2="610" y2="90.0"/>
        <line x1="70" y1="55.0" x2="610" y2="55.0"/>
        <line x1="70" y1="20.0" x2="610" y2="20.0"/>
      </g>
      <g class="sc-axis">
        <text x="62" y="234.0" text-anchor="end">0</text>
        <text x="62" y="199.0" text-anchor="end">200</text>
        <text x="62" y="164.0" text-anchor="end">400</text>
        <text x="62" y="129.0" text-anchor="end">600</text>
        <text x="62" y="94.0" text-anchor="end">800</text>
        <text x="62" y="59.0" text-anchor="end">1,000</text>
        <text x="62" y="24.0" text-anchor="end">1,200</text>
        <text x="70" y="250" text-anchor="middle">0</text>
        <text x="178" y="250" text-anchor="middle">2</text>
        <text x="286" y="250" text-anchor="middle">4</text>
        <text x="394" y="250" text-anchor="middle">6</text>
        <text x="502" y="250" text-anchor="middle">8</text>
        <text x="610" y="250" text-anchor="middle">10</text>
        <text x="340" y="272" text-anchor="middle">air velocity (m/s)</text>
        <text x="16" y="125" text-anchor="middle" transform="rotate(-90 16 125)">heat rejected (W)</text>
      </g>
      <line class="sc-ideal-line" x1="70" y1="90.0" x2="610" y2="90.0"/>
      <text class="sc-target" x="606" y="84.0" text-anchor="end">800 W target</text>
      <polyline class="sc-line sc-s1" points="151.0,162.3 178.0,116.7 205.0,70.9 232.0,35.6"/>
      <polyline class="sc-line sc-s2" points="232.0,99.2 259.0,77.4 286.0,57.7"/>
      <polyline class="sc-line sc-s3" points="286.0,117.1 313.0,104.8 340.0,93.4 367.0,82.7 394.0,72.5"/>
      <polyline class="sc-line sc-s4" points="205.0,186.9 232.0,179.8 259.0,172.8 286.0,165.5 313.0,158.5 340.0,152.9 367.0,145.5 394.0,139.9 421.0,132.2 448.0,126.6 475.0,120.9 502.0,115.3 529.0,109.6 556.0,104.0 583.0,98.3 610.0,92.6"/>
      <g class="sc-points">
        <circle class="sc-s1" cx="151.0" cy="162.3" r="4"><title>Pin fins, 10 mm (190 pins): 387 W at 1.5 m/s</title></circle>
        <circle class="sc-s1" cx="178.0" cy="116.7" r="4"><title>Pin fins, 10 mm (190 pins): 647 W at 2 m/s</title></circle>
        <circle class="sc-s1" cx="205.0" cy="70.9" r="4"><title>Pin fins, 10 mm (190 pins): 909 W at 2.5 m/s</title></circle>
        <circle class="sc-s1" cx="232.0" cy="35.6" r="4"><title>Pin fins, 10 mm (190 pins): 1,111 W at 3 m/s</title></circle>
        <circle class="sc-s2" cx="232.0" cy="99.2" r="4"><title>Pin fins, 15 mm (91 pins): 748 W at 3 m/s</title></circle>
        <circle class="sc-s2" cx="259.0" cy="77.4" r="4"><title>Pin fins, 15 mm (91 pins): 872 W at 3.5 m/s</title></circle>
        <circle class="sc-s2" cx="286.0" cy="57.7" r="4"><title>Pin fins, 15 mm (91 pins): 985 W at 4 m/s</title></circle>
        <circle class="sc-s3" cx="286.0" cy="117.1" r="4"><title>Pin fins, 20 mm (45 pins): 645 W at 4 m/s</title></circle>
        <circle class="sc-s3" cx="313.0" cy="104.8" r="4"><title>Pin fins, 20 mm (45 pins): 715 W at 4.5 m/s</title></circle>
        <circle class="sc-s3" cx="340.0" cy="93.4" r="4"><title>Pin fins, 20 mm (45 pins): 780 W at 5 m/s</title></circle>
        <circle class="sc-s3" cx="367.0" cy="82.7" r="4"><title>Pin fins, 20 mm (45 pins): 842 W at 5.5 m/s</title></circle>
        <circle class="sc-s3" cx="394.0" cy="72.5" r="4"><title>Pin fins, 20 mm (45 pins): 900 W at 6 m/s</title></circle>
        <circle class="sc-s4" cx="205.0" cy="186.9" r="4"><title>Rectangular fins, 2 mm: 246 W at 2.5 m/s</title></circle>
        <circle class="sc-s4" cx="232.0" cy="179.8" r="4"><title>Rectangular fins, 2 mm: 287 W at 3 m/s</title></circle>
        <circle class="sc-s4" cx="259.0" cy="172.8" r="4"><title>Rectangular fins, 2 mm: 327 W at 3.5 m/s</title></circle>
        <circle class="sc-s4" cx="286.0" cy="165.5" r="4"><title>Rectangular fins, 2 mm: 369 W at 4 m/s</title></circle>
        <circle class="sc-s4" cx="313.0" cy="158.5" r="4"><title>Rectangular fins, 2 mm: 409 W at 4.5 m/s</title></circle>
        <circle class="sc-s4" cx="340.0" cy="152.9" r="4"><title>Rectangular fins, 2 mm: 440 W at 5 m/s</title></circle>
        <circle class="sc-s4" cx="367.0" cy="145.5" r="4"><title>Rectangular fins, 2 mm: 483 W at 5.5 m/s</title></circle>
        <circle class="sc-s4" cx="394.0" cy="139.9" r="4"><title>Rectangular fins, 2 mm: 515 W at 6 m/s</title></circle>
        <circle class="sc-s4" cx="421.0" cy="132.2" r="4"><title>Rectangular fins, 2 mm: 559 W at 6.5 m/s</title></circle>
        <circle class="sc-s4" cx="448.0" cy="126.6" r="4"><title>Rectangular fins, 2 mm: 591 W at 7 m/s</title></circle>
        <circle class="sc-s4" cx="475.0" cy="120.9" r="4"><title>Rectangular fins, 2 mm: 624 W at 7.5 m/s</title></circle>
        <circle class="sc-s4" cx="502.0" cy="115.3" r="4"><title>Rectangular fins, 2 mm: 656 W at 8 m/s</title></circle>
        <circle class="sc-s4" cx="529.0" cy="109.6" r="4"><title>Rectangular fins, 2 mm: 688 W at 8.5 m/s</title></circle>
        <circle class="sc-s4" cx="556.0" cy="104.0" r="4"><title>Rectangular fins, 2 mm: 720 W at 9 m/s</title></circle>
        <circle class="sc-s4" cx="583.0" cy="98.3" r="4"><title>Rectangular fins, 2 mm: 753 W at 9.5 m/s</title></circle>
        <circle class="sc-s4" cx="610.0" cy="92.6" r="4"><title>Rectangular fins, 2 mm: 785 W at 10 m/s</title></circle>
      </g>
    </svg>
    <figcaption>Estimated heat rejected by each heat-sink option against air velocity, from my hand calculations and C++ sweep (inlet air at 300 K). Hover over a point for its value.</figcaption>
  </figure>
</div>

Even the best rectangular fins (2 mm thick) reach only about 785 W at 10 m/s.
Pin-fin arrays pass the 800 W target at 2.5–5.5 m/s, depending on pin diameter.
The final design uses **staggered aluminum pins** with a transverse pitch of
2.5 diameters, which reject about 870 W at 3.5 m/s with 15 mm pins.

## Materials

I also surveyed candidate materials for the assembly and its optical mounts,
comparing thermal conductivity, expansion, diffusivity, strength and
machinability. The candidates were copper, aluminum, titanium and magnesium,
plus the low-expansion Zerodur glass-ceramic and Invar (FeNi36).

## Related work

In a later winter project, I simulated helium flow through a Zanker flow
conditioner in ANSYS, evaluating flow stabilization, pressure drop and
development length for a 383 K, 6 bar duct flow.
