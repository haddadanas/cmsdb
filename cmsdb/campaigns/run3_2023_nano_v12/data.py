# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_nano_v12 import campaign_run3_2023_nano_v12 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_e",
    id=14763168,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2023E-PromptReco-v1/NANOAOD",
    ],
    n_files=41,
    n_events=8078002,
    aux={
        "era": "E",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_b",
    id=14668013,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023B-PromptNanoAODv11p9_v1-v1/NANOAOD",
    ],
    n_files=32,
    n_events=3680520,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_tau_c",
    id=14690540,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-PromptNanoAODv12_v3-v1/NANOAOD",
    ],
    n_files=14,
    n_events=6470602,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14576539,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-PromptReco-v2/NANOAOD",
    ],
    n_files=29,
    n_events=7246202,
    aux={
        "era": "D",
    },
)


#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_e",
    id=14763101,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2023E-PromptReco-v1/NANOAOD",
    ],
    n_files=28,
    n_events=4136453,
    aux={
        "era": "E",
    },
)
