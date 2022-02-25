# OpenSees Python Bindings


## Documentation

<dl>
  <dt>building</dt>
  <dd>Run <code>elstir build</code> to build the documentation.</dd>

  <dt>publishing</dt>
  <dd><code>git subtree push --prefix site/ origin gh-pages</code>.</dd>

  <dt>developing</dt>
  <dd><code>elstir serve</code>.</dd>

  <dt>API documentation</dt>
  <dd>
   <code>for i in patch section...; do python tools/apidoc.py opensees.$i > docs/api/$i.md</code>.
  </dd>
</dl>




