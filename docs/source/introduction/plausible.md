# Project Plausibility

A solid basis is key.

## A Team's Key Business Questions

In a 2018 article, Kevin Tyranos proposed a few steps that may aid a team's generation of its Key Business Questions form its Business Outcomes Targets.[^Tyranos2018]  In brief, and minimally adapted,

<ol class="numeric">
  <li class="numeric">Business Outcomes<ul><li>Reduce operational cost due to intensive care unit hypoglycaemic incident care costs.</li><li>Reduce risk costs due to intensive care unit hypoglycaemic incident mortality rates.</li></ul>
  </li>
  <li class="numeric">An in-depth evaluation of knowledge & data understandings till date.</li>
  <li class="numeric">Outline key business questions, e.g.,
    <ul><li>Is it possible to continuously predict the probability of a hypoglycaemic incident amongst our intensive care unit patients?</li>
    <li>Is it possible to automatically warn intensive care unit colleagues if a patient is at risk of a hypoglycaemic incident within the next 6 hours?</li></ul>
  </li>
  <li class="numeric">Prioritise</li>
</ol>


<br>

<!--suppress CheckImageSize -->
<img src="../../../assets/W200128_TROYANOS_THEKEY-1200x1580.png" alt="priorities" width="60%" class="x-small">

<figure>
  <figcaption>Source: <a href="https://hbr.org/2020/02/use-data-to-answer-your-key-business-questions" target="_blank">Publicis Health, via Harvard Business Review</a>
  </figcaption>
</figure>

<br>

The _pipe dreams_ cell also addresses the question - do the capabilities to achieve an objective exist?


> If you don’t have the right CRM and tech infrastructure in place, you’ll be unable to put your model into play in the market, and your original question will end up as a pipe dream — its potential business impact is high, but your ability to realize this potential is effectively nonexistent. [^Tyranos2020]


Therefore, ``... cross-functional teams capable of translating insight into action'' are critical.

<br>
<br>


## Quantitative Prioritisation

Douglas A Gray's[^Gray2024a] quantitative prioritisation method is a systematic and unambiguous method.  It depends on

* The business value potential: More details further below.  Subsequently, assign a business value scores $\rightarrow$ highest business value $10$, lowest business value $1$
* Complexity: <i>Complexity, in effect, is an important surrogate measure for risk; i.e., the more complex a project is, the more likely it is that you will run into difficulties that end up manifesting themselves in timeline delays and budget overruns and jeopardize the whole project</i>[^Gray2024a]  Assign complexity scores $\rightarrow$ lowest complexity $10$, highest complexity $1$
* Project Cost: Labour Cost, Materials & Computing Cost.  Subsequent, assign a project cost score to each project $\rightarrow$ lowest $10$, highest $1$

Hence, the <b>priority score</b> is

> business value potential score $\times$ complexity score $\times$ project cost score

The highest possible score is $1000$.  Amongst a set of projects, a project that manages to achieve a $1000$ score <b>(a)</b> has the highest business value, <b>(b)</b> is the least complex, and <b>(c)</b> is the least costly -- **each potentially & relatively**.


### The Business Value Potential

**Best**

[Cost of Delay](https://blackswanfarming.com/cost-of-delay/)

> _Cost of Delay is a way of communicating the impact of time on the outcomes we hope to achieve. More formally, it is the partial derivative of the total expected value with respect to time._
> 
> _Cost of Delay combines urgency and value – two things that humans are not very good at distinguishing between._

<ul class="disc">
  <li class="disc"><a href="https://blackswanfarming.com/cost-of-delay-divided-by-duration/" target="_blank">Cost of Delay Divided by Duration</a></li>
  <li class="disc"><a href="https://blackswanfarming.com/four-steps-to-quantifying-cost-of-delay/"  target="_blank">Four steps to Quantifying Cost of Delay</a></li>
</ul>

<br>


**Close**

<ul class="disc">
  <li class="disc"><a href="https://www.investopedia.com/ask/answers/05/npv-irr.asp" target="_blank">Net Present Value (NPV)</a> cf. <a href="https://www.investopedia.com/ask/answers/05/npv-irr.asp" target="_blank">IRR (Internal Rate of Return)</a></li>
  <li class="disc"><a href="https://www.investopedia.com/terms/r/returnoninvestment.asp"  target="_blank">Return on Investment (ROI)</a> cf. <a href="https://accountinginsights.org/npv-vs-roi-key-differences-and-how-to-use-them-in-decision-making/">NPV & ROI</a></li>
</ul>

<br>

### Project Cost

To avoid over or under penalising - lowest $10$, highest $1$ - scoring via a sigmoid function is an option.  Let $x$ represent a project's monetary cost.  Sigmoid function dependent options include


$$tanh(x) = \frac{e^{x} - e^{-x}}{e^{x} + e^{-x}}$$
$$score = 10 \times \frac{1}{tanh(x)}$$




<br>
<br>

## Viability/Feasibility Filters

### Marginal Benefit & Marginal Cost


<br>

### Stepping Through

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

<figcaption>An illustration of considerations vis-à-vis a potential machine learning dependent project.  The project details inform the feasibility assessment.</figcaption>

<br>
<br>
<br>
<br>

<br>
<br>
<br>
<br>

[^Tyranos2018]: [How to Make Sure You’re Not Using Data Just to Justify Decisions You’ve Already Made](https://hbr.org/2018/10/how-to-make-sure-youre-not-using-data-just-to-justify-decisions-youve-already-made)

[^Tyranos2020]: [Use Data to Answer Your Key Business Questions](https://hbr.org/2020/02/use-data-to-answer-your-key-business-questions)

[^Gray2024a]: Chapter 2 of [Why Data Science Projects Fail: the Harsh Realities of Implementing AI and Analytics, without the Hype](https://www.taylorfrancis.com/books/mono/10.1201/9781032661360/data-science-projects-fail-evan-shellshear-douglas-gray)

[^Marginal2024]: [Marginal Benefit & Marginal Cost](https://www.investopedia.com/ask/answers/051815/what-difference-between-marginal-benefit-and-marginal-cost.asp)

[^Marginal2018]: [What is the Marginal Cost of Capital?](https://pressbooks.pub/businessfinanceessentials/chapter/chapter-10-marginal-cost-of-capital-2/)
