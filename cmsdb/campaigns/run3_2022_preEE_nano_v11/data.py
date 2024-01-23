# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v11 import campaign_run3_2022_preEE_nano_v11 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_a",
    id=14665093,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2022A-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=5,
    n_events=75655,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_mu_b",
    id=14665444,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2022B-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=8,
    n_events=5328210,
    aux={
        "era": "B",
    },
)

# cpn.add_dataset(
#     name="data_mu_c",
#     id=14665675,
#     is_data=True,
#     processes=[procs.data_mu],
#     keys=[
#         "/SingleMuon/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
#     ],
#     n_files=16,
#     n_events=20164673,
#     aux={
#         "era": "C",
#     },
# )

cpn.add_dataset(
    name="data_mu_c",
    id=14670816,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=85,
    n_events=138018846,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14665037,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=55,
    n_events=75494657,
    aux={
        "era": "D",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_c",
    id=14665314,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=164,
    n_events=263336263,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14665654,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022D-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=62,
    n_events=88530905,
    aux={
        "era": "D",
    },
)

#
# MET
#

cpn.add_dataset(
    name="data_met_a",
    id=14665082,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2022A-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=4,
    n_events=218,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_met_b",
    id=14665430,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2022B-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=10,
    n_events=620518,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_met_c",
    id=14665604,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=7,
    n_events=4412846,
    aux={
        "era": "C",
    },
)

#
# JET HT
#

cpn.add_dataset(
    name="data_jetht_a",
    id=14665313,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2022A-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=4,
    n_events=199152,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_jetht_b",
    id=14665403,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2022B-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=15,
    n_events=14624428,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_jetht_c",
    id=14665445,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2022C-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=17,
    n_events=15620904,
    aux={
        "era": "C",
    },
)
