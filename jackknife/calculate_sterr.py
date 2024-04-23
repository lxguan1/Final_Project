import pandas as pd
import numpy as np
import json


def calc_sterr():
    std_err = {}
    
    for i in range(1,23):
        true_ld = pd.read_csv('../gcta_output_1000/chr' + str(i) + ".score.ld", sep=' ', comment='#')['ldscore']
        std_err[i] = np.zeros(np.shape(true_ld))

        for j in range(1,379):
            jackknife_ld = pd.read_csv('gcta_folders/gcta_file_{}/chr{}.score.ld'.format(str(j), str(i)), sep=' ', comment='#')['ldscore']
            std_err[i] += np.square(np.array(true_ld) - np.array(jackknife_ld))
        
        std_err[i] = np.sqrt(std_err[i])
    
    json.dump(std_err, "standard_error.json")
