# ProfileSPD SOE

<p>This command is used to construct a profileSPDSOE linear system of
equation object. As the name implies, this class is used for symmetric
positive definite matrix systems. The matrix is stored as shown below in
a 1 dimensional array with only those values below the first non-zero
row in any column being stored. This is sometimes also referred to as a
skyline storage scheme. The following command is used to construct such
a system:</p>

```tcl
system ProfileSPD
```
<hr />
<p>THEORY:</p>
<p>An <em>n</em>&amp;times;<em>n</em> matrix
<em>A</em>=(<em>a</em>&lt;sub&gt;<em>i,j</em> &lt;/sub&gt;) is a
<strong>symmmetric postive definite matrix</strong> if:</p>
<dl>
<dt></dt>
<dd>

$$a_{i,j} = a_{j,i}\,$$

</dd>
</dl>

$$ y^T A y != 0 \,&lt;/math&gt; for all non-zero vectors
<em>y</em> with real entries ($y \in
\mathbb{R}^n$.
</dd>
</dl>
<p>In the skyline or profile storage scheme only the entries below the
first no-zero row entry in any column are stored if storing by rows: The
reason for this is that as no reordering of the rows is required in
gaussian eleimination because the matrix is SPD, no non-zero entries
will ocur in the elimination process outside the area stored.</p>
<p>For example, a symmetric 6-by-6 matrix with a structura as shown
below:</p>

$$
</dd>
</dl>
<p>\begin{bmatrix} A_{11} &amp; A_{12} &amp; 0 &amp; 0 &amp; 0 \\ &amp;
A_{22} &amp; A_{23} &amp; 0 &amp; A_{25} \\ &amp; &amp; A_{33} &amp; 0
&amp; 0 \\ &amp; &amp; &amp; A_{44} &amp; A_{45} \\ &amp; sym &amp;
&amp; &amp; A_{55} \end{bmatrix}. &lt;/math&gt;</p>
<p>The matrix is stored as 1-d array</p>

$$
</dd>
</dl>
<p>\begin{bmatrix} A_{11} &amp; A_{12} &amp; A_{22} &amp; A_{23} &amp;
A_{33} &amp; A_{44} &amp; A_{25} &amp; 0 &amp; A_{45} &amp; A_{55}
\end{bmatrix}. &lt;/math&gt;</p>
<p>with a further array containing indices of diagonal elements:</p>

$$
</dd>
</dl>
<p>\begin{bmatrix} 1 &amp; 3 &amp; 5 &amp; 6 &amp; 10 \end{bmatrix}.
&lt;/math&gt;</p>
<hr />
<p>Code Developed by: <span style="color:blue"> fmk
</span></p>
