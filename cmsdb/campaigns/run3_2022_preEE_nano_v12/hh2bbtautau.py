# coding: utf-8

"""
HH -> bbtautau datasets for the 2022 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# ggF -> H -> HH
#

# SM
cpn.add_dataset(
    name="hh_ggf_bbtautau_powheg",
    id=14875866,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=101,
    n_events=913950,
)

cpn.add_dataset(
    name="hh_vbf_bbtautau_madgraph",
    id=14792416,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=981154,
)
# Another dataset with the similar name (- instead of _) is also present,
# however less events and more susspicious generator path

# BSM scenarios
cpn.add_dataset(
    name="bsm_hh_vbf_bbtautau_cv1_c2v2_c3_1_madgraph",
    id=14805329,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV-1_C2V-2_C3-1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="bsm_hh_vbf_bbtautau_cv1_c2v0_c3_1_madgraph",
    id=14793769,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=988736,
)

cpn.add_dataset(
    name="bsm_hh_vbf_bbtautau_cv1_c2v1_c3_2_madgraph",
    id=14788950,
    processes=[procs.hh_vbf_bbtautau],
    keys=[
        "/VBFHHto2B2Tau_CV-1_C2V-1_C3-2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="bsm_hh_ggf_bbtautau_kl0_kt1_powheg",
    id=14800360,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=98380,
)

cpn.add_dataset(
    name="bsm_hh_ggf_bbtautau_kl2p45_kt1_powheg",
    id=14805258,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=97635,
)

cpn.add_dataset(
    name="bsm_hh_ggf_bbtautau_kl5_kt1_powheg",
    id=14803777,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=99647,
)
