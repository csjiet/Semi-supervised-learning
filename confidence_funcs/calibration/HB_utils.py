import numpy as np

# for uniform mass binning methods

def get_uniform_mass_bins(probs, n_bins):
    assert(probs.size >= n_bins), "Fewer points than bins"
    
    probs_sorted = np.sort(probs)

    # split probabilities into groups of approx equal size
    groups = np.array_split(probs_sorted, n_bins)
    bin_edges = list()
    bin_upper_edges = list()

    for cur_group in range(n_bins-1):
        bin_upper_edges += [max(groups[cur_group])]
    bin_upper_edges += [np.inf]

    return np.array(bin_upper_edges)

def bin_points(scores, bin_edges):
    assert(bin_edges is not None), "Bins have not been defined"
    scores = scores.squeeze()
    assert(np.size(scores.shape) < 2), "scores should be a 1D vector or singleton"
    scores = np.reshape(scores, (scores.size, 1))
    bin_edges = np.reshape(bin_edges, (1, bin_edges.size))
    return np.sum(scores > bin_edges, axis=1)

def bin_points_uniform(x, n_bins):
    x = x.squeeze()
    bin_upper_edges = get_uniform_mass_bins(x, n_bins)
    return np.sum(x.reshape((-1, 1)) > bin_upper_edges, axis=1)

def nudge(matrix, delta):
    return((matrix + np.random.uniform(low=0,
                                       high=delta,
                                       size=(matrix.shape)))/(1+delta))

class identity():
    def __init__(self):
        self.bin_upper_edges = np.array([1.0])
        self.n_bins =1 
        self.mean_pred_values = np.array([1.0])
        
    def predict_proba(self, x):
        return x
    def predict(self, x):
        #print(x)
        #return np.argmax(x, axis=1)
        return x