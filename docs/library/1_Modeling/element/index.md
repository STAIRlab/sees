---
template: grid_index.html
...

# Element

<style>
.grid.cards>:-webkit-any(ul,ol) {
  display: contents !important;
}
ul {
  list-style-type: disc;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 40px;
}
.grid {
  grid-gap: .4rem;
  display: grid !important;
  grid-template-columns: repeat(auto-fit,minmax(16rem,1fr));
  margin: 1em 0;
}
.grid>.card {
  text-size-adjust: none;
  -webkit-font-smoothing: antialiased;
  font-feature-settings: "kern","liga";
  color: var(--md-typeset-color);
  font-family: var(--md-text-font-family);
  -webkit-print-color-adjust: exact;
  font-size: .8rem;
  line-height: 1.6;
  box-sizing: inherit;
  grid-gap: .4rem;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(16rem,1fr));
  margin: 1em 0;
}
.li {
    text-size-adjust: none;
  --md-text-font: "Roboto";
  --md-code-font: "Roboto Mono";
  -webkit-font-smoothing: antialiased;
  --md-text-font-family: var(--md-text-font,_),-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif;
  --md-code-font-family: var(--md-code-font,_),SFMono-Regular,Consolas,Menlo,monospace;
  font-feature-settings: "kern","liga";
  color: var(--md-typeset-color);
  font-family: var(--md-text-font-family);
  --md-default-fg-color: rgba(0,0,0,.87);
  --md-default-fg-color--light: rgba(0,0,0,.54);
  --md-default-fg-color--lighter: rgba(0,0,0,.32);
  --md-default-fg-color--lightest: rgba(0,0,0,.07);
  --md-default-bg-color: #fff;
  --md-default-bg-color--light: hsla(0,0%,100%,.7);
  --md-default-bg-color--lighter: hsla(0,0%,100%,.3);
  --md-default-bg-color--lightest: hsla(0,0%,100%,.12);
  --md-shadow-z1: 0 0.2rem 0.5rem rgba(0,0,0,.05),0 0 0.05rem rgba(0,0,0,.1);
  --md-shadow-z2: 0 0.2rem 0.5rem rgba(0,0,0,.1),0 0 0.05rem rgba(0,0,0,.25);
  --md-shadow-z3: 0 0.2rem 0.5rem rgba(0,0,0,.2),0 0 0.05rem rgba(0,0,0,.35);
  --md-typeset-table-sort-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m18 21-4-4h3V7h-3l4-4 4 4h-3v10h3M2 19v-2h10v2M2 13v-2h7v2M2 7V5h4v2H2Z"/></svg>');
  --md-typeset-table-sort-icon--asc: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 17h3l-4 4-4-4h3V3h2M2 17h10v2H2M6 5v2H2V5m0 6h7v2H2v-2Z"/></svg>');
  --md-typeset-table-sort-icon--desc: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 7h3l-4-4-4 4h3v14h2M2 17h10v2H2M6 5v2H2V5m0 6h7v2H2v-2Z"/></svg>');
  --md-toc-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 9h14V7H3v2m0 4h14v-2H3v2m0 4h14v-2H3v2m16 0h2v-2h-2v2m0-10v2h2V7h-2m0 6h2v-2h-2v2Z"/></svg>');
  --md-search-result-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h7c-.41-.25-.8-.56-1.14-.9-.33-.33-.61-.7-.86-1.1H6V4h7v5h5v1.18c.71.16 1.39.43 2 .82V8l-6-6m6.31 16.9c1.33-2.11.69-4.9-1.4-6.22-2.11-1.33-4.91-.68-6.22 1.4-1.34 2.11-.69 4.89 1.4 6.22 1.46.93 3.32.93 4.79.02L22 23.39 23.39 22l-3.08-3.1m-3.81.1a2.5 2.5 0 0 1-2.5-2.5 2.5 2.5 0 0 1 2.5-2.5 2.5 2.5 0 0 1 2.5 2.5 2.5 2.5 0 0 1-2.5 2.5Z"/></svg>');
  --md-source-forks-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M5 3.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0zm0 2.122a2.25 2.25 0 1 0-1.5 0v.878A2.25 2.25 0 0 0 5.75 8.5h1.5v2.128a2.251 2.251 0 1 0 1.5 0V8.5h1.5a2.25 2.25 0 0 0 2.25-2.25v-.878a2.25 2.25 0 1 0-1.5 0v.878a.75.75 0 0 1-.75.75h-4.5A.75.75 0 0 1 5 6.25v-.878zm3.75 7.378a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0zm3-8.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5z"/></svg>');
  --md-source-repositories-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 1 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 0 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 0 1 1-1h8zM5 12.25v3.25a.25.25 0 0 0 .4.2l1.45-1.087a.25.25 0 0 1 .3 0L8.6 15.7a.25.25 0 0 0 .4-.2v-3.25a.25.25 0 0 0-.25-.25h-3.5a.25.25 0 0 0-.25.25z"/></svg>');
  --md-source-stars-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.75.75 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694v.001z"/></svg>');
  --md-source-version-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2.5 7.775V2.75a.25.25 0 0 1 .25-.25h5.025a.25.25 0 0 1 .177.073l6.25 6.25a.25.25 0 0 1 0 .354l-5.025 5.025a.25.25 0 0 1-.354 0l-6.25-6.25a.25.25 0 0 1-.073-.177zm-1.5 0V2.75C1 1.784 1.784 1 2.75 1h5.025c.464 0 .91.184 1.238.513l6.25 6.25a1.75 1.75 0 0 1 0 2.474l-5.026 5.026a1.75 1.75 0 0 1-2.474 0l-6.25-6.25A1.75 1.75 0 0 1 1 7.775zM6 5a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/></svg>');
  --md-tag-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m5.41 21 .71-4h-4l.35-2h4l1.06-6h-4l.35-2h4l.71-4h2l-.71 4h6l.71-4h2l-.71 4h4l-.35 2h-4l-1.06 6h4l-.35 2h-4l-.71 4h-2l.71-4h-6l-.71 4h-2M9.53 9l-1.06 6h6l1.06-6h-6Z"/></svg>');
  --md-tooltip-width: 20rem;
  --md-version-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512"><!--! Font Awesome Free 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc.--><path d="m310.6 246.6-127.1 128c-7.1 6.3-15.3 9.4-23.5 9.4s-16.38-3.125-22.63-9.375l-127.1-128C.224 237.5-2.516 223.7 2.438 211.8S19.07 192 32 192h255.1c12.94 0 24.62 7.781 29.58 19.75s3.12 25.75-6.08 34.85z"/></svg>');
  --md-footnotes-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 7v4H5.83l3.58-3.59L8 6l-6 6 6 6 1.41-1.42L5.83 13H21V7h-2Z"/></svg>');
  --md-details-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M8.59 16.58 13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.42Z"/></svg>');
  --md-tasklist-icon: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M1 12C1 5.925 5.925 1 12 1s11 4.925 11 11-4.925 11-11 11S1 18.075 1 12zm16.28-2.72a.75.75 0 0 0-1.06-1.06l-5.97 5.97-2.47-2.47a.75.75 0 0 0-1.06 1.06l3 3a.75.75 0 0 0 1.06 0l6.5-6.5z"/></svg>');
  --md-tasklist-icon--checked: url('data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M1 12C1 5.925 5.925 1 12 1s11 4.925 11 11-4.925 11-11 11S1 18.075 1 12zm16.28-2.72a.75.75 0 0 0-1.06-1.06l-5.97 5.97-2.47-2.47a.75.75 0 0 0-1.06 1.06l3 3a.75.75 0 0 0 1.06 0l6.5-6.5z"/></svg>');
  --md-accent-fg-color: #526cfe;
  --md-accent-fg-color--transparent: rgba(82,108,254,.1);
  --md-accent-bg-color: #fff;
  --md-accent-bg-color--light: hsla(0,0%,100%,.7);
  --md-primary-fg-color: #4051b5;
  --md-primary-fg-color--light: #5d6cc0;
  --md-primary-fg-color--dark: #303fa1;
  --md-primary-bg-color: #fff;
  --md-primary-bg-color--light: hsla(0,0%,100%,.7);
  --md-code-fg-color: #36464e;
  --md-code-bg-color: #f5f5f5;
  --md-code-hl-color: rgba(255,255,0,.5);
  --md-code-hl-number-color: #d52a2a;
  --md-code-hl-special-color: #db1457;
  --md-code-hl-function-color: #a846b9;
  --md-code-hl-constant-color: #6e59d9;
  --md-code-hl-keyword-color: #3f6ec6;
  --md-code-hl-string-color: #1c7d4d;
  --md-code-hl-name-color: var(--md-code-fg-color);
  --md-code-hl-operator-color: var(--md-default-fg-color--light);
  --md-code-hl-punctuation-color: var(--md-default-fg-color--light);
  --md-code-hl-comment-color: var(--md-default-fg-color--light);
  --md-code-hl-generic-color: var(--md-default-fg-color--light);
  --md-code-hl-variable-color: var(--md-default-fg-color--light);
  --md-typeset-color: var(--md-default-fg-color);
  --md-typeset-a-color: var(--md-primary-fg-color);
  --md-typeset-mark-color: rgba(255,255,0,.5);
  --md-typeset-del-color: rgba(245,80,61,.15);
  --md-typeset-ins-color: rgba(11,213,112,.15);
  --md-typeset-kbd-color: #fafafa;
  --md-typeset-kbd-accent-color: #fff;
  --md-typeset-kbd-border-color: #b8b8b8;
  --md-typeset-table-color: rgba(0,0,0,.12);
  --md-admonition-fg-color: var(--md-default-fg-color);
  --md-admonition-bg-color: var(--md-default-bg-color);
  --md-footer-fg-color: #fff;
  --md-footer-fg-color--light: hsla(0,0%,100%,.7);
  --md-footer-fg-color--lighter: hsla(0,0%,100%,.3);
  --md-footer-bg-color: rgba(0,0,0,.87);
  --md-footer-bg-color--dark: rgba(0,0,0,.32);
  --md-mermaid-font-family: var(--md-text-font-family),sans-serif;
  --md-mermaid-edge-color: var(--md-code-fg-color);
  --md-mermaid-node-bg-color: var(--md-accent-fg-color--transparent);
  --md-mermaid-node-fg-color: var(--md-accent-fg-color);
  --md-mermaid-label-bg-color: var(--md-default-bg-color);
  --md-mermaid-label-fg-color: var(--md-code-fg-color);
  -webkit-print-color-adjust: exact;
  font-size: .8rem;
  line-height: 1.6;
  list-style-type: disc;
  box-sizing: inherit;
  border: .05rem solid var(--md-default-fg-color--lightest);
  border-radius: .1rem;
  display: block;
  margin: 0;
  padding: .8rem;
  transition: border .25s,box-shadow .25s;
}
</style>





