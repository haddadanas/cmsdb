# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_e",
    id=14784109,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022E-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=147,
    n_events=141460608,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14826624,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022F-22Sep2023-v2/NANOAOD",  # noqa
    ],
    n_files=359,
    n_events=449887248,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=14784262,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022G-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=88,
    n_events=76689396,
    aux={
        "era": "G",
    },
)


#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_e",
    id=14783260,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022E-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=188,
    n_events=148654795,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_egamma_f",
    id=14784299,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022F-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=490,
    n_events=464373259,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_egamma_g",
    id=14826525,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022G-22Sep2023-v2/NANOAOD",  # noqa
    ],
    n_files=87,
    n_events=76807350,
    aux={
        "era": "G",
    },
)


#
# Tau
#

cpn.add_dataset(
    name="data_tau_e",
    id=14784151,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022E-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=48,
    n_events=30522105,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=14784498,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022F-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=223,  # 233 - 10
    n_events=115472800,
    aux={
        "era": "F",
        "bad_files": [
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/50000/aa5d0a1d-ce4d-4a6d-913f-9cda23b3a22a.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/2540000/690ae9e3-b88f-4165-938a-33fc8ccc253b.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/50000/bf6a427f-00ba-4324-8dbf-d008da584f10.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/30000/4516186e-0fab-41ba-a86c-67423c0fb483.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/30000/1de9b504-522b-43cf-949a-3fae7b04f6f1.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/2540000/2ab5909f-66c1-4fc5-b7c2-f9173d4dc6df.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/2540000/761ebafd-4d5d-4bc6-9d55-1c06752e1ffc.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/50000/82b002ac-5f79-4b66-8100-5169a0ed34b6.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/2540000/0b171ae3-b87f-482f-89d7-27b5eab6b802.root",
            "/store/data/Run2022F/Tau/NANOAOD/22Sep2023-v1/50000/5618dea1-6308-4485-9ee1-8abf9eeaf34a.root",
        ],
    },
)

cpn.add_dataset(
    name="data_tau_g",
    id=14784442,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022G-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=35,  # 36 - 1
    n_events=17838713,
    aux={
        "era": "G",
        "bad_files": [
            "/store/data/Run2022G/Tau/NANOAOD/22Sep2023-v1/30000/926604d0-2c69-4a09-8eab-0636e26b0ac9.root",
        ],
    },
)


#
# MuonEG
#


cpn.add_dataset(
    name="data_muoneg_e",
    id=14783435,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=29,
    n_events=12873327,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=14784482,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=95,
    n_events=38219969,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=14784485,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=27,
    n_events=6238527,
    aux={
        "era": "G",
    },
)
