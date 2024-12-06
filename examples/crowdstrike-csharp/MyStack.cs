using System;
using Pulumi;
using CrowdStrike.Crowdstrike;

class MyStack : Stack
{
    public MyStack()
    {
        var hostGroup = new HostGroup("hostgroup_pulumi_csharp_published", new HostGroupArgs
        {
            Name = "hostgroup_pulumi_dotnet",
            Type = "dynamic",
            Description = "Test pulumi hostgroup",
            AssignmentRule = "tags:'SensorGroupingTags/cloud-lab'+os_version:'Amazon Linux 2'"
        });
    }
}