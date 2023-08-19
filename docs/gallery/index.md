---
template: grid_index.html
...

# Gallery

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
</span> <strong>Basic Structures</strong></p> <hr> 
<p>description here</p> <p>
<a href="skeletal"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> skeletal</a></p>
</li> 

<li><p><span class="twemoji lg middle">
<!--
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512">
-->
  <!-- Font Awesome Free 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2022 Fonticons, Inc.-->
<!--
  <path d="M593.8 59.1H46.2C20.7 59.1 0 79.8 0 105.2v301.5c0 25.5 20.7 46.2 46.2 46.2h547.7c25.5 0 46.2-20.7 46.1-46.1V105.2c0-25.4-20.7-46.1-46.2-46.1zM338.5 360.6H277v-120l-61.5 76.9-61.5-76.9v120H92.3V151.4h61.5l61.5 76.9 61.5-76.9h61.5v209.2zm135.3 3.1L381.5 256H443V151.4h61.5V256H566z"></path></svg>
-->
</span>
<strong>Components Studies</strong></p> <hr>
<p>cross-section analysis, uniaxial materials and more.</p> <p><a href="components/"><span class="twemoji">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> Reference</a></p> 
</li> 

<li> <p>
<!--
<span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17 8h3v12h1v1h-4v-1h1v-3h-4l-1.5 3H14v1h-4v-1h1l6-12m1 1-3.5 7H18V9M5 3h5c1.11 0 2 .89 2 2v11H9v-5H6v5H3V5c0-1.11.89-2 2-2m1 2v4h3V5H6Z"></path></svg></span> 
-->
<strong>Geotech</strong></p> <hr> <p>Soil models and geotechnical modeling techniques</p> <p><a href="geotech/">
<span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> Geotech</a></p> 
</li> 

<li> 
<p><span class="twemoji lg middle"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 3c-1.27 0-2.4.8-2.82 2H3v2h1.95L2 14c-.47 2 1 3 3.5 3s4.06-1 3.5-3L6.05 7h3.12c.33.85.98 1.5 1.83 1.83V20H2v2h20v-2h-9V8.82c.85-.32 1.5-.97 1.82-1.82h3.13L15 14c-.47 2 1 3 3.5 3s4.06-1 3.5-3l-2.95-7H21V5h-6.17C14.4 3.8 13.27 3 12 3m0 2a1 1 0 0 1 1 1 1 1 0 0 1-1 1 1 1 0 0 1-1-1 1 1 0 0 1 1-1m-6.5 5.25L7 14H4l1.5-3.75m13 0L20 14h-3l1.5-3.75Z"></path></svg></span>
<strong>Continua</strong></p> <hr> 
<p>Continuum mechanics.
<p><a href="../../license/"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M13.22 19.03a.75.75 0 0 0 1.06 0l6.25-6.25a.75.75 0 0 0 0-1.06l-6.25-6.25a.75.75 0 1 0-1.06 1.06l4.97 4.97H3.75a.75.75 0 0 0 0 1.5h14.44l-4.97 4.97a.75.75 0 0 0 0 1.06z"></path></svg>
</span> License</a></p> 
</li> 
</ul> </div>

