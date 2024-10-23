package main

import (
	"github.com/crowdstrike/pulumi-crowdstrike/sdk/go/crowdstrike"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		hostGroup, err := crowdstrike.NewHostGroup(ctx, "hostgroup_pulumi_golang", &crowdstrike.HostGroupArgs{
			Description:    pulumi.String("test pulumi provider"),
			Type:           pulumi.String("dynamic"),
			AssignmentRule: pulumi.String("tags:'SensorGroupingTags/cloud-lab'+os_version:'Amazon Linux 2'"),
		})
		if err != nil {
			return err
		}
		ctx.Export("hostgroup_pulumi_golang", hostGroup)
		return nil
	})
}
