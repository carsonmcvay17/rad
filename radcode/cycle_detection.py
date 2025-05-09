# imports
import numpy as np
from scipy.interpolate import interp1d

class Cycle_Detection:
    """
    Used to detect when a new cycle starts by defining phase space
    area A and seeing when trajectories cross through area
    """
    def in_region(self, vec, center, tol):
        """
        Returns all vectors passing through region 
        given some tolerance
        """
        return np.all(np.abs(vec-center)<=tol)
    
    def detect_crossings(self, accl, center, tol):
        """
        Detects when the trajectory passes through area and returns
        """
        crossings = []
        was_inside = False

        for i, vec in enumerate(accl):
            inside = Cycle_Detection.in_region(vec, center, tol)
            if inside and not was_inside: # was in the region and left region
                crossings.append(i)
            was_inside = inside
        return crossings
    
    def segment_cycles(self, accl, crossings):
        """
        Consecutive crossings mark cycle
        """
        return [accl[start:end] for start, end in zip(crossings[:-1], crossings[1:])]
    
    def normalize_cycle(self, cycle, num_pts):
        """
        Make each cycle have a fixed number of points
        """
        t_orig = np.linspace(0, 1, len(cycle))
        t_target = np.linspace(0, 1, num_pts)
        interpolator = interp1d(t_orig, cycle, axis=0)
        return interpolator(t_target)
    
    def process_attractor(self, accl, center, tol, num_pts):
        """
        Put the functions together to create an attractor
        """
        crossings = Cycle_Detection.detect_crossings(accl, center, tol)
        cycles = Cycle_Detection.segment_cycles(accl, crossings)
        normalized = [Cycle_Detection.normalize_cycle(c, num_pts) for c in cycles if len(c)>10]
        attractor = np.mean(normalized, axis=0)
        return attractor, normalized