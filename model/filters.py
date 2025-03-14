from pykalman import KalmanFilter
import numpy as np

class Kalman:
    def __init__(self):
        self.kf = KalmanFilter(
            initial_state_mean=0,
            n_dim_obs=1,
            transition_matrices=[1],
            observation_matrices=[1],
            transition_covariance=[1e-6],
            observation_covariance=[1e-2]
        )

    def apply_filter(self, record):
        filtered_output, _ = self.kf.filter(record)
        return filtered_output
