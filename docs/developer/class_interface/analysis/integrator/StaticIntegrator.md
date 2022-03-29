\
# StaticIntegrator 

```cpp
#include <analysis/integrator/StaticIntegrator.h>
```

class StaticIntegrator: public Integrator\

MovableObject\
Integrator\
IncrementalIntegrator\

LoadControl\
ArcLength\
DisplacementControl\

StaticIntegrator is an abstract class. It is a subclass of
IncrementalIntegrator provided to implement the common methods among
integrator classes used in performing a static analysis on the FE_Model.
The StaticIntegrator class provides an implementation of the methods to
form the FE_Element and DOF_Group contributions to the tangent and
residual. A pure virtual method `newStep()` is also defined in the
interface, this is the method first called at each iteration in a static
analysis, see the StaticAnalysis class.
In static nonlinear finite element problems we seek a solution ($\U$,
$\lambda$) to the nonlinear vector function

$$\R(\U, \lambda) = \lambda {\bf P} - {\bf F}_R(\U) = \zero
\label{staticGenForm}$$

The most widely used technique for solving the non-linear finite element
equation, equation [\[femGenForm\]](#femGenForm){reference-type="ref"
reference="femGenForm"}, is to use an incremental scheme. In the
incremental formulation, a solution to the equation is sought at
successive incremental steps.

$$\R({\bf U}_{n}, \lambda_n) = \lambda_n {\bf P} - {\bf F}_R({\bf U}_{n})
\label{staticIncForm}$$

The solution of this equation is typically obtained using an iterative
procedure, in which a sequence of approximations (${\bf U}_{n}^{(i)}$,
$\lambda_n^{(i)}$), $i=1,2, ..$ is obtained which converges to the
solution (${\bf U}_n$, $\lambda_n)$. The most frequently used iterative
schemes, such as Newton-Raphson, modified Newton, and quasi Newton
schemes, are based on a Taylor expansion of
equation [\[staticIncForm\]](#staticIncForm){reference-type="ref"
reference="staticIncForm"} about (${\bf U}_{n}$, $\lambda_n$):

$$\R({\bf U}_{n},\lambda_n) = \lambda_n^{(i)} {\bf P} 
 - {\bf F}_{R}\left({\bf U}_{n}^{(i)} \right) - \left[
\begin{array}{cc}
{\bf K}_n^{(i)} & -{\bf P} \\
\end{array} \right] 
\left\{
\begin{array}{c}
{\bf U}_{n} - {\bf U}_{n}^{(i)}  \\ 
\lambda_n - \lambda_n^{(i)} 
\end{array} \right\}
\label{staticFormTaylor}$$

which a system of of $N$ equations with ($N+1$) unknowns. Two solve
this, an additional equation is required, the constraint equation. The
constraint equation used depends on the static integration scheme, of
which there are a number, for example load control, arc length, and
displacement control.

### Constructors

\
### Destructor

\
// Public Methods\

\

\

\

The integer *classTag* is passed to the IncrementalIntegrator classes
constructor.

\
Does nothing. Provided so that the subclasses destructors will be
called.

\
To form the tangent matrix of the FE_Element, *theEle*, is instructed to
zero this matrix and then add it's $K$ matrix to the tangent, i.e. it
performs the following:

::: {.tabbing}
while ̄ while w̄hile ̄ theEle-$>$zeroTang()\
theEle-$>$addKtoTang()
:::

The method returns $0$.

```{.cpp}
virtual int formEleResidual(FE_Element \*theEle);
```

To form the residual vector of the FE_Element, *theEle*, is instructed
to zero the vector and then add it's $R$ vector to the residual, i.e. it
performs the following:

::: {.tabbing}
while ̄ while w̄hile ̄ theEle-$>$zeroResidual()\
theEle-$>$addRtoResid()
:::

The method returns $0$.

```{.cpp}
virtual int formNodTangent(DOF_Group \*theDof);
```

This should never be called in a static analysis. An error message is
printed if it is. Returns -1.

```{.cpp}
virtual int formNodUnbalance(DOF_Group \*theDof);
```

To form the unbalance vector of the DOF_Group, *theDof*, is instructed
to zero the vector and then add it's $P$ vector to the unbalance, i.e.
it performs the following:

::: {.tabbing}
while ̄ while w̄hile ̄ theDof-$>$zeroUnbalance()\
theDof-$>$addPtoUnbal()
:::

The method returns $0$.
