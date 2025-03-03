// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/crowdstrike/pulumi-crowdstrike/sdk/go/crowdstrike/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

var _ = internal.GetEnvOrDefault

// Falcon Client Id for authenticating to the CrowdStrike APIs. Will use FALCON_CLIENT_ID environment variable when left
// blank.
func GetClientId(ctx *pulumi.Context) string {
	return config.Get(ctx, "crowdstrike:clientId")
}

// Falcon Client Secret used for authenticating to the CrowdStrike APIs. Will use FALCON_CLIENT_SECRET environment variable
// when left blank.
func GetClientSecret(ctx *pulumi.Context) string {
	return config.Get(ctx, "crowdstrike:clientSecret")
}

// Falcon Cloud to authenticate to. Valid values are autodiscover, us-1, us-2, eu-1, us-gov-1. Will use FALCON_CLOUD
// environment variable when left blank.
func GetCloud(ctx *pulumi.Context) string {
	return config.Get(ctx, "crowdstrike:cloud")
}

// For MSSP Master CIDs, optionally lock the token to act on behalf of this member CID
func GetMemberCid(ctx *pulumi.Context) string {
	return config.Get(ctx, "crowdstrike:memberCid")
}
