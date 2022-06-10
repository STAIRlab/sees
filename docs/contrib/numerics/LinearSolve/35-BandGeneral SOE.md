# BandGeneral SOE

<p>This command is used to construct a BandGeneralSOE linear system of
equation object. As the name implies, this class is used for matrix
systems which have a banded profile. The matrix is stored as shown below
in a 1dimensional array of size equal to the bandwidth times the number
of unknowns. When a solution is required, the Lapack routines DGBSV and
SGBTRS are used. The following command is used to construct such a
system:</p>

```tcl
system BandGeneral
```

<hr />

<p>NOTES:</p>
<hr />

<p>THEORY:</p>
<p>An <em>n</em>&times;<em>n</em> matrix
<em>A</em>=(<em>a</em><sub><em>i,j</em> </sub>) is a
<strong>band matrix</strong> if all matrix elements are zero outside a
diagonally bordered band whose range is determined by constants
<em>k</em><sub>1</sub> and
<em>k</em><sub>2</sub>:</p>
<dl>
<dt></dt>
<dd>

$$a_{i,j}=0 \quad\mbox{if}\quad j<i-k_1 \quad\mbox{ or
}\quad j>i+k_2; \quad k_1, k_2 \ge 0.\,$$

</dd>
</dl>
<p>The quantities <em>k</em><sub>1</sub> and
<em>k</em><sub>2</sub> are the <em>left</em> and
<em>right</em> <em>half-bandwidth</em>, respectively. The
<em>bandwidth</em> of the matrix is
<em>k</em><sub>1</sub>&nbsp;+&nbsp;<em>k</em><sub>2</sub>&nbsp;+&nbsp;1
(in other words, the smallest number of adjacent diagonals to which the
non-zero elements are confined).</p>
<p>and matrices are usually stored by storing the diagonals in the band;
the rest is implicitly zero.</p>

<p>For example, 6-by-6 a matrix with bandwidth 3:</p>

$$
\begin{bmatrix} B_{11} & B_{12} & 0 & \cdots & \cdots
& 0 \\ B_{21} & B_{22} & B_{23} & \ddots & \ddots
& \vdots \\ 0 & B_{32} & B_{33} & B_{34} & \ddots
& \vdots \\ \vdots & \ddots & B_{43} & B_{44} &
B_{45} & 0 \\ \vdots & \ddots & \ddots & B_{54} &
B_{55} & B_{56} \\ 0 & \cdots & \cdots & 0 & B_{65}
& B_{66} \end{bmatrix} 
$$

is stored as the 6-by-3 matrix

$$
\begin{bmatrix} 0 & B_{11} & B_{12}\\ B_{21} & B_{22}
& B_{23} \\ B_{32} & B_{33} & B_{34} \\ B_{43} & B_{44}
& B_{45} \\ B_{54} & B_{55} & B_{56} \\ B_{65} & B_{66}
& 0 \end{bmatrix}.
$$

<hr />

<p>Code Developed by: <span style="color:blue"> fmk</span></p>

