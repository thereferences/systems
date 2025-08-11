# Maintainability & Resilience

## Definitions

Of maintainability and resilience.

### Maintainability

In the systems engineering body of knowledge the [basic definition of maintainability](https://sebokwiki.org/wiki/System_Reliability,_Availability,_and_Maintainability#Maintainability) is the

<blockquote>“ … probability that a given maintenance action for an item under given usage conditions can be performed within a stated time interval when the maintenance is performed under stated conditions using stated procedures and resources.”</blockquote>

Note that **maintainability comprises** serviceability & repairability, i.e.,

<blockquote>"… the ease of conducting scheduled inspections and servicing"</blockquote>

**and**

> "… the ease of restoring service after a failure"

<br>

### Resilience

The resilience of a system can be defined as "… the ability to maintain [capability](https://sebokwiki.org/wiki/Capability_(glossary)) in the face of a [disruption](https://sebokwiki.org/wiki/Disruption_(glossary))" [[The Systems Engineering Body of Knowledge.](https://sebokwiki.org/wiki/System_Resilience#Definition)]

The body of knowledge outlines the objectives of a system's resilience plan. Study the Achieving Resilience details, therein the fundamental objectives are:

<ul>
    <li>Avoid: eliminate or reduce exposure to <a href="https://sebokwiki.org/wiki/Stress_(glossary)" target="_blank">stress</a></li>
    <li>Withstand: resist capability degradation when stressed</li>
    <li>Recover: replenish lost capability after degradation</li>
</ul>


<br>


## Outlining Specifications for Machine Learning Systems

**In the context of machine learning**, the foci herein are

<ul>
    <li><b>The model drift and data drift strategy</b>.  The blog <a href="https://encord.com/blog/model-drift-best-practices/" target="_blank">Model Drift: Best Practices to Improve Machine Learning Model Performance</a> includes an excellent discussion about how to monitor machine learning systems.  Drift details must be outlined vis-à-vis model drift and data drift.  Model drift monitoring is via the evaluation metrics detailed in the model performance metrics section.  Whereas data drift is generally via statistical tests or custom models, depending on the data types in question.</li>
    <li><b>Continuous performance improvement strategy</b>.  For continuous model improvement purposes, the system architecture should include a re-training component.  If it does not, the monitoring system should have an automatic end-of-life alert, triggered by one or more evaluation metrics falling-out of their constraints.</li>
    <li><b>Maintenance services/agreements</b>.  For general maintainability concepts, study the <a href="https://sebokwiki.org/wiki/System_Reliability,_Availability,_and_Maintainability" target="_blank">reliability, maintainability, and availability page</a> of the systems engineering body of knowledge for the expectations herein; <b>and the maintenance and resilience metrics thereof</b>. </li>
</ul>

Altogether, define maintenance and resilience metrics vis-à-vis the system/product, model drift & data drift.  The references link to metrics definitions examples.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>

[^maintenance-metrics]: <a href="https://www.maintworld.com/Applications/5-Important-Maintenance-Metrics-and-How-To-Use-Them" target="_blank">Maintenance Metrics</a>
[^resilience-metrics]: <a href="https://sebokwiki.org/wiki/System_Resilience#Metrics" target="_blank">Resilience Metrics</a>
[^drift]: <a href="https://arxiv.org/abs/2012.09258">Detection of data drift and outliers affecting machine learning model performance over time.</a>

<br>
<br>
