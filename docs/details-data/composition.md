<br>

# Composition

In general, the questions herein should be studied before data collection.  The datasheets paper [1] notes that most of the questions:

<blockquote>
  "… are intended to provide dataset consumers with the information they need to make informed decisions about using the dataset for their chosen tasks. … the questions are designed to elicit information about compliance with the EU's General Data Protection Regulation (GDPR) or comparable regulations in other jurisdictions."
</blockquote>

<br>

<details><summary><b>References</b></summary>
<ol class="numeric">
    <li class="numeric"><a href="https://arxiv.org/abs/1803.09010v8" target="_blank">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated datasheet appendix</li>
</ol>
</details>

<br>
<br>

## What does each data set instance represent?

Describe what each instance, i.e., row, of the data set represents.  Although peculiar, if the data set is multi-representational, e.g., an instance in a merchant's data base table might represent one of: (a) an online reading event, (b) an online product purchasing event, or \(c\) an online download event.  Each representation must be described.

<br>
<br>

## The # of Instances

How many instances does the data set have?

<br>
<br>

## Pre-processed?

Are any aspects of the data set pre-processed?  If yes:

<ul class="disc">
    <li class="disc">Document the pre-processing steps.</li>
    <li class="disc">State whether the underlying raw data is available, and provide a link to the data.</li>
    <li class="disc">If available, provide a link to the pre-processing programs.</li>
</ul>

<br>
<br>

## Is the data set a sample of a larger data set?

**If yes:**

<ul class="disc">
    <li class="disc"><b>If the data set is representative</b> of the larger data set: How was representativeness verified/validated?</li>
    <li class="disc"><b>If the data set is not representative</b> of the larger data set, e.g., is a geographically focused subset, explain why.</li>
</ul>

<br>
<br>

## Lineage

Summarise the data set's lineage, including linkage options. [1, 2]

<br>

<details><summary><b>References</b></summary> 
<ol class="numeric">
    <li class="numeric"><a href="https://www.qlik.com/us/data-management/data-lineage" target="_blank">QLIK: What is data lineage?</a></li>
    <li class="numeric"><a href="https://www.ibm.com/topics/data-lineage" target="_blank">IBM: What is data lineage?</a></li>
</ol>
</details>

<br>
<br>

## Licences & Fees

If applicable, summarise the data's costs.

<br>
<br>

## Profiles of Instances

Herein, the focus is a summary of the instances of a data set, e.g., for a tabular data set:

**By Field**

<ul class="disc">
    <li class="disc">The field name.</li>
    <li class="disc">Description: What does the element of an instance denote/represent?</li>
    <li class="disc">Data type.</li>
    <li class="disc">Dictionary of a categorical data type.</li>
    <li class="disc">Unit of measure.</li>
    <li class="disc">Is this a raw data field or a feature?</li>
    <li class="disc">Is this a target field?</li>
    <li class="disc">Does the field identify a sub-population?</li>
    <li class="disc">Column Profile: Note column profiling <i>"… provides statistical information regarding the distribution of data values and associated patterns that are assigned to each data attribute, …"</i>. [1] &nbsp; &nbsp; If a field/column has missing elements, explain why.</li>
    <li class="disc">A graph of the field's data distribution.</li>
</ul>

<br>

**Across Fields**

<ul class="disc">
    <li class="disc">Cross-Column Profiles: Relationships between columns.</li>
</ul>

<br>
<br>

<details><summary><b>References</b></summary>
<ol class="numeric">
    <li class="numeric">5.5.2 Profiling for Data Quality Assessment, in <a href="https://www.sciencedirect.com/book/9780123742254/master-data-management" target="_blank">Master Data Management</a>, Page 96, The MK/OMG Press, 2008</li>
    <li class="numeric"><a href="https://www.talend.com/resources/what-is-data-profiling/" target="_blank">Data Profiling</a></li>
</ol>
</details>

<br>
<br>


## Errors

Please detail any errors, sources of noise, or redundancies.


<br>
<br>


## Recommended Data Splits for Machine Learning

Are there recommended data splits?

<br>
<br>

## Confidentiality

Does the data set contain data that might be considered confidential?  For example,

<ul class="disc">
    <li class="disc">Is the data protected by legal privilege or by doctor–patient confidentiality?</li>
    <li class="disc">Does the data include the content of private/non-public communications of individuals.</li>
</ul>

<br>
<br>

## Identification of Individuals

Is it possible to identify individuals directly or indirectly?

<br>
<br>

## Data Sensitivity

Does the data set include sensitive data elements?  Describe.  Examples of sensitive data elements are 
elements that directly/indirectly reveal:

<ul class="disc">
    <li class="disc">Locations.</li>
    <li class="disc">Financial details.</li>
    <li class="disc">Health details.</li>
    <li class="disc">Biometric profiles.</li>
    <li class="disc">Genetic profiles.</li>
    <li class="disc">Government identification codes of individuals.</li>
    <li class="disc">Criminal history.</li>
    <li class="disc">Institutionally and/or commercially sensitive data.</li>
    <li class="disc">Race or ethnic origin.</li>
    <li class="disc">Sexual orientations.</li>
    <li class="disc">Religious beliefs.</li>
    <li class="disc">Political opinions.</li>
    <li class="disc">Trade union memberships.</li>
    <li class="disc">And more.</li>
</ul>

<br>
<br>

## Distressing Data Elements

Does ``… the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?'' [1, 2]

<br>

<details><summary><b>References</b></summary>
<ol class="numeric">
    <li class="numeric"><a href="https://dl.acm.org/doi/10.1145/3458723" target="_blank">Datasheets for Datasets</a>, Communications of the ACM, 2021, Volume 64, Issue 12, pages 86 – 92</li>
    <li class="numeric"><a href="https://arxiv.org/abs/1803.09010v8" target="_blank">Datasheets for Datasets</a>, arXiv:1803.09010v8, 2021, updated datasheet appendix</li>
</ol>
</details>

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