<div class="grid cards"><ul>

<li> <p><span class="twemoji lg middle">
</span> <strong>Beams and Columns</strong></p> <hr> 
<p>...</p><p>
<a href="beam"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> beams</a></p>
</li> 

<li><p><span class="twemoji lg middle">
</span>
<strong>Cables and Trusses</strong></p> <hr>
<p>...</p> <p><a href="truss/"><span class="twemoji">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> Reference</a></p> 
</li> 

<li> <p>
<strong>Quadrilaterals</strong></p> <hr> <p>Quadrilaterals</p> <p><a href="quadrilateral/">
<span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> Quadrilaterals</a></p> 
</li> 

<li> <p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 3c-1.27 0-2.4.8-2.82 2H3v2h1.95L2 14c-.47 2 1 3 3.5 3s4.06-1 3.5-3L6.05 7h3.12c.33.85.98 1.5 1.83 1.83V20H2v2h20v-2h-9V8.82c.85-.32 1.5-.97 1.82-1.82h3.13L15 14c-.47 2 1 3 3.5 3s4.06-1 3.5-3l-2.95-7H21V5h-6.17C14.4 3.8 13.27 3 12 3m0 2a1 1 0 0 1 1 1 1 1 0 0 1-1 1 1 1 0 0 1-1-1 1 1 0 0 1 1-1m-6.5 5.25L7 14H4l1.5-3.75m13 0L20 14h-3l1.5-3.75Z"></path></svg></span>
<strong>Triangle</strong></p> <hr> <p>...</p> <p><a href="triangle"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> Triangles</a></p> 
</li> 
</ul> </div>



