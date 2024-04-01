<br>

# Performance Metrics

<br>

:::{note}
:class: margin
In progress
:::


<h2>Criteria</h2>

<details><summary>Acronyms</summary>
<br>
N: # of negative cases.<br>
P: # of positive cases.<br>
TN: True Negative<br>
FP: False Positive<br>
FN: False Negative<br>
TP: True Positive<br>
TNR: TN/N, True Negative Rate (specificity)<br>
FPR: FP/N, False Positive Rate (fall out)<br>
FNR: FN/P, False Negative Rate (miss rate)<br>
TPR: TP/P, True Positive Rate (hit rate, sensitivity, recall)
<br>
</details>

<br>

Based on the
* Error Matrix Measures, i.e., TP, FN, FP, TN
* A threshold defined as the intersection of precision & sensitivity.

<br>

**Overarching Criteria**

At the threshold

* Precision > 0.9
* Sensitivity (TPR) > 0.9
* Specificity (TNR) > 0.9
* Youden's J Statistic > 0.9

and

* False Positive Rate < 0.1

<br>

**Disaggregated Criteria**

For each class, and by the same overarching threshold value, ensure that:

* Each criterion metric value is within its defined range; as oulined above.


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
