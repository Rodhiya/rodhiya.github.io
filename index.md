## About me
---
I am a Doctoral Candidate in the Department of Mechanical and Aerospace Engineering at New York University’s Tandon School of Engineering, working under the supervision of <a href="https://engineering.nyu.edu/faculty/katepalli-sreenivasan" rel="external nofollow noopener" target="_blank">Prof. K. R. Sreenivasan</a> Previously, I earned my M.Tech (Research) in Computational Science from the Department of Computational and Data Sciences at the Indian Institute of Science (IISc), Bangalore.

<p>My research investigates the governing laws of turbulent kinetic energy and length scales in decaying turbulence. Using massively parallel Direct Numerical Simulations (DNS) of three-dimensional periodic boxes, I am working toward simulating decaying turbulence at the highest possible Reynolds numbers over extended durations. My goal is to provide a definitive, high-fidelity picture of the long-time evolution of turbulent flows.</p>

<p>Beyond the lab, I am a sports enthusiast with a particular love for Football, Badminton, and Cricket. I also enjoy the outdoors through trekking and camping.</p>

Interests:
- **Fluid Mechanics**: Fundamental turbulence and high-Reynolds-number flows.
- **Scientific Computing**: Massively parallel DNS and HPC optimization.
- **Combustion**: Flame structure and alternative fuel transitions.
- **Data Analysis**: Interpreting complex physical phenomena through simulation.


<br>
## Current Projects

### The Asymptotic State of Decaying Turbulence
The long-time evolution of decaying homogeneous turbulence remains a fundamental challenge in fluid dynamics. My current work utilizes a comprehensive suite of DNS to investigate this problem. We initialize the energy spectrum using both the Birkhoff-Saffman (BS) form (with $E(k)\sim k^2$ for small $k$) and the Loitsianskii-Kolmogorov-Batchelor (LKB) form (with $E(k)\sim k^4$ for small $k$). 

By extending simulations to unprecedented durations—on the order of 200,000 initial eddy-turnover times—we have observed an unambiguous power-law decay ($E_n\sim t^{-n}$) for both cases. These findings provide critical empirical benchmarks for the recent theory of decaying turbulence developed by Migdal.


## Publications
**Rodhiya, A.**, Bhattacharya, S., & Verma, M. K. (2025). [Relative accuracy of turbulence simulations using pseudo-spectral and finite difference solvers](https://arxiv.org/abs/2508.10808), Sādhanā (in press)

**Rodhiya, A.**, Gruber, A., Bothien, M. R., Chen, J. H., & Aditya, K. (2024). [Spontaneous ignition and flame propagation in hydrogen/methane wrinkled laminar flames at reheat conditions: Effect of pressure and hydrogen fraction](https://www.sciencedirect.com/science/article/abs/pii/S0010218024004048), Combustion and Flame, 269, 113695.

Jonnalagadda, A., Kulkarni, S.,** Rodhiya, A.**, Kolla, H., & Aditya, K. (2023). [A co-kurtosis based dimensionality reduction method for combustion datasets](https://www.sciencedirect.com/science/article/abs/pii/S0010218023000202), Combustion and Flame, 250, 112635.

**Rodhiya, A.**, Aditya, K., Gruber, A., & Chen, J. H. (2021). [Simulations of flame structure in a reheat burner: pressure scaling](https://arc.aiaa.org/doi/abs/10.2514/6.2021-3448). In AIAA Propulsion and Energy 2021 Forum (p. 3448).

## Selected Talks
### 78th Annual Meeting of the Division of Fluid Dynamics, Nov 2025
[**Rodhiya, A.**, Sajeev, S., Donzis, D. A., Keyes, D. E., & Sreenivasan, K. R. (2025)](https://archive.aps.org/dfd/2025/k27/12/). The Asymptotic State of Decaying Turbulence. Bulletin of the American Physical Society, 66.

### 74th Annual Meeting of the Division of Fluid Dynamics, Nov 2021
[**Rodhiya, A.**, Gruber, A., Chen, J.,& Aditya, K. (2021)](https://meetings.aps.org/Meeting/DFD21/Session/M09.10). Effect of fuel-blend ratio in methane-hydrogen reheat flames. Bulletin of the American Physical Society, 66.

### 73th Annual Meeting of the Division of Fluid Dynamics, Nov 2020
[**Rodhiya, A.**, Aditya, K., Gruber, A., & Chen, J. (2020).](https://ui.adsabs.harvard.edu/abs/2020APS..DFDP03004R/abstract). Effect of fuel-blend ratio in methane-hydrogen reheat flames. Bulletin of the American Physical Society, 66.


## Past Projects
### Relative accuracy  of turbulence simulations using pseudo-spectral and finite difference solvers
While spectral solvers are theoretically more accurate for a single timestep, our research demonstrated that both methods yield nearly identical results for long-term turbulence simulations. By simulating forced hydrodynamic turbulence on a $256^3$ grid across a range of Reynolds numbers ($965$ to $1994$), we showed that the total energy, flow profiles, and energy flux remained consistent. We propose that within a turbulence attractor, numerical errors tend to cancel out rather than accumulate, leading to converged results across different numerical schemes.

### Effect of fuel-blend ratio in methane-hydrogen reheat flames 
To facilitate the transition to carbon-neutral fuels in gas turbines, We investigated the combustion characteristics of various $CH_4-H_2$ blends. Using 2D simulations of a reheat burner at 5 bar, I analyzed three fuel-blend ratios ($0.5:0.5$, $0.3:0.7$, and pure $H_2$ by volume) to understand how hydrogen concentration shifts flame structure and stability.

### Pressure scaling of reheat flame structure
This project utilized DNS to explore the effects of pressure (1, 5, and 10 bar) on reheat flame structures. I employed Chemical Explosive Mode Analysis (CEMA) to quantify the distribution of fuel consumption rates across different combustion modes, providing insights into how high-pressure environments alter chemical heat release.

### Engineering Design & Prototyping
- **Thermal Energy Storage**: Designed a PCM-based battery storage system. I utilized STAR CCM+ to optimize heat exchanger geometry and validated the design using a custom experimental setup.
- **Laser Cooling Systems**: Developed a high-efficiency vapor chamber and pin-fin heat sink for air-cooling lasers, optimizing for strict dimensional and heat flux constraints.
- **Sustainable Engineering**: Developed a gym-powered Reverse Osmosis (RO) purifier that utilizes mechanical energy from exercise equipment to drive the filtration process.





---
<p style="font-size:11px">Page template forked from <a href="https://github.com/evanca/quick-portfolio">evanca</a></p>
<!-- Remove above link if you don't want to attibute -->
