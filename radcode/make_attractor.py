# imports
import numpy as np
from scipy.signal import find_peaks
from scipy.interpolate import interp1d

class Attractor:
    def segment_cycles(self, vec, peaks):
        """
        Extract gait cycles based on peaks
        """
        cycle = [vec[peaks[i]:peaks[i+1]] for i in range(len(peaks-1))]
        return cycle
    
    def normalize_cycle(self, cycle, num_points=100):
        """
        Interpolate each gait cycle to a fixed number of points
        """
        original = np.linspace(0, 1, len(cycle))
        target = np.linspace(0, 1, num_points)
        interpolater = interp1d(original, cycle, axis=0)
        normalized_cycle = interpolater(target)
        return normalized_cycle
    
    def compute_attractor(cycles, num_points=100):
        """
        Compute the attractor as the mean across normalized cycles
        """
        normed = np.array([Attractor.normalize_cycle(c, num_points) for c in cycles])
        return np.mean(normed, axis=0)

    
    
    
    




    