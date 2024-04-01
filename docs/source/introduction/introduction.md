# Introduction


:::{note}
:class: margin
In progress.
:::

<br>

> "… aiming to do the right thing, rather than doing things right."

<br>




```{mermaid}
%%{ init: { 'flowchart': { 'curve': 'monotoneX' } } }%%
flowchart LR    
    id0([start]) --> id1{budget} -- yes --> id2{plausible<br> budget &<br> time-box}
    id1 -- no --> id3([terminate])
    id2 -- no --> id4([terminate])
    id2 -- yes --> id5(<span title="The project details">design <br> document</span>)
    id5 --> id6{feasible}
    id6 -- no --> id7([terminate])
    id6 -- yes --> id8(next <br> steps)
    
    classDef default fill:#000000,stroke:#000000,stroke-width:0px,color:#ffffff,font-size:11pt;
    
```

<br>

<figure>
<figcaption><b>FIGURE</b>.  The data science team is neither a research team, a data team, nor a technology team.  It is a business solutions development team; rather, it is a key collaborator in the development & deployment of machine learning dependent solutions.
</figcaption>
</figure>

<br>

The aim of these pages is to ensure that each prospective client/collaborator carefully considers the commitment 
(time & collaboration), cost, range of expertise, project details, etc., that are required for a business machine learning 
project. 

A project's details are especially critical to conducting a well-informed technical feasibility & economic 
viability assessment before proceeding.  It is also important to beware that the data science aspect of the project is 
only a part of the project, ignoring this leads to [project failures](https://www.kdnuggets.com/survey-machine-learning-projects-still-routinely-fail-to-deploy):

> Business machine learning projects failures, a few examples of causes:
> * Under-planning.
> * Project Misunderstandings & Opaqueness: It is not a data project, it is not a technology project, it is a business project.  The business' deployment goal, and the underlying model's business performance metrics, must be unambiguously detailed.
> * Underestimating, or ignoring, cost.
> * Ignoring the critical importance of intensive collaboration between the business, data science, operations, etc., teams.

<br>

Finally, understanding what data science is, and is not, understanding the demands of a business machine learning project,
etc., is a step towards avoiding [data scientists turnover](https://www.consortia.com/insights/why-do-data-scientists-leave-their-jobs/bp120/) problems, and more.

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>
