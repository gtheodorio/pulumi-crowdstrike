// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace CrowdStrike.Crowdstrike.Inputs
{

    public sealed class CloudAwsAccountSensorManagementArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable 1-click sensor deployment
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        public CloudAwsAccountSensorManagementArgs()
        {
        }
        public static new CloudAwsAccountSensorManagementArgs Empty => new CloudAwsAccountSensorManagementArgs();
    }
}
