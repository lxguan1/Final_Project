# Import necessary libraries
import pandas as pd
import sys, os

def extract_ind_new(group = "EUR"):
    """Extracts the individuals of the jackknife"""
    # Load the sample file into a pandas DataFrame
    df = pd.read_csv('../data/ALL_1000G_phase1integrated_v3.sample', sep=' ', comment='#')

    # Filter the DataFrame to include only rows with the specified group
    # Also remove the cousin that the paper removed
    # And remove the jackknife individual
    eur_df = (df[df['group'] == group])[df['sample'] != 'HG00119'].drop(int(sys.argv[1]))

    out_df = pd.DataFrame({"family" : eur_df.loc[1:, 'sample'].tolist(), "sample" : eur_df.loc[1:, 'sample'].tolist()})

    # Write the IDs of the filtered individuals to a new file
    plink_folder = "plink_folders/plink_files_" + sys.argv[1]
    gcta_folder = "gcta_folders/gcta_files_" + sys.argv[1]
    if not os.path.exists(plink_folder):
        os.mkdir(plink_folder)
    if not os.path.exists(gcta_folder):
        os.mkdir(gcta_folder)
    out_df.to_csv(plink_folder + '/inds.txt', columns=['family', 'sample'], sep=' ', index=False, header=False)