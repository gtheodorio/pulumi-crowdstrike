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

    public sealed class CloudAwsAccountRealtimeVisibilityArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The AWS region of the CloudTrail bucket
        /// </summary>
        [Input("cloudtrailRegion", required: true)]
        public Input<string> CloudtrailRegion { get; set; } = null!;

        /// <summary>
        /// Enable real-time visibility and detection
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        /// <summary>
        /// Set to true if a CloudTrail already exists
        /// </summary>
        [Input("useExistingCloudtrail")]
        public Input<bool>? UseExistingCloudtrail { get; set; }

        public CloudAwsAccountRealtimeVisibilityArgs()
        {
        }
        public static new CloudAwsAccountRealtimeVisibilityArgs Empty => new CloudAwsAccountRealtimeVisibilityArgs();
    }
}
