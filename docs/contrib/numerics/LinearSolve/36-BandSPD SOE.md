# BandSPD SOE

<p>This command is used to construct a BandSPDSOE linear system of
equation object. As the name implies, this class is used for symmetric
positive definite matrix systems which have a banded profile. The matrix
is stored as shown below in a 1 dimensional array of size equal to the
(bandwidth/2) times the number of unknowns. When a solution is required,
the Lapack routines DPBSV and DPBTRS are used. The following command is
used to construct such a system:</p>

```tcl
system BandSPD
```
<hr />
<p>NOTES:</p>
<hr />
<p>THEORY:</p>
<p>An <em>n</em>&amp;times;<em>n</em> matrix
<em>A</em>=(<em>a</em>&lt;sub&gt;<em>i,j</em> &lt;/sub&gt;) is a
<strong>symmmetric banded matrix</strong> if all matrix elements are
zero outside a diagonally bordered band whose range is determined by
constants <em>k</em>:</p>
<dl>
<dt></dt>
<dd>

$$a_{i,j}=0 \quad\mbox{if}\quad j&lt;i-k \quad\mbox{ or }\quad
j&gt;i+k; \quad k \ge 0.\,$$

</dd>
</dl>
<dl>
<dt></dt>
<dd>

$$a_{i,j} = a_{j,i}\,$$

</dd>
</dl>

$$ y^T A y != 0 \,&lt;/math&gt; for all non-zero vectors
<em>y</em> with real entries ($y \in
\mathbb{R}^n$,
</dd>
</dl>
<p>The <em>bandwidth</em> of the matrix is
<em>k</em>&amp;nbsp;+&amp;nbsp;<em>k</em>&amp;nbsp;+&amp;nbsp;1.</p>
<p>For example, a symmetric 6-by-6 matrix with a right bandwidth of
2:</p>

$$
</dd>
</dl>
<p>\begin{bmatrix} A_{11} &amp; A_{12} &amp; A_{13} &amp; 0 &amp; \cdots
&amp; 0 \\ &amp; A_{22} &amp; A_{23} &amp; A_{24} &amp; \ddots &amp;
\vdots \\ &amp; &amp; A_{33} &amp; A_{34} &amp; A_{35} &amp; 0 \\ &amp;
&amp; &amp; A_{44} &amp; A_{45} &amp; A_{46} \\ &amp; sym &amp; &amp;
&amp; A_{55} &amp; A_{56} \\ &amp; &amp; &amp; &amp; &amp; A_{66}
\end{bmatrix}. &lt;/math&gt; This matrix is stored as the 6-by-3
matrix:</p>

$$
</dd>
</dl>
<p>\begin{bmatrix} A_{11} &amp; A_{12} &amp; A_{13} \\ A_{22} &amp;
A_{23} &amp; A_{24} \\ A_{33} &amp; A_{34} &amp; A_{35} \\ A_{44} &amp;
A_{45} &amp; A_{46} \\ A_{55} &amp; A_{56} &amp; 0 \\ A_{66} &amp; 0
&amp; 0 \end{bmatrix}. &lt;/math&gt;</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
