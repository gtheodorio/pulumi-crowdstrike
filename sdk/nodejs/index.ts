// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { CloudAwsAccountArgs, CloudAwsAccountState } from "./cloudAwsAccount";
export type CloudAwsAccount = import("./cloudAwsAccount").CloudAwsAccount;
export const CloudAwsAccount: typeof import("./cloudAwsAccount").CloudAwsAccount = null as any;
utilities.lazyLoad(exports, ["CloudAwsAccount"], () => require("./cloudAwsAccount"));

export { DefaultPreventionPolicyLinuxArgs, DefaultPreventionPolicyLinuxState } from "./defaultPreventionPolicyLinux";
export type DefaultPreventionPolicyLinux = import("./defaultPreventionPolicyLinux").DefaultPreventionPolicyLinux;
export const DefaultPreventionPolicyLinux: typeof import("./defaultPreventionPolicyLinux").DefaultPreventionPolicyLinux = null as any;
utilities.lazyLoad(exports, ["DefaultPreventionPolicyLinux"], () => require("./defaultPreventionPolicyLinux"));

export { DefaultPreventionPolicyMacArgs, DefaultPreventionPolicyMacState } from "./defaultPreventionPolicyMac";
export type DefaultPreventionPolicyMac = import("./defaultPreventionPolicyMac").DefaultPreventionPolicyMac;
export const DefaultPreventionPolicyMac: typeof import("./defaultPreventionPolicyMac").DefaultPreventionPolicyMac = null as any;
utilities.lazyLoad(exports, ["DefaultPreventionPolicyMac"], () => require("./defaultPreventionPolicyMac"));

export { DefaultPreventionPolicyWindowsArgs, DefaultPreventionPolicyWindowsState } from "./defaultPreventionPolicyWindows";
export type DefaultPreventionPolicyWindows = import("./defaultPreventionPolicyWindows").DefaultPreventionPolicyWindows;
export const DefaultPreventionPolicyWindows: typeof import("./defaultPreventionPolicyWindows").DefaultPreventionPolicyWindows = null as any;
utilities.lazyLoad(exports, ["DefaultPreventionPolicyWindows"], () => require("./defaultPreventionPolicyWindows"));

export { DefaultSensorUpdatePolicyArgs, DefaultSensorUpdatePolicyState } from "./defaultSensorUpdatePolicy";
export type DefaultSensorUpdatePolicy = import("./defaultSensorUpdatePolicy").DefaultSensorUpdatePolicy;
export const DefaultSensorUpdatePolicy: typeof import("./defaultSensorUpdatePolicy").DefaultSensorUpdatePolicy = null as any;
utilities.lazyLoad(exports, ["DefaultSensorUpdatePolicy"], () => require("./defaultSensorUpdatePolicy"));

export { FilevantagePolicyArgs, FilevantagePolicyState } from "./filevantagePolicy";
export type FilevantagePolicy = import("./filevantagePolicy").FilevantagePolicy;
export const FilevantagePolicy: typeof import("./filevantagePolicy").FilevantagePolicy = null as any;
utilities.lazyLoad(exports, ["FilevantagePolicy"], () => require("./filevantagePolicy"));

export { FilevantageRuleGroupArgs, FilevantageRuleGroupState } from "./filevantageRuleGroup";
export type FilevantageRuleGroup = import("./filevantageRuleGroup").FilevantageRuleGroup;
export const FilevantageRuleGroup: typeof import("./filevantageRuleGroup").FilevantageRuleGroup = null as any;
utilities.lazyLoad(exports, ["FilevantageRuleGroup"], () => require("./filevantageRuleGroup"));

export { GetCloudAwsAccountArgs, GetCloudAwsAccountResult, GetCloudAwsAccountOutputArgs } from "./getCloudAwsAccount";
export const getCloudAwsAccount: typeof import("./getCloudAwsAccount").getCloudAwsAccount = null as any;
export const getCloudAwsAccountOutput: typeof import("./getCloudAwsAccount").getCloudAwsAccountOutput = null as any;
utilities.lazyLoad(exports, ["getCloudAwsAccount","getCloudAwsAccountOutput"], () => require("./getCloudAwsAccount"));

export { GetSensorUpdatePolicyBuildsResult } from "./getSensorUpdatePolicyBuilds";
export const getSensorUpdatePolicyBuilds: typeof import("./getSensorUpdatePolicyBuilds").getSensorUpdatePolicyBuilds = null as any;
export const getSensorUpdatePolicyBuildsOutput: typeof import("./getSensorUpdatePolicyBuilds").getSensorUpdatePolicyBuildsOutput = null as any;
utilities.lazyLoad(exports, ["getSensorUpdatePolicyBuilds","getSensorUpdatePolicyBuildsOutput"], () => require("./getSensorUpdatePolicyBuilds"));

