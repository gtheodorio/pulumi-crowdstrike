// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace CrowdStrike.Crowdstrike.Outputs
{

    [OutputType]
    public sealed class CloudAwsAccountSensorManagement
    {
        /// <summary>
        /// Enable 1-click sensor deployment
        /// </summary>
        public readonly bool Enabled;

        [OutputConstructor]
        private CloudAwsAccountSensorManagement(bool enabled)
        {
            Enabled = enabled;
        }
    }
}