<hr />

<ul>
<li>Truss Elements
 <ul>
  <li><a href="Truss" >Truss</a> - Basic 2D/3D truss</li>
  <li><a href="Truss2" >Truss2</a> - Truss element for concrete walls</li>
  <li><a href="Corotational_Truss" >CorotTruss</a> - Corotational truss element</li>
 </ul>
</li>

<li>Beam-Column Elements
 <ul>
 <li><a href="ElasticBeamColumn" >Elastic Beam Column</a></li>
 <li><a href="ModElasticBeamColumn"
 >Elastic Beam Column Element with Stiffness
 Modifiers</a></li>
 <li><a href="Elastic_Timoshenko_Beam_Column"
 >Elastic Timoshenko Beam Column Element</a></li>
 <li><a href="Beam_With_Hinges" >Beam With Hinges
 Element</a></li>
 
 <li><a href="Displacement-Based_Beam-Column"
 >Displacement-Based Beam-Column Element</a></li>
 
 <li><a href="Force-Based_Beam-Column"
 >Force-Based Beam-Column Element</a></li>
 
 <li><a
 href="Flexure-Shear_Interaction_Displacement-Based_Beam-Column"
 >Flexure-Shear Interaction Displacement-Based Beam-Column Element</a></li>
 
 <li><a href="MVLEM">MVLEM</a> - Multiple-Vertical-Line-Element-Model for flexure dominated RC Walls</li>
 
 <li><a href="SFI_MVLEM">SFI_MVLEM</a> - Cyclic shear-flexure interaction model for RC walls</li>

 </ul>

