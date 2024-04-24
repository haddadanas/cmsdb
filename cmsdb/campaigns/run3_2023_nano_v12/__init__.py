# coding: utf-8

"""
Common, analysis independent definition of the 2023 with datasets at NanoAOD tier in version 11.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2023_nano_v12 = Campaign(
    name="run3_2023_nano_v12",
    id=320231201,  # 3 2023 12 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2023,
        "version": 12,
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2023_nano_v12.data  # noqa
