<br>

# Business Metrics

<br>

:::{note}
:class: margin
In progress
:::


Criteria

<details><summary>Acronyms</summary>
N: # of negative cases.
P: # of positive cases.
TN: True Negative
FP: False Positive
FN: False Negative
TP: True Positive
TNR: TN/N, True Negative Rate (specificity)
FPR: FP/N, False Positive Rate (fall out)
FNR: FN/P, False Negative Rate (miss rate)
TPR: TP/P, True Positive Rate (hit rate, sensitivity, recall)
</details>



Based on the
* Error Matrix Measures, i.e., TP, FN, FP, TN
* A threshold defined as the intersection of precision & sensitivity.

Overarching Criteria

* Precision > 0.9
* Sensitivity (TPR) > 0.9
* Specificity (TNR) > 0.9
* Youden's J Statistic > 0.9

and

* False Positive Rate < 0.1

at the threshold.

Disaggregated Criteria

For each class, and by the same overarching threshold value, ensure that

* Each criterion metric value is within its defined range; as oulined above.
