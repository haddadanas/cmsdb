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
    name="data_mu_c_1",
    id=14786982,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=165,
    n_events=138943783,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_c_2",
    id=14787027,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=131,
    n_events=101615754,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d_1",
    id=14787686,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=32,
    n_events=21462916,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_d_2",
    id=14786997,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=30,
    n_events=21463645,
    aux={
        "era": "D",
    },
)


#
# Tau
#

cpn.add_dataset(
    name="data_tau_c",
    id=14786972,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=70,
    n_events=45176805,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14786907,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=13,
    n_events=7246202,
    aux={
        "era": "D",
    },
)


#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_a",
    id=14667984,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023A-PromptNanoAODv11p9_v2-v1/NANOAOD",  # noqa
    ],
    n_files=3,
    n_events=839,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_egamma_b",
    id=14784860,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023B-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=47,
    n_events=23772132,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_egamma_c",
    id=14786977,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=168,
    n_events=160108119,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14787876,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=33,
    n_events=22657211,
    aux={
        "era": "D",
    },
)

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
