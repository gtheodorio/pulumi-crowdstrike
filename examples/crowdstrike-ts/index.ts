import * as pulumi from "@pulumi/pulumi";
import * as crowdstrike from "@crowdstrike/pulumi"

//
const hostGroup = new crowdstrike.HostGroup("hostgroup_pulumi_typescript_published", {
    "description": "host group test resource from pulumi",
    "type": "dynamic",
    "assignmentRule": "tags:'SensorGroupingTags/cloud-lab'+os_version:'Amazon Linux 2'"
}

)
