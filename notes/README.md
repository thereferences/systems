<br>

# A Distinct Problem

* [The Problem](#the-problem)
  * [Problem Statement](#problem-statement)
  * [Aim & Objectives](#aim--objectives)
* [Stakeholders](#stakeholders)
  * [Identify the project's stakeholders](#identify-the-projects-stakeholders)
  * [Create a stakeholder register](#create-a-stakeholder-register)
* [Functional Requirement](#functional-requirement)
* [Non Functional Requirement: Cost](#non-functional-requirement-cost)
* [Non Functional Requirements: System](#non-functional-requirements-system)
* [Project Constraints](#project-constraints)
* [Risks](#risks)
* [Datasheets](#datasheets)
  * [Motivation](#motivation)
  * [Composition](#composition)
  * [Collection Process](#collection-process)
  * [Pre-processed Data](#pre-processed-data)
  * [Uses](#uses)
  * [Export Controls](#export-controls)
  * [Maintenance](#maintenance)
  * [Natural Language Processing](#natural-language-processing)



<br>
<br>


## The Problem

### Problem Statement

Briefly describe the problem.  Why is it important, and why address it now?  If there are alternative, off-the-shelf, solutions  justify the rationale for a custom solution.

### Aim & Objectives

Briefly state the aim of the project, e.g.,

> … a system that provides daily forecasts of hourly nitrogen monoxide levels per geographic co&ouml;rdinate

Hence, state the objectives thereof, e.g.

> * Each day, at 0600, the model provides hourly forecasts for the next  hundred and sixty days
> * Each hourly forecast is within 0.05% of the real nitrogen monoxide level

Each objective must have a metric.

<br>
<br>

## Stakeholders

<br>

Stakeholders are critical to a project’s success, beware of their 
import and expectations vis-à-vis agreements, constraints, 
boundaries, etc.

### Identify the project's stakeholders

The stakeholders are the people who

> … can affect the outcome/success of [a] project and/or [are] affected by its outcome/success.  ([Volere](https://homepages.laas.fr/kader/Robertson.pdf))

Examples include:

> * **The client.**  The entity **(a)** the system/product is being built for, and **(b)** that will pay for the system/product. 
> * **The signatories.**  The people who need to sign-off aspects of the project, e.g., system security, data access, etc.
    > The Information/Data Asset Owner is a critical signatory.
> * **End users.**  The people who will interact with the product. 

The Open Group Architecture Framework ( TOGAF) hosts a detailed discussion of [stakeholder management](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap21.html).  The discussion includes a [sample stakeholder map for an imaginary project](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap21.html#:~:text=21.3.1.1-,Sample%20Stakeholder%20Analysis,-A%20sample%20stakeholder).  It is a good guide to discerning your project's stakeholders and their import.

<br>

### Create a stakeholder register

The stakeholder register is a

> … project document that includes information about project stakeholders including an assessment and classification of 
> project stakeholders. [1]

The details per registree should include the stakeholder’s

* Name
* Role; employing organisation.
* Department
* Role in project
* Participation timebox
* Participation cost

and a few items that would aid stakeholder interactions.  For a helpful guide study [2]

<details><summary><b>References</b></summary>
<ol>
<li>A Guide to the Project Management Body of Knowledge, Seventh Edition, 2021, The Standard for Project Management</li>
<li><a href="https://www.pmi.org/learning/library/stakeholder-management-plan-6090" target="_blank">Got stake?</a> by Forman, J. B. & 
Discenza, R., 2012</li>
</ol>
</details>

<br>
<br>

## Functional Requirement

<br>

In the case an artificial intelligence/machine learning project, the functional requirement specifies what a machine 
learning model must do vis-à-vis the project's aim.  A functional requirement must have a defined criterion, or defined 
criteria.  A criterion, i.e., fit criterion, is an objective measure 

> … for defining the meaning of a requirement, and eventually testing whether a given solution satisfies the original 
> requirement. ([Volere Specification](https://homepages.laas.fr/kader/Robertson.pdf))

The client, alongside domain experts, specifies the functional requirement; domain experts are critical to [construct 
validity](https://conjointly.com/kb/construct-validity/), including positing appropriate data sets. Thereafter, the 
client, domain experts - client & independent domain experts - and data scientists discuss

* construct validity vis-à-vis problem statement, aim, and the posited data sets.
* and outline the prospective model's performance measures & metrics
expectations.

The data scientists are responsible for determining the appropriate artificial intelligence algorithm for a problem in 
question, model development, and all the mechanics thereof.


<details>
<summary><b>Example: Functional Requirement & Fit Criteria</b></summary>

### Functional Requirement

> Automatically Classify Skin Cancer Images

### Fit Criteria

<br>

#### <span style="color: #777777">Overarching</span>

Based on a threshold defined as the intersection of precision & sensitivity

**Core**

* Precision > 0.9
* Sensitivity (TPR)  > 0.9
* Specificity (TNR)  > 0.9
* Youden's J Statistic  > 0.9
* Balanced Accuracy  > 0.9

at the threshold, and

* False Positive Rate < 0.1 
* Matthew Correlation Coefficient > 0.8, [-1, +1]

at the threshold.

**Receiver Operating Characteristic Curve**

* Area > 0.85 

**Precision & True Positive Rate Curve**

* Area > 0.85 

<br>

#### <span style="color: #777777">Disaggregated</span>

For each class, and by the same overarching threshold value, ensure that

* Each criterion metric value is within its defined range; as above. 
* The area under the receiver operating curve is within the defined limit as above.
* The area under the precision & true positive rate curve is within the defined limit; as above.

</details>


<br>
<br>

## Non Functional Requirement: Cost

<br>

**In brief.**  Diligently estimate the cost of each part of the project, i.e., preceding & succeeding sections, and more.  This 
will 
probably require the knowledge & help of a mix of professionals, e.g.,  information technology operations team, asset owners, security experts, reliability engineers, etc.

<br>

## Non Functional Requirements: System

<br>

**In brief.**  If a machine learning system hosts a model that identifies human brain magnetic resonance images that exhibit 
cerebral 
atrophy, then system's non-functional requirement will probably stipulate

* Reliability, maintenance, availability, and resilience expectations
* Usability expectations.
* Security expectations.

and much more.  This is the focus of the non-functional requirements, which can be quite costly.

<details><summary><b>Overarching Parts</b></summary>
<ul>
<li>System Security</li>
<li>Usability & Accessibility</li>
<li>Performance & Scalability</li>
<li>Context & Infrastructure</li>
<li>Reliability, Maintainability, Resilience, & Availability</li>
</ul>
</details>

<br>
<br>

## Project Constraints

This will include

* Time Constraints
* Budget Constraints

alongside

* Solution Constraints
* Implementation Environment Constraints: For example, a client might stipulate that the system must be hosted within 
  Google Cloud Platform.

<br>

## Risks

<br>
<br>
<br>
<br>

## Datasheets

<br>

Each dataset must have its own datasheet.  The datasheet of a dataset outlines the dataset’s provenance.  Gebru & colleagues [first proposed Datasheets for Datasets](https://arxiv.org/pdf/1803.09010v1.pdf), for machine learning products or projects, during the years 2018/2019.  Following feedback from a variety of institutions, industries, agencies, etc., a baseline Datasheets for Datasets was released [1, 2].

Each datasheet consists of a set of questions, and the datasheet’s primary objective vis-à-vis dataset creator is to

> encourage dataset creators to reflect carefully upon (a) the “process of creating, distributing, and maintaining a 
> dataset“, and (b) “any underlying assumptions, potential risks or harms, and implications of use“

The primary objective vis-à-vis dataset user is to

> ensure that the dataset user has the information required  to  “ … make informed decisions about using a dataset.“ [1]

This epic consists of a set of stories.  The stories, except the Natural Language Processing story, reflect the groupings of the questions in the latest datasheet version [1, 2]

The questions of the natural language processing (NLP) story apply to NLP projects only.  The questions were developed by Bender & Friedman [3]

<details><summary><b>References</b></summary>
<ol>
<li><a href="https://dl.acm.org/doi/10.1145/3458723" target="_blank">Datasheets for Datasets</a>, Communications of the ACM, 2021, 
Volume 64, Issue 12, pages 86 – 92</li>
<li><a href="https://arxiv.org/abs/1803.09010v8" target="_blank">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated 
datasheet appendix</li>
<li><a href="https://doi.org/10.1162/tacl_a_00041" target="_blank">Data Statements for Natural Language Processing: Toward Mitigating 
System Bias and Enabling Better Science</a>, 
Transactions 
of the Association for Computational Linguistics, 2018, 6: 587–604</li>
</ol>
</details>

<br>

### Motivation

The questions herein are critical for a few reasons, e.g.,

> * External Validity: In the context of a forecasting model, for example, external validity is the degree to which a 
> model’s forecasts can be generalised to other populations, “... in other places, and at other times” [1] 
> * Sponsorship Bias [2, 3]

<details><summary><b>References</b></summary>
<ol>
<li><a href="https://conjointly.com/kb/external-validity/" target="_blank">External Validity</a>, Research Methods Knowledge Base</li>
<li><a href="https://catalogofbias.org/biases/industry-sponsorship-bias/" target="_blank">Industry Sponsorship Bias</a></li>
<li><a href="https://link.springer.com/article/10.1007/s13194-020-00280-2" target="_blank">What is epistemically wrong with research 
affected by sponsorship bias? The evidential account</a></li>
</ol>
</details>

<br>

**The motivation questions:**

* For what purpose was the dataset created?
* Who created the dataset?
* Who funded the creation of the dataset?

<br>

### Composition

The questions herein should be studied prior to data collection.  The datasheets paper [1] notes that most of the questions

> " ,,, are intended to provide dataset consumers with the information they need to make informed decisions about using 
> the dataset for their chosen tasks. Some of the questions are designed to elicit information about compliance with the EU’s General Data Protection Regulation (GDPR) or comparable regulations in other jurisdictions."

<details><summary><b>References</b></summary>
<ol>
<li><a href="https://arxiv.org/abs/1803.09010v8" target="_blank">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated 
datasheet appendix</li>
<li><a href="https://www.talend.com/resources/what-is-data-profiling/" target="_blank">Data Profiling</a></li>
</ol>
</details>

<br>

**The composition questions:**
<ul>
<li>What does each data set instance represent?</li>
<li>How many instances does the data set have?</li>
<li>Is the data set a sample of a larger data set?</li>
<li>Detail the data set's source & linkage attributes</li>
<li>Profiles of Instances: A summary of the instances of the data set by field and across fields.</li>
<li>Detail any errors, sources of noise, or redundancies.</li>
<li>Are there recommended data splits?</li>
<li>Does the data set contain data that might be considered confidential?</li>
<li>Detail distressing data elements</li>
<li>Is it possible to identify individuals directly or indirectly?</li>
<li>Describe sensitive data elements within the data set</li>
</ul>

<br>

### Collection Process

Was the data of each instance acquired via

* a sensor
* an application programming interface
* interviews
* questionnaires
* a mix of mechanisms
* etc.

Summarise the details within a table.

<br>

### Pre-processed Data

In relation to a pre-processed data set, or each pre-processed data field,

* Document the pre-processing steps.
* State whether the underlying raw data is available, and provide a link to the data
* If available, provide a link to the pre-processing programs

<br>

### Uses

According to the data asset owner, what the data should/could, and should not, be used for.  This does not negate the 
responsibility of prospective users vis-à-vis considering the appropriateness of the data for a problem in question.

<br>

### Export Controls

In brief

> Do any export controls or other regulatory restrictions apply to
the dataset or to individual instances? [1, 2]

<details><summary><b>References</b></summary>
<ol>
<li><a href="https://dl.acm.org/doi/10.1145/3458723">Datasheets for Datasets</a>, Communications of the ACM, 2021, Volume 64, Issue 12, pages 86 – 92</li>
<li><a href="https://arxiv.org/abs/1803.09010v8">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated datasheet appendix</li>
</ol>
</details>

<br>

### Maintenance

<br>
<br>
<br>


### Natural Language Processing

The extra questions that must be considered if the prospective model is a natural language processing model.


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>