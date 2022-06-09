# DegradingPinchedBW

- [User](https://github.com/GiacomoGr) University of Modena and Reggio Emilia
- Matteo Pelliciari, Phd (University of Modena and Reggio Emilia, Dept. of Engineering “Enzo Ferrari”, Modena)
- Professor Davide Lavorato (Roma Tre University, Dept. of Architecture, Rome).

|   Parameter       |  Role  |
|-------------------|--------------------------------------|
| $\alpha$          |  Ratio of linear to non-linear response  |
| $k$               |  Elastic stiffness  |
| $\beta_{0}$       |  Hysteresis shape control  |
| $\eta_{0}$        |  Hysteresis shape control  |
| $n$               |  Hysteresis shape control  |
| $\rho_{x}$        |  Max. displacement degradation  |
| $\rho_{\epsilon}$ |  Energy degradation  |
| $\delta_{k}$ |  Stiffness degradation  |
| $\delta_{f}$ |  Strength degradation  |
| $\psi$ |  Stiffness degradation rate control  |
| $\sigma$ |  Pinching width  |
| $u$ |  Pinching slope  |
| $\rho_{p}$ |  Pinching severity  |
| $\epsilon_{p}$ |  Pinching activation energy  |


     int    Tag,
     double p_m,
	   double p_Fy,
	   double p_xu,
	   double p_alpha,
	   double p_ko,
	   double p_n,
	   double p_eta,
	   double p_beta,
	   double p_rhoeps,
	   double p_rhox,
	   double p_phi,
	   double p_deltak,
	   double p_deltaf,
	   double p_sigma,
	   double p_u,
	   double p_epsp,
	   double p_rhop,
	   double ptolerance,
	   int pMaxNumIter)

- [https://github.com/OpenSees/OpenSees/pull/335](merge)

$$
\begin{aligned}
\dot{z} &=A\left(d_{i}\right) \dot{x}-\beta\left(d_{i}\right)\left(|\dot{x}||z|^{n-1} z+\eta_{0} \dot{x}|z|^{n}\right) \\
&=e^{-\delta_{k} d_{i} p_{k}\left(d_{i}\right)} \dot{x}-\beta_{0} e^{-\left[\delta_{k} p_{k}\left(d_{i}\right)-n \delta_{f}\right] d_{i}}\left(|\dot{x}||z|^{n-1} z+\eta_{0} \dot{x}|z|^{n}\right)
\end{aligned}
$$


## References

- “A degrading Bouc-Wen model for the hysteresis of reinforced concrete structural elements”, by Pelliciari M. et al. (Structure and Infrastructure Engineering, 2019, 1-14). https://doi.org/10.1080/15732479.2019.1674893