<li>Zero-Length Elements
<ul>
<li><a href="zeroLength" >zeroLength</a></li>

<li><a href="zeroLengthND" >zeroLengthND</a></li>

<li><a href="zeroLengthSection">zeroLengthSection Element</a></li>

<li><a href="CoupledZeroLength">CoupledZeroLength</a></li>

<li><a href="zeroLengthContact">zeroLengthContact</a></li>

<li><a href="zeroLengthContactNTS2D">zeroLengthContactNTS2D</a></li>

<li><a href="zeroLengthInterface2D">zeroLengthInterface2D</a></li>

<li><a href="zeroLengthImpact3D">zeroLengthImpact3D</a></li>
</ul></li>


<li>Joint Elements
<ul>
<li><a href="BeamColumnJoint" >BeamColumnJoint
Element</a></li>
<li><a href="ElasticTubularJoint"
>ElasticTubularJoint Element</a></li>
<li><a href="Joint2D" >Joint2D Element</a></li>
</ul></li>
</ul>
<ul>
<li>Link Elements
<ul>
<li><a href="Two_Node_Link" >Two Node Link Element</a></li>
</ul></li>

<li>Bearing Elements
<ul>
<li><a href="Elastomeric_Bearing_(Plasticity)">elastomericBearingPlasticity</a>Elastomeric Bearing (Plasticity)</li>
<li><a href="Elastomeric_Bearing_(Bouc-Wen)">elastomericBearingBoucWen </a>Elastomeric Bearing (Bouc-Wen)</li>
<li><a href="Flat_Slider_Bearing" >Flat Slider Bearing</a></li>

<li><a href="Single_Friction_Pendulum_Bearing">Single Friction Pendulum Bearing</a></li>

<li><a href="Triple_Friction_Pendulum_Bearing" >TFP</a>Triple Friction Pendulum Bearing</li>
<li><a href="Triple_Friction_Pendulum" >TripleFrictionPendulum</a></li>

<li><a href="MultipleShearSpring">MultipleShearSpring</a></li>

<li><a href="KikuchiBearing" >KikuchiBearing</a></li>

