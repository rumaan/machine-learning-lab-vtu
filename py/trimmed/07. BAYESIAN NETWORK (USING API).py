# coding: utf-8
from bayespy.nodes import Categorical, Mixture
from bayespy.inference import VB
import numpy as np
FALSE = 0
TRUE = 1
def _or(p_false, p_true):
    return np.take([p_false, p_true], [[FALSE, TRUE], [TRUE, TRUE]], axis=0)
asia = Categorical([0.5, 0.5])
tuberculosis = Mixture(asia, Categorical, [[0.99, 0.01], [0.8, 0.2]])
smoking = Categorical([0.5, 0.5])
lung = Mixture(smoking, Categorical, [[0.98, 0.02], [0.25, 0.75]])
bronchitis = Mixture(smoking, Categorical, [[0.97, 0.03], [0.08, 0.92]])
xray = Mixture(tuberculosis, Mixture, lung, Categorical,_or([0.96, 0.04], [0.115, 0.885]))
dyspnea = Mixture(bronchitis, Mixture, tuberculosis, Mixture, lung, Categorical,[_or([0.6, 0.4],[0.18, 0.82]),_or([0.11, 0.89], [0.04, 0.96])])
tuberculosis.observe(TRUE)
smoking.observe(FALSE)
bronchitis.observe(TRUE)
Q = VB(dyspnea, xray, bronchitis, lung, smoking, tuberculosis, asia)
Q.update(repeat=100)
print("P(asia):", asia.get_moments()[0][TRUE])
print("P(tuberculosis):", tuberculosis.get_moments()[0][TRUE])
print("P(smoking):", smoking.get_moments()[0][TRUE])
print("P(lung):", lung.get_moments()[0][TRUE])
print("P(bronchitis):", bronchitis.get_moments()[0][TRUE])
print("P(xray):", xray.get_moments()[0][TRUE])
print("P(dyspnea):", dyspnea.get_moments()[0][TRUE])
