// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

package examples

import (
	"os"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getClientId(t *testing.T) string {
	client_id := os.Getenv("FALCON_CLIENT_ID")
	if client_id == "" {
		t.Skipf("Skipping test due to missing CROWDSTRIKE_FALCON_CLIENT_ID environment variable")
	}

	return client_id
}

func getClientSecret(t *testing.T) string {
	client_secret := os.Getenv("FALCON_CLIENT_SECRET")
	if client_secret == "" {
		t.Skipf("Skipping test due to missing CROWDSTRIKE_FALCON_CLIENT_SECRET environment variable")
	}

	return client_secret
}

func getCwd(t *testing.T) string {
	cwd, err := os.Getwd()
	if err != nil {
		t.FailNow()
	}

	return cwd
}

func getBaseOptions(t *testing.T) integration.ProgramTestOptions {
	client_id := getClientId(t)
	client_secret := getClientSecret(t)
	return integration.ProgramTestOptions{
		Config: map[string]string{
			"client_id":     client_id,
			"client_secret": client_secret,
		},
	}
}
