# Import necessary libraries
import pandas as pd


def extract_snps():
    """No longer needed, but was originally used to extract SNPs that were used in the EUR population"""
    # Loop through different chromosomes
    for chr in range(1, 23):
        # Load the legend file into a pandas DataFrame
        df = pd.read_csv('1000GP_Phase3/1000GP_Phase3_chr{}.legend.gz'.format(str(chr)), compression='gzip', sep=' ', comment='#')

        # Filter the DataFrame to include only rows where the EUR column is not 0
        eur_df = df[df['EUR'] != 0]

        # Write the IDs of the filtered SNPs to a new file
        eur_df['id'].to_csv('snp_files/chr{}_eur_snps.txt'.format(str(chr)), index=False, header=False)

def extract_ind_old(group = "EUR"):
    """Extracts the individuals in a specified population
    
    DEPRECATED, this was for the case of the second bad dataset, where per0, per1, per2, ... 
    were used instead of the actual individual identifiers"""
    # Load the sample file into a pandas DataFrame
    df = pd.read_csv('1000GP_Phase3/1000GP_Phase3.sample', sep=' ', comment='#')

    per_list = ['per' + str(i) for i in range(len(df['ID']))]

    df.insert(0, 'per', per_list, True)

    # Filter the DataFrame to include only rows with the specified group
    eur_df = df[df['GROUP'] == group]

    # Write the IDs of the filtered individuals to a new file
    eur_df['per'].to_csv('eur_inds.txt'.format(str(chr)), index=False, header=False)

def extract_ind_new(group = "EUR"):
    """Extracts the individuals in a specified population"""
    # Load the sample file into a pandas DataFrame
    df = pd.read_csv('data/ALL_1000G_phase1integrated_v3.sample', sep=' ', comment='#')

    # Filter the DataFrame to include only rows with the specified group
    # Also remove the cousin that the paper removed
    eur_df = (df[df['group'] == group])[df['sample'] != 'HG00119']

    out_df = pd.DataFrame({"family" : eur_df.loc[0:, 'sample'].tolist(), "sample" : eur_df.loc[0:, 'sample'].tolist()})

    # Write the IDs of the filtered individuals to a new file
    out_df.to_csv('eur_inds.txt', columns=['family', 'sample'], sep=' ', index=False, header=False)

def extract_subpop_ind(pop = "CEU"):
    """Extracts the individuals in a specified population"""
    # Load the sample file into a pandas DataFrame
    df = pd.read_csv('data/ALL_1000G_phase1integrated_v3.sample', sep=' ', comment='#')

    # Filter the DataFrame to include only rows with the specified population
    # Also remove the cousin that the paper removed
    eur_df = (df[df['population'] == pop])[df['sample'] != 'HG00119']

    out_df = pd.DataFrame({"family" : eur_df.loc[0:, 'sample'].tolist(), "sample" : eur_df.loc[0:, 'sample'].tolist()})

    # Write the IDs of the filtered individuals to a new file
    out_df.to_csv(pop + '_inds.txt', columns=['family', 'sample'], sep=' ', index=False, header=False)

# extract_ind_new("EUR")
for pop in ['CEU', 'GBR', 'TSI', 'FIN']:
    extract_subpop_ind(pop)
