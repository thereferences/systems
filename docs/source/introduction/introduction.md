# Introduction

```{mermaid}
%%{ init: { 'flowchart': { 'curve': 'monotoneX'} } }%%
flowchart LR    
    id0([start]) --> id1{<span title="Does the potential project have a budget?">budget</span>} -- yes --> id2{plausible<br> budget &<br> time-box}
    id1 -- no --> id3([terminate])
    id2 -- no --> id4([terminate])
    id2 -- yes --> id5(<span title="The project scope/design details">design <br> document</span>)
    id5 --> id6{<span title="Is the potential project addressable via machine learning, technically feasible, and economically viable?">feasible?</span>}
    id6 -- no --> id7([terminate])
    id6 -- yes --> id8(next <br> steps)
    
    classDef default fill:#000000,stroke:#000000,stroke-width:0px,color:#ffffff,font-size:11pt;
```

<br>

<figure>
<figcaption><b>FIGURE</b>.  The data science team is neither a research team, a data team, nor a technology team.  It is 
a key collaborator in the development & deployment of machine learning dependent solutions; it is a business solutions 
consulting/development team.  This diagram illustrates consideration steps vis-à-vis a potential business machine 
learning project.  The project scope/design details informs the feasibility assessment.
</figcaption>
</figure>

<br>

The aim of these pages is to ensure that each prospective client/collaborator carefully considers the time commitment, collaboration commitment, cost, range of expertise, project details, etc., that are required for a business machine learning project. 

A project's details are especially critical to conducting a well-informed technical feasibility & economic 
viability assessment before proceeding.  It is also important to beware that the data science aspect of the project is 
only a part of the project, ignoring this leads to [project failures](https://www.kdnuggets.com/survey-machine-learning-projects-still-routinely-fail-to-deploy) due to, e.g.,

* Under-planning.
* Ambiguous project scope/design details. 
* Project pilots that are neither informed by **nor** tests the deployment goal.
* Underestimating, or ignoring, cost.
* Ignoring the critical importance of intensive collaboration between the business, data science, operations, etc., teams.

<br>

## The Deployment Goal Focus

Colleagues may question the reverse approach of these pages.  Here are a few references that capture our experience of 
why business data science projects fail, and the advantages of starting with ``the end in mind'' [^deployment]

* [Why Data Science Projects Fail](https://pubsonline.informs.org/do/10.1287/LYTX.2023.02.04/full/): Practical Principles for Data Science Success, by Douglas A. Gray.  This is the first article of the excellent [series](https://pubsonline.informs.org/action/doSearch?&target=digital-object-search&content=digitalObjects&Keywords=Principles%20for%20Successful%20Analytics%20Projects).

* [The AI Play Book: Mastering the Rare Art of Machine Learning Deployment](https://mitpress.mit.edu/9780262048903/the-ai-playbook/), by Eric Siegel.

It is not a data project, it is not a technology project, it is not a research project, it is a business project.  The business' deployment goal, and the underlying model's business performance metrics, must be unambiguously detailed.

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

[^deployment]: An upcoming update will include more notes.
