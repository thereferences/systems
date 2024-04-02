
<br>

# Composition

<br>

In general, the questions herein should be studied before data collection.  The datasheets paper [1] notes that most of the questions:

> "… are intended to provide dataset consumers with the information they need to make informed decisions about using 
> the dataset for their chosen tasks. … the questions are designed to elicit information about compliance with the EU's > General Data Protection Regulation (GDPR) or comparable regulations in other jurisdictions."

 
<details><summary><b>References</b></summary>
<ol>
<li><a href="https://arxiv.org/abs/1803.09010v8" target="_blank">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated datasheet appendix</li>
<li><a href="https://www.talend.com/resources/what-is-data-profiling/" target="_blank">Data Profiling</a></li>
</ol>
</details>

<br>

## What does each data set instance represent?

Describe what each instance, i.e., row, of the data set represents.  Although peculiar, if the data set is 
multi-representational, e.g., an instance in a merchant's data base table might represent one of:

* an online reading event
* an online product purchasing event
* an online download event

Each representation must be described.

<br>

## The # of Instances

How many instances does the data set have?

<br>

## Is the data set a sample of a larger data set?

**IF YES:**

* If the data set **is representative** of the larger data set: How was representativeness verified/validated? OR
* If the data set **is not representative** of the larger data set, e.g., is a geographically focused subset, explain why.


<br>

## Lineage


Summarise the data set's lineage, including linkage options. [^lineage]<sup>, </sup>[^extra]

<br>

## Licences & Fees

If applicable, summarise the data's costs.

<br>

## Profiles of Instances

Herein, a summary of the instances of a data set, e.g., for a tabular data set

By Field

The field name

Description: What does the element of an instance denote/represent?

Data Type

Dictionary of a categorical data type

Unit of Measure

Is this a raw data field or a feature?

Is this a target field?

Does the field identify a sub-population?

Column Profile: Note column profiling “ … provides statistical information regarding the distribution of data values and associated patterns that are assigned to each data attribute, including range analysis, sparseness, format and pattern evaluation, cardinality and uniqueness analysis, value absence, abstract type recognition, and attribute overloading analysis“  [1]  If a field/column has missing elements, explain why?

and

A graph of the field’s data distribution

Across Fields

Cross-Column Profiles: Relationships between columns.


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>

[^lineage]: QLIK: [What is data lineage](https://www.qlik.com/us/data-management/data-lineage)
[^extra]: IBM: [What is data lineage?](https://www.ibm.com/topics/data-lineage)
