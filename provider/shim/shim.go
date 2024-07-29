package shim

import (
	"github.com/crowdstrike/terraform-provider-crowdstrike/internal/provider"
	tf "github.com/hashicorp/terraform-plugin-framework/provider"
)

func NewProvider() tf.Provider {
	return provider.New()
}
