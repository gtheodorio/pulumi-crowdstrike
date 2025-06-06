// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace CrowdStrike.Crowdstrike
{
    /// <summary>
    /// This resource allows managing the host groups and ioa rule groups attached to a prevention policy. This resource takes exclusive ownership over the host groups and ioa rule groups assigned to a prevention policy. If you want to fully create or manage a prevention policy please use the `prevention_policy_*` resource for the platform you want to manage.
    /// 
    /// ## API Scopes
    /// 
    /// The following API scopes are required:
    /// 
    /// - Prevention policies | Read &amp; Write
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Crowdstrike = CrowdStrike.Crowdstrike;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Crowdstrike.PreventionPolicyAttachment("example", new()
    ///     {
    ///         IdProperty = "16c0eecfeebb47ce95185fda2e5b3112",
    ///         HostGroups = new[]
    ///         {
    ///             "df868c936cd443e5a95b2603e2483602",
    ///         },
    ///         IoaRuleGroups = new[]
    ///         {
    ///             "507117bc669d41bb93d0a009f557bb23",
    ///         },
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["preventionPolicyAttachment"] = example,
    ///     };
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Prevention Policy Attachment can be imported by specifying the id.
    /// 
    /// ```sh
    /// $ pulumi import crowdstrike:index/preventionPolicyAttachment:PreventionPolicyAttachment example 7fb858a949034a0cbca175f660f1e769
    /// ```
    /// </summary>
    [CrowdstrikeResourceType("crowdstrike:index/preventionPolicyAttachment:PreventionPolicyAttachment")]
    public partial class PreventionPolicyAttachment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Host Group ids to attach to the prevention policy.
        /// </summary>
        [Output("hostGroups")]
        public Output<ImmutableArray<string>> HostGroups { get; private set; } = null!;

        /// <summary>
        /// The prevention policy id you want to attach to.
        /// </summary>
        [Output("idProperty")]
        public Output<string> IdProperty { get; private set; } = null!;

        /// <summary>
        /// IOA Rule Group to attach to the prevention policy.
        /// </summary>
        [Output("ioaRuleGroups")]
        public Output<ImmutableArray<string>> IoaRuleGroups { get; private set; } = null!;

        [Output("lastUpdated")]
        public Output<string> LastUpdated { get; private set; } = null!;


        /// <summary>
        /// Create a PreventionPolicyAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PreventionPolicyAttachment(string name, PreventionPolicyAttachmentArgs args, CustomResourceOptions? options = null)
            : base("crowdstrike:index/preventionPolicyAttachment:PreventionPolicyAttachment", name, args ?? new PreventionPolicyAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PreventionPolicyAttachment(string name, Input<string> id, PreventionPolicyAttachmentState? state = null, CustomResourceOptions? options = null)
            : base("crowdstrike:index/preventionPolicyAttachment:PreventionPolicyAttachment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/crowdstrike/pulumi-crowdstrike",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PreventionPolicyAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PreventionPolicyAttachment Get(string name, Input<string> id, PreventionPolicyAttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new PreventionPolicyAttachment(name, id, state, options);
        }
    }

    public sealed class PreventionPolicyAttachmentArgs : global::Pulumi.ResourceArgs
    {
        [Input("hostGroups")]
        private InputList<string>? _hostGroups;

        /// <summary>
        /// Host Group ids to attach to the prevention policy.
        /// </summary>
        public InputList<string> HostGroups
        {
            get => _hostGroups ?? (_hostGroups = new InputList<string>());
            set => _hostGroups = value;
        }

        /// <summary>
        /// The prevention policy id you want to attach to.
        /// </summary>
        [Input("idProperty", required: true)]
        public Input<string> IdProperty { get; set; } = null!;

        [Input("ioaRuleGroups")]
        private InputList<string>? _ioaRuleGroups;

        /// <summary>
        /// IOA Rule Group to attach to the prevention policy.
        /// </summary>
        public InputList<string> IoaRuleGroups
        {
            get => _ioaRuleGroups ?? (_ioaRuleGroups = new InputList<string>());
            set => _ioaRuleGroups = value;
        }

        public PreventionPolicyAttachmentArgs()
        {
        }
        public static new PreventionPolicyAttachmentArgs Empty => new PreventionPolicyAttachmentArgs();
    }

    public sealed class PreventionPolicyAttachmentState : global::Pulumi.ResourceArgs
    {
        [Input("hostGroups")]
        private InputList<string>? _hostGroups;

        /// <summary>
        /// Host Group ids to attach to the prevention policy.
        /// </summary>
        public InputList<string> HostGroups
        {
            get => _hostGroups ?? (_hostGroups = new InputList<string>());
            set => _hostGroups = value;
        }

        /// <summary>
        /// The prevention policy id you want to attach to.
        /// </summary>
        [Input("idProperty")]
        public Input<string>? IdProperty { get; set; }

        [Input("ioaRuleGroups")]
        private InputList<string>? _ioaRuleGroups;

        /// <summary>
        /// IOA Rule Group to attach to the prevention policy.
        /// </summary>
        public InputList<string> IoaRuleGroups
        {
            get => _ioaRuleGroups ?? (_ioaRuleGroups = new InputList<string>());
            set => _ioaRuleGroups = value;
        }

        [Input("lastUpdated")]
        public Input<string>? LastUpdated { get; set; }

        public PreventionPolicyAttachmentState()
        {
        }
        public static new PreventionPolicyAttachmentState Empty => new PreventionPolicyAttachmentState();
    }
}
