# cmsdb

[![Lint and test](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml/badge.svg)](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml)
[![License](https://img.shields.io/github/license/uhh-cms/cmsdb.svg)](https://github.com/uhh-cms/cmsdb/blob/master/LICENSE)

Database of physics processes, cross sections and scientific constants as well as CMS-related campaign information on datasets.


#### Dependencies

- [order](https://github.com/riga/order) is used to model the relations between physics meta data containers (datasets, processes, systematics, ...).
- [scinum](https://github.com/riga/scinum)'s `Number` is the basis for numeric values with multiple sources of systematic uncertainties attributed to them.


## Adding a new campaign
To add a new campaign, create a new folder in the `./cmsdb/campaigns` directory. The file should be named after the campaign with the used NanoAoD version, e.g., `run3_2023_nano_v12`. In the folder, create a `__init__.py` file, in which the campaign instance of the `order.Campaign` class is defined as follows:

```python
from order import Campaign

campaign_run3_2023_nano_v12 = Campaign(
    name="run3_2023_nano_v12", # name with which the campaign is referenced in the analysis
    id=320231201,              # a unique id for the campaign (e.g. run-year-nano version-number)
    ecm=13.6,                  # used center of mass energy in TeV
    bx=25,                     # number of bunch crossings
    aux={                      # additional information (can be accessed via in the analysis via campaign.x)
        "tier": "NanoAOD",
        "year": 2023,
        "version": 12,
    },
)
```
Additionally, `.py` files for all used datasets should be created in the campaign folder and imported into the `__init__.py` file. It is recommended to separate the datasets into different files based on the used dataset type or process type (e.g., `data.py`, `higgs.py`, `qcd.py`,...). In every new dataset file, the campaign instance as well as the needed processes from `cmsdb.processes` should be imported (usually it is more convenient to import the whole process module).

In the analysis, a new entry in the configuration files for the new campaign is needed in order to be able to use it.
## Adding a new dataset
For the creation of new datasets, a Python script `get_das_info.py` is provided, which can be used to generate the necessary code for the dataset. The script can be found in the `./scripts` directory, and it uses the `dasgoclient` to get the necessary information for the dataset and uses the same key structure as the CMS Data Aggregation System. For running the script, a valid voms proxy is required (sourcing the analysis environment is recommended since all needed packages are then activated).
For running the script, just provide the dataset name pattern as an argument with `-d` or `--dataset`. All matching datasets are printed to the console with the necessary information.

```bash 
python get_das_info.py -d /GluGlutoHHto2B2Tau*/*Run3Summer23NanoAODv12*/NANOAODSIM

> cpn.add_dataset(
>     name="PLACEHOLDER",
>     id=14931313,
>     processes=[procs.PLACEHOLDER],
>     keys=[
>         "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
>     ],
>     n_files=47,
>     n_events=959000,
> )
> 
> cpn.add_dataset(
>     name="PLACEHOLDER",
>     id=14931215,
>     processes=[procs.PLACEHOLDER],
>     keys=[
>         "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
>     ],
>     n_files=48,
>     n_events=994000,
> )
> ...
```

The needed datasets can be copied from the output and pasted into the corresponding dataset file in the campaign folder. The `name` and `processes` should be replaced with a useful dataset name and the used processes. If multiple datasets are to be used under one name or one dataset instance, all dataset keys should be appended to the list in the `keys` parameter, and `n_files` and `n_events` should be updated with the total number of files and events for all datasets accordingly. This is usually the case if extensions of a dataset exist.

The dataset file should look like this:

```python
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_nano_v12 import campaign_run3_2023_nano_v12 as cpn

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_0_kt_1_c2_0_powheg",
    id=14931313,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=959000,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_0_kt_1_c2_1_powheg",
    id=14931215,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=994000,
)
```
