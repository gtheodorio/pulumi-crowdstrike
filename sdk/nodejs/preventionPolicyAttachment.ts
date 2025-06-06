// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * This resource allows managing the host groups and ioa rule groups attached to a prevention policy. This resource takes exclusive ownership over the host groups and ioa rule groups assigned to a prevention policy. If you want to fully create or manage a prevention policy please use the `prevention_policy_*` resource for the platform you want to manage.
 *
 * ## API Scopes
 *
 * The following API scopes are required:
 *
 * - Prevention policies | Read & Write
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as crowdstrike from "@crowdstrike/pulumi";
 *
 * const example = new crowdstrike.PreventionPolicyAttachment("example", {
 *     idProperty: "16c0eecfeebb47ce95185fda2e5b3112",
 *     hostGroups: ["df868c936cd443e5a95b2603e2483602"],
 *     ioaRuleGroups: ["507117bc669d41bb93d0a009f557bb23"],
 * });
 * export const preventionPolicyAttachment = example;
 * ```
 *
 * ## Import
 *
 * Prevention Policy Attachment can be imported by specifying the id.
 *
 * ```sh
 * $ pulumi import crowdstrike:index/preventionPolicyAttachment:PreventionPolicyAttachment example 7fb858a949034a0cbca175f660f1e769
 * ```
 */
export class PreventionPolicyAttachment extends pulumi.CustomResource {
    /**
     * Get an existing PreventionPolicyAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PreventionPolicyAttachmentState, opts?: pulumi.CustomResourceOptions): PreventionPolicyAttachment {
        return new PreventionPolicyAttachment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'crowdstrike:index/preventionPolicyAttachment:PreventionPolicyAttachment';

    /**
     * Returns true if the given object is an instance of PreventionPolicyAttachment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PreventionPolicyAttachment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PreventionPolicyAttachment.__pulumiType;
    }

    /**
     * Host Group ids to attach to the prevention policy.
     */
    public readonly hostGroups!: pulumi.Output<string[] | undefined>;
    /**
     * The prevention policy id you want to attach to.
     */
    public readonly idProperty!: pulumi.Output<string>;
    /**
     * IOA Rule Group to attach to the prevention policy.
     */
    public readonly ioaRuleGroups!: pulumi.Output<string[] | undefined>;
    public /*out*/ readonly lastUpdated!: pulumi.Output<string>;

    /**
     * Create a PreventionPolicyAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PreventionPolicyAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PreventionPolicyAttachmentArgs | PreventionPolicyAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PreventionPolicyAttachmentState | undefined;
            resourceInputs["hostGroups"] = state ? state.hostGroups : undefined;
            resourceInputs["idProperty"] = state ? state.idProperty : undefined;
            resourceInputs["ioaRuleGroups"] = state ? state.ioaRuleGroups : undefined;
            resourceInputs["lastUpdated"] = state ? state.lastUpdated : undefined;
        } else {
            const args = argsOrState as PreventionPolicyAttachmentArgs | undefined;
            if ((!args || args.idProperty === undefined) && !opts.urn) {
                throw new Error("Missing required property 'idProperty'");
            }
            resourceInputs["hostGroups"] = args ? args.hostGroups : undefined;
            resourceInputs["idProperty"] = args ? args.idProperty : undefined;
            resourceInputs["ioaRuleGroups"] = args ? args.ioaRuleGroups : undefined;
            resourceInputs["lastUpdated"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PreventionPolicyAttachment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PreventionPolicyAttachment resources.
 */
export interface PreventionPolicyAttachmentState {
    /**
     * Host Group ids to attach to the prevention policy.
     */
    hostGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The prevention policy id you want to attach to.
     */
    idProperty?: pulumi.Input<string>;
    /**
     * IOA Rule Group to attach to the prevention policy.
     */
    ioaRuleGroups?: pulumi.Input<pulumi.Input<string>[]>;
    lastUpdated?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PreventionPolicyAttachment resource.
 */
export interface PreventionPolicyAttachmentArgs {
    /**
     * Host Group ids to attach to the prevention policy.
     */
    hostGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The prevention policy id you want to attach to.
     */
    idProperty: pulumi.Input<string>;
    /**
     * IOA Rule Group to attach to the prevention policy.
     */
    ioaRuleGroups?: pulumi.Input<pulumi.Input<string>[]>;
}
