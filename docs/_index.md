---
title: CrowdStrike
meta_desc: Provides an overview of the CrowdStrike Provider for Pulumi.
layout: overview
---

The CrowdStrike provider for Pulumi can be used to provision any of the supported cloud resources available in CrowdStrike.

The CrowdStrike provider must be configured with credentials to deploy and update resources in CrowdStrike.

## Example

### Python

```python
import pulumi
import crowdstrike_pulumi

host_group = crowdstrike_pulumi.HostGroup(
    resource_name="hostgroup_1",
    description="A host group created using Pulumi",
    type="dynamic",
    assignment_rule="tags:'SensorGroupingTags/production'+os_version:'Amazon Linux 2'",
    
)
```

### Typescript

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as crowdstrike from "@crowdstrike/pulumi"

//
const hostGroup = new crowdstrike.HostGroup("hostgroup_2", {
    "description": "A host group created using Pulumi",
    "type": "dynamic",
    "assignmentRule": "tags:'SensorGroupingTags/production'+os_version:'Amazon Linux 2'"
}
)

```

### Go

```go
package main

import (
 "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
 "github.com/crowdstrike/pulumi-crowdstrike/sdk/go/crowdstrike"
)

func main() {
 pulumi.Run(func(ctx *pulumi.Context) error {
  hostGroup, err := crowdstrike.NewHostGroup(ctx, "hostgroup_3", &crowdstrike.HostGroupArgs{
   Description:    pulumi.String("A host group created using Pulumi"),
   Type:           pulumi.String("dynamic"),
   AssignmentRule: pulumi.String("tags:'tags:'SensorGroupingTags/production'+os_version:'Amazon Linux 2'"),
  })
  if err != nil {
   return err
  }
  ctx.Export("hostgroup_3", hostGroup)
  return nil
 })
}

```
