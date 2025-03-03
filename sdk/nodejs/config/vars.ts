// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("crowdstrike");

/**
 * Falcon Client Id for authenticating to the CrowdStrike APIs. Will use FALCON_CLIENT_ID environment variable when left
 * blank.
 */
export declare const clientId: string | undefined;
Object.defineProperty(exports, "clientId", {
    get() {
        return __config.get("clientId");
    },
    enumerable: true,
});

/**
 * Falcon Client Secret used for authenticating to the CrowdStrike APIs. Will use FALCON_CLIENT_SECRET environment variable
 * when left blank.
 */
export declare const clientSecret: string | undefined;
Object.defineProperty(exports, "clientSecret", {
    get() {
        return __config.get("clientSecret");
    },
    enumerable: true,
});

/**
 * Falcon Cloud to authenticate to. Valid values are autodiscover, us-1, us-2, eu-1, us-gov-1. Will use FALCON_CLOUD
 * environment variable when left blank.
 */
export declare const cloud: string | undefined;
Object.defineProperty(exports, "cloud", {
    get() {
        return __config.get("cloud");
    },
    enumerable: true,
});

/**
 * For MSSP Master CIDs, optionally lock the token to act on behalf of this member CID
 */
export declare const memberCid: string | undefined;
Object.defineProperty(exports, "memberCid", {
    get() {
        return __config.get("memberCid");
    },
    enumerable: true,
});

