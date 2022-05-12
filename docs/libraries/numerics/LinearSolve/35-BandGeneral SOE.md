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
<p>An <em>n</em>&amp;times;<em>n</em> matrix
<em>A</em>=(<em>a</em>&lt;sub&gt;<em>i,j</em> &lt;/sub&gt;) is a
<strong>band matrix</strong> if all matrix elements are zero outside a
diagonally bordered band whose range is determined by constants
<em>k</em>&lt;sub&gt;1&lt;/sub&gt; and
<em>k</em>&lt;sub&gt;2&lt;/sub&gt;:</p>
<dl>
<dt></dt>
<dd>

$$a_{i,j}=0 \quad\mbox{if}\quad j&lt;i-k_1 \quad\mbox{ or
}\quad j&gt;i+k_2; \quad k_1, k_2 \ge 0.\,$$

</dd>
</dl>
<p>The quantities <em>k</em>&lt;sub&gt;1&lt;/sub&gt; and
<em>k</em>&lt;sub&gt;2&lt;/sub&gt; are the <em>left</em> and
<em>right</em> <em>half-bandwidth</em>, respectively. The
<em>bandwidth</em> of the matrix is
<em>k</em>&lt;sub&gt;1&lt;/sub&gt;&amp;nbsp;+&amp;nbsp;<em>k</em>&lt;sub&gt;2&lt;/sub&gt;&amp;nbsp;+&amp;nbsp;1
(in other words, the smallest number of adjacent diagonals to which the
non-zero elements are confined).</p>
<p>and matrices are usually stored by storing the diagonals in the band;
the rest is implicitly zero.</p>
<p>For example, 6-by-6 a matrix with bandwidth 3:</p>

$$
</dd>
</dl>
<p>\begin{bmatrix} B_{11} &amp; B_{12} &amp; 0 &amp; \cdots &amp; \cdots
&amp; 0 \\ B_{21} &amp; B_{22} &amp; B_{23} &amp; \ddots &amp; \ddots
&amp; \vdots \\ 0 &amp; B_{32} &amp; B_{33} &amp; B_{34} &amp; \ddots
&amp; \vdots \\ \vdots &amp; \ddots &amp; B_{43} &amp; B_{44} &amp;
B_{45} &amp; 0 \\ \vdots &amp; \ddots &amp; \ddots &amp; B_{54} &amp;
B_{55} &amp; B_{56} \\ 0 &amp; \cdots &amp; \cdots &amp; 0 &amp; B_{65}
&amp; B_{66} \end{bmatrix} &lt;/math&gt; is stored as the 6-by-3
matrix</p>

$$
</dd>
</dl>
<p>\begin{bmatrix} 0 &amp; B_{11} &amp; B_{12}\\ B_{21} &amp; B_{22}
&amp; B_{23} \\ B_{32} &amp; B_{33} &amp; B_{34} \\ B_{43} &amp; B_{44}
&amp; B_{45} \\ B_{54} &amp; B_{55} &amp; B_{56} \\ B_{65} &amp; B_{66}
&amp; 0 \end{bmatrix}. &lt;/math&gt;</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
