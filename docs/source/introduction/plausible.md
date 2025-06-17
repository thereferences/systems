# Project Plausibility

A solid basis is key.

## A Team's Key Business Questions

<ol class="numeric">
  <li class="numeric">Business Outcomes</li>
  <li class="numeric">An in-depth evaluation of knowledge & data understandings till date.</li>
  <li class="numeric">Outline key business questions, e.g.,
    <ul><li>Is it possible to continuously predict the probability of a hypoglycaemic attack amongst our intensive care unit patients?</li>
    <li>Is it possible to automatically warn intensive care unit colleagues if a patient is at risk of a hypoglycaemic incident within the next 6 hours?</li></ul>
  </li>
  <li class="numeric">Prioritise</li>
</ol>


<br>

<img src="../../../assets/W200128_TROYANOS_THEKEY-1200x1580.png" alt="priorities" width="60%" style="margin-left: 65px">

<br>

The _pipe dreams_ cell also addresses the question - do the capabilities to achieve an objective exist?


> If you don’t have the right CRM and tech infrastructure in place, you’ll be unable to put your model into play in the market, and your original question will end up as a pipe dream — its potential business impact is high, but your ability to realize this potential is effectively nonexistent. [^Tyranos]


Therefore, ``... cross-functional teams capable of translating insight into action'' are critical.

<br>
<br>


## Quantitative Prioritisation

Quantitative prioritisation can eliminate ...




<br>





<br>

```{mermaid}
%%{ init: { 'flowchart': { 'curve': 'monotoneX'} } }%%
flowchart LR    
    id0([start]) --> id1{<span title="Does the potential project have a budget?">budget</span>} 
    id1 -- yes --> id2{<span title="Is the budget, project timebox, and the collaboration commitment plausible?">budget,<br>time</span>}
    id1 -- no --> id3([terminate])
    id2 -- no --> id3
    id2 -- yes --> id5(<span title="The project scope/design details">project<br>details</span>)
    id5 --> id6{<span title="Is the potential project addressable via machine learning, technically feasible, and economically viable?">feasible?</span>}
    id6 -- no --> id3
    id6 -- yes --> id8(next <br> steps)
    
    classDef default fill:#333333,stroke:#333333,stroke-width:0px,color:#ffffff,font-size:11pt;
```

<br>

<figcaption>An illustration of considerations vis-à-vis a potential machine learning dependent project.  The project details 
inform the feasibility assessment.</figcaption>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

[^Tyranos]: [Use Data to Answer Your Key Business Questions](https://hbr.org/2020/02/use-data-to-answer-your-key-business-questions)
