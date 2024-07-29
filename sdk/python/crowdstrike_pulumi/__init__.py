# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .filevantage_policy import *
from .filevantage_rule_group import *
from .get_sensor_update_policy_builds import *
from .host_group import *
from .prevention_policy_linux import *
from .prevention_policy_mac import *
from .prevention_policy_windows import *
from .provider import *
from .sensor_update_policy import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import crowdstrike_pulumi.config as __config
    config = __config
else:
    config = _utilities.lazy_import('crowdstrike_pulumi.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "crowdstrike",
  "mod": "index/filevantagePolicy",
  "fqn": "crowdstrike_pulumi",
  "classes": {
   "crowdstrike:index/filevantagePolicy:FilevantagePolicy": "FilevantagePolicy"
  }
 },
 {
  "pkg": "crowdstrike",
  "mod": "index/filevantageRuleGroup",
  "fqn": "crowdstrike_pulumi",
  "classes": {
   "crowdstrike:index/filevantageRuleGroup:FilevantageRuleGroup": "FilevantageRuleGroup"
  }
 },
 {
  "pkg": "crowdstrike",
  "mod": "index/hostGroup",
  "fqn": "crowdstrike_pulumi",
  "classes": {
   "crowdstrike:index/hostGroup:HostGroup": "HostGroup"
  }
 },
 {
  "pkg": "crowdstrike",
  "mod": "index/preventionPolicyLinux",
  "fqn": "crowdstrike_pulumi",
  "classes": {
   "crowdstrike:index/preventionPolicyLinux:PreventionPolicyLinux": "PreventionPolicyLinux"
  }
 },
 {
  "pkg": "crowdstrike",
  "mod": "index/preventionPolicyMac",
  "fqn": "crowdstrike_pulumi",
  "classes": {
   "crowdstrike:index/preventionPolicyMac:PreventionPolicyMac": "PreventionPolicyMac"
  }
 },
 {
  "pkg": "crowdstrike",
  "mod": "index/preventionPolicyWindows",
  "fqn": "crowdstrike_pulumi",
  "classes": {
   "crowdstrike:index/preventionPolicyWindows:PreventionPolicyWindows": "PreventionPolicyWindows"
  }
 },
 {
  "pkg": "crowdstrike",
  "mod": "index/sensorUpdatePolicy",
  "fqn": "crowdstrike_pulumi",
  "classes": {
   "crowdstrike:index/sensorUpdatePolicy:SensorUpdatePolicy": "SensorUpdatePolicy"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "crowdstrike",
  "token": "pulumi:providers:crowdstrike",
  "fqn": "crowdstrike_pulumi",
  "class": "Provider"
 }
]
"""
)