"""
==================
Pipeline Anova SVM
==================

Simple usage of Pipeline that runs successively a univariate
feature selection with anova and then a C-SVM of the selected features.
"""
print __doc__

from scikits.learn import svm
from scikits.learn.datasets import samples_generator
from scikits.learn.feature_selection import SelectKBest, f_regression
from scikits.learn.pipeline import Pipeline

# import some data to play with
X, y = samples_generator.make_classification(
	n_features=20, n_informative=3, n_redundant=0, 
	n_classes=4, n_clusters_per_class=2)

# ANOVA SVM-C
# 1) anova filter, take 3 best ranked features
anova_filter = SelectKBest(f_regression, k=3)
# 2) svm
clf = svm.SVC(kernel='linear')

anova_svm = Pipeline([('anova', anova_filter), ('svm', clf)])
anova_svm.fit(X, y)
anova_svm.predict(X)