<li><a href="YamamotoBiaxialHDR">YamamotoBiaxialHDR Element</a></li>
<li><a href="ElastomericX" >ElastomericX</a></li>
<li><a href="LeadRubberX" >LeadRubberX</a></li>
<li><a href="HDR" >HDR</a> high damping rubber bearing (3D)</li>
<li><a href="RJ-Watson_EQS_Bearing" >RJWatsonEqsBearing</a> RJ-Watson EQS Bearing Element</li>
<li><a href="FPBearingPTV" >FPBearingPTV</a></li>
</ul></li>

<li>Quadrilateral Elements
<ul>
<li><a href="Quad" >Quad Element</a></li>
<li><a href="Shell" >Shell Element</a></li>
<li><a href="ShellDKGQ" >ShellDKGQ</a></li>
<li><a href="ShellNLDKGQ" >ShellNLDKGQ</a></li>
<li><a href="ShellNL" >ShellNL</a></li>
<li><a href="Bbar_Plane_Strain_Quadrilateral" >Bbar Plane Strain Quadrilateral Element</a></li>
<li><a href="Enhanced_Strain_Quadrilateral" >Enhanced Strain Quadrilateral Element</a></li>
<li><a href="SSPquad" >SSPquad Element</a></li>
</ul></li>

<li>Triangular Elements
<ul>
<li><a href="Tri31" >Tri31 Element</a></li>
<li><a href="ShellDKGT" >ShellDKGT</a></li>
<li><a href="ShellNLDKGT" >ShellNLDKGT</a></li>
</ul></li>

<li>Brick Elements
<ul>
<li><a href="Standard_Brick" >Standard Brick</a></li>
<li><a href="Bbar_Brick" >Bbar Brick</a></li>
<li><a href="http://opensees.berkeley.edu/OpenSees/manuals/usermanual/734.htm">Twenty Node Brick</a></li>
<li><a href="Twenty_Seven_Node_Brick" >Twenty Seven Node Brick</a></li>
<li><a href="SSPbrick" >SSPbrick</a></li>
</ul></li>

<li>Tetrahedron Elements
<ul>
<li><a href="FourNodeTetrahedron" >FourNodeTetrahedron</a></li>
</ul></li>


<li>u-p Elements
<ul>
<li>UC San Diego u-p element (saturated soil)
<ul>
<li><a href="Four_Node_Quad_u-p" >Four Node Quad u-p</a></li>
<li><a href="Brick_u-p" >Brick u-p</a></li>
<li><a href="bbarQuad_u-p" >bbarQuad u-p</a></li>
<li><a href="bbarBrick_u-p" >bbarBrick u-p</a></li>
<li><a href="Nine_Four_Node_Quad_u-p" >Nine Four Node Quad u-p</a></li>
<li><a href="Twenty_Eight_Node_Brick_u-p">Twenty Eight Node Brick u-p</a></li>
</ul></li>

<li><a href="Twenty_Node_Brick_u-p" >Twenty Node Brick u-p</a></li>
<li><a href="Brick_Large_Displacement_u-p">Brick Large Displacement u-p</a></li>
<li><a href="SSPquadUP" >SSPquadUP</a></li>
<li><a href="SSPbrickUP" >SSPbrickUP</a></li>
</ul></li>

<li>Contact Elements
<ul>
<li><a href="SimpleContact2D" >SimpleContact2D</a></li>
<li><a href="SimpleContact3D" >SimpleContact3D</a></li>
<li><a href="BeamContact2D" >BeamContact2D</a></li>
<li><a href="BeamContact3D" >BeamContact3D</a></li>
<li><a href="BeamEndContact3D" >BeamEndContact3D</a></li>
<li><a href="zeroLengthImpact3D">zeroLengthImpact3D</a></li>
</ul></li>


<li>Cable Elements
<ul>
<li><a href="CatenaryCableElement" >CatenaryCable
</a></li>
</ul></li>

<li>Misc.
<ul>
<li><a href="ShallowFoundationGen"
>ShallowFoundationGen</a></li>
<li><a href="SurfaceLoad" >SurfaceLoad
Element</a></li>
<li><a href="VS3D4" >VS3D4</a></li>
<li><a href="AC3D8" >AC3D8</a></li>
<li><a href="ASI3D8" >ASI3D8</a></li>
<li><a href="AV3D4" >AV3D4</a></li>
</ul></li>
</ul>
