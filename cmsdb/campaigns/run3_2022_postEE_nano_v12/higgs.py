# coding: utf-8

"""
Higgs datasets for the 2022 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14807725,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=289000,
)

# cpn.add_dataset(
#     name="h_ggf_tautau_madgraph",
#     id=14849353,
#     processes=[procs.h_ggf_tautau],
#     keys=[
#         "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=89,
#     n_events=3533459,
# )

# vbf
cpn.add_dataset(
    name="h_vbf_tautau_powheg",
    id=14804064,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-Poisson60KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=298000,
)

# H radiation

cpn.add_dataset(
    name="zh_llbb_powheg",
    id=14802579,
    processes=[procs.zh_llbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=37 + 236,
    n_events=2062940 + 12923375,
)

cpn.add_dataset(
    name="zh_qqbb_powheg",
    id=14790777,
    processes=[procs.zh_qqbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=17 + 136,
    n_events=4090842 + 11353020,
)

cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14927555,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=69650,
)

cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14925742,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=70000,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14925240,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=67580,
)

cpn.add_dataset(
    name="ggzh_llbb_powheg",
    id=14800335,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=36 + 153,
    n_events=2068050 + 13417872,
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
    id=14868530,
    processes=[procs.tth_bb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=134,
    n_events=11099294,
)

cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14845759,
    processes=[procs.tth_nonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=122,
    n_events=13955780,
)
