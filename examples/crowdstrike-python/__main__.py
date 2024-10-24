"""A Python Pulumi program"""

import pulumi
import crowdstrike_pulumi

host_group = crowdstrike_pulumi.HostGroup(
    resource_name="hostgroup_pulumi_python",
    description="test pulumi provider",
    type="dynamic",
    assignment_rule="tags:'SensorGroupingTags/cloud-lab'+os_version:'Amazon Linux 2'",
    
)

