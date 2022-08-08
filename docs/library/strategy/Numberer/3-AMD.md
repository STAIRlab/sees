# AMD Numberer

This option is used to select the AMD degree-of-freedom numbering
algorithm to provide the mapping between the degrees-of-freedom at the
nodes and the equation numbers. An AMD numberer uses the approximate
minimum degree scheme to order the matrix equations. 

The Tcl command to construct an AMD numberer is a follows:

```tcl
numberer AMD
```


## References

- Algorithm 837: AMD, An approximate minimum degree ordering
  algorithm, P. Amestoy, T. A. Davis, and I. S. Duff, ACM Transactions on
  Mathematical Software, vol 30, no. 3, Sept. 2004, pp. 381-388.

- An approximate minimum degree ordering algorithm, P. Amestoy, T. A.
  Davis, and I. S. Duff, SIAM Journal on Matrix Analysis and Applications,
  vol 17, no. 4, pp. 886-905, Dec. 1996.
  [online](https://people.engr.tamu.edu/davis/publications_files/An_Approximate_Minimum_Degree_Ordering_Algorithm.pdf)

- Direct Methods for Sparse Linear Systems, T. A. Davis, SIAM,
  Philadelphia, Sept. 2006. Part of the SIAM Book Series on the
  Fundamentals of Algorithms.

-----------------------------------------------------------------------
<p>Code developed by: <span style="color:blue"> fmk
</span></p>
