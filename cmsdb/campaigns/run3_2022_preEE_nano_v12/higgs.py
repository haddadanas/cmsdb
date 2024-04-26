# coding: utf-8

"""
Higgs datasets for the 2022 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14805667,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=295722,
)
# cpn.add_dataset(
#     name="h_ggf_tautau_madgraph",
#     id=14849328,
#     processes=[procs.h_ggf_tautau],
#     keys=[
#         "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=29,
#     n_events=1038456,
# )

# vbf
cpn.add_dataset(
    name="h_vbf_tautau_powheg",
    id=14797744,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=299337,
)

# H radiation
cpn.add_dataset(
    name="zh_llbb_powheg",
    id=14805378,
    processes=[procs.zh_llbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=34 + 57,
    n_events=599100 + 4339792,
)

cpn.add_dataset(
    name="zh_qqbb_powheg",
    id=14805167,
    processes=[procs.zh_qqbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=19 + 65,
    n_events=1144560 + 3177722,
)

cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14927154,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=28752,
)

cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14925460,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=30000,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14926126,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=30000,
)

cpn.add_dataset(
    name="ggzh_llbb_powheg",
    id=14803231,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=23 + 41,
    n_events=582250 + 3780820,
)

# ttH
# cpn.add_dataset(
#     name="tth_tautau_powheg",
#     id=14198429,
#     processes=[procs.tth_tautau],
#     keys=[
#         "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
#     ],
#     n_files=32,
#     n_events=21700000,
# )

cpn.add_dataset(
    name="tth_bb_powheg",
    id=14857767,
    processes=[procs.tth_bb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=3177628,
)

cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14849153,
    processes=[procs.tth_nonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=3846525,
)