export { HostGroupArgs, HostGroupState } from "./hostGroup";
export type HostGroup = import("./hostGroup").HostGroup;
export const HostGroup: typeof import("./hostGroup").HostGroup = null as any;
utilities.lazyLoad(exports, ["HostGroup"], () => require("./hostGroup"));

export { PreventionPolicyLinuxArgs, PreventionPolicyLinuxState } from "./preventionPolicyLinux";
export type PreventionPolicyLinux = import("./preventionPolicyLinux").PreventionPolicyLinux;
export const PreventionPolicyLinux: typeof import("./preventionPolicyLinux").PreventionPolicyLinux = null as any;
utilities.lazyLoad(exports, ["PreventionPolicyLinux"], () => require("./preventionPolicyLinux"));

export { PreventionPolicyMacArgs, PreventionPolicyMacState } from "./preventionPolicyMac";
export type PreventionPolicyMac = import("./preventionPolicyMac").PreventionPolicyMac;
export const PreventionPolicyMac: typeof import("./preventionPolicyMac").PreventionPolicyMac = null as any;
utilities.lazyLoad(exports, ["PreventionPolicyMac"], () => require("./preventionPolicyMac"));

export { PreventionPolicyWindowsArgs, PreventionPolicyWindowsState } from "./preventionPolicyWindows";
export type PreventionPolicyWindows = import("./preventionPolicyWindows").PreventionPolicyWindows;
export const PreventionPolicyWindows: typeof import("./preventionPolicyWindows").PreventionPolicyWindows = null as any;
utilities.lazyLoad(exports, ["PreventionPolicyWindows"], () => require("./preventionPolicyWindows"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { SensorUpdatePolicyArgs, SensorUpdatePolicyState } from "./sensorUpdatePolicy";
export type SensorUpdatePolicy = import("./sensorUpdatePolicy").SensorUpdatePolicy;
export const SensorUpdatePolicy: typeof import("./sensorUpdatePolicy").SensorUpdatePolicy = null as any;
utilities.lazyLoad(exports, ["SensorUpdatePolicy"], () => require("./sensorUpdatePolicy"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "crowdstrike:index/cloudAwsAccount:CloudAwsAccount":
                return new CloudAwsAccount(name, <any>undefined, { urn })
            case "crowdstrike:index/defaultPreventionPolicyLinux:DefaultPreventionPolicyLinux":
                return new DefaultPreventionPolicyLinux(name, <any>undefined, { urn })
            case "crowdstrike:index/defaultPreventionPolicyMac:DefaultPreventionPolicyMac":
                return new DefaultPreventionPolicyMac(name, <any>undefined, { urn })
            case "crowdstrike:index/defaultPreventionPolicyWindows:DefaultPreventionPolicyWindows":
                return new DefaultPreventionPolicyWindows(name, <any>undefined, { urn })
            case "crowdstrike:index/defaultSensorUpdatePolicy:DefaultSensorUpdatePolicy":
                return new DefaultSensorUpdatePolicy(name, <any>undefined, { urn })
            case "crowdstrike:index/filevantagePolicy:FilevantagePolicy":
                return new FilevantagePolicy(name, <any>undefined, { urn })
            case "crowdstrike:index/filevantageRuleGroup:FilevantageRuleGroup":
                return new FilevantageRuleGroup(name, <any>undefined, { urn })
            case "crowdstrike:index/hostGroup:HostGroup":
                return new HostGroup(name, <any>undefined, { urn })
            case "crowdstrike:index/preventionPolicyLinux:PreventionPolicyLinux":
                return new PreventionPolicyLinux(name, <any>undefined, { urn })
            case "crowdstrike:index/preventionPolicyMac:PreventionPolicyMac":
                return new PreventionPolicyMac(name, <any>undefined, { urn })
            case "crowdstrike:index/preventionPolicyWindows:PreventionPolicyWindows":
                return new PreventionPolicyWindows(name, <any>undefined, { urn })
            case "crowdstrike:index/sensorUpdatePolicy:SensorUpdatePolicy":
                return new SensorUpdatePolicy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("crowdstrike", "index/cloudAwsAccount", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/defaultPreventionPolicyLinux", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/defaultPreventionPolicyMac", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/defaultPreventionPolicyWindows", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/defaultSensorUpdatePolicy", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/filevantagePolicy", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/filevantageRuleGroup", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/hostGroup", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/preventionPolicyLinux", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/preventionPolicyMac", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/preventionPolicyWindows", _module)
pulumi.runtime.registerResourceModule("crowdstrike", "index/sensorUpdatePolicy", _module)
pulumi.runtime.registerResourcePackage("crowdstrike", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:crowdstrike") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
