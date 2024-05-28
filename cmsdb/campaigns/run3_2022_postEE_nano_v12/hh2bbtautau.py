# coding: utf-8

"""
HH -> bbtautau datasets for the 2022 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# ggF -> H -> HH
#

# SM

cpn.add_dataset(
    name="hh_ggf_bbtautau_powheg",
    id=14853038,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=259,
    n_events=3068220,
)

cpn.add_dataset(
    name="hh_vbf_bbtautau_madgraph",
    id=14802385,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=3432100,
)

# BSM scenarios
cpn.add_dataset(
    name="bsm_hh_vbf_bbtautau_cv1_c2v2_c3_1_madgraph",
    id=14797773,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV-1_C2V-2_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=97000,
)

cpn.add_dataset(
    name="bsm_hh_vbf_bbtautau_cv1_c2v0_c3_1_madgraph",
    id=14801336,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=3434450,
)

cpn.add_dataset(
    name="bsm_hh_vbf_bbtautau_cv1_c2v1_c3_2_madgraph",
    id=14802733,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV-1_C2V-1_C3-2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=100000,
)

cpn.add_dataset(
    name="bsm_hh_ggf_bbtautau_kl0_kt1_powheg",
    id=14800595,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=96787,
)

cpn.add_dataset(
    name="bsm_hh_ggf_bbtautau_kl2p45_kt1_powheg",
    id=14952817,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=362,
    n_events=3435020,
)

cpn.add_dataset(
    name="bsm_hh_ggf_bbtautau_kl5_kt1_powheg",
    id=14802365,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=96676,
)
