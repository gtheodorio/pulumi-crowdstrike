---
title: Crowdstrike Installation & Configuration
meta_desc: Information on how to install the Crowdstrike provider.
layout: installation
---

## Installation

The Pulumi Crowdstrike provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@crowdstrike/pulumi`](https://www.npmjs.com/package/@crowdstrike/pulumi)
* Python: [`crowdstrike_pulumi`](https://pypi.org/project/crowdstrike_pulumi/)
* Go: [`github.com/crowdstrike/pulumi-crowdstrike/sdk/go/crowdstrike`](https://pkg.go.dev/github.com/crowdstrike/pulumi-crowdstrike/sdk/go/crowdstrike)
* .NET: [`CrowdStrike.Crowdstrike`](https://www.nuget.org/packages/CrowdStrike.Crowdstrike)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `crowdstrike` provider:

- `crowdstrike:apiKey` (environment: `crowdstrike_API_KEY`) - the API key for `crowdstrike`
- `crowdstrike:region` (environment: `crowdstrike_REGION`) - the region in which to deploy resources

### Provider Binary

The Crowdstrike provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource crowdstrike <version>
```

Replace the version string `<version>` with your desired version.
