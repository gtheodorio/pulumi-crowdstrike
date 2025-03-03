# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['CloudAwsAccountArgs', 'CloudAwsAccount']

@pulumi.input_type
class CloudAwsAccountArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 account_type: Optional[pulumi.Input[str]] = None,
                 asset_inventory: Optional[pulumi.Input['CloudAwsAccountAssetInventoryArgs']] = None,
                 deployment_method: Optional[pulumi.Input[str]] = None,
                 dspm: Optional[pulumi.Input['CloudAwsAccountDspmArgs']] = None,
                 idp: Optional[pulumi.Input['CloudAwsAccountIdpArgs']] = None,
                 is_organization_management_account: Optional[pulumi.Input[bool]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 realtime_visibility: Optional[pulumi.Input['CloudAwsAccountRealtimeVisibilityArgs']] = None,
                 sensor_management: Optional[pulumi.Input['CloudAwsAccountSensorManagementArgs']] = None,
                 target_ouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a CloudAwsAccount resource.
        :param pulumi.Input[str] account_id: The AWS Account ID
        :param pulumi.Input[str] account_type: The AWS account type. Value is 'commercial' for Commercial cloud accounts. For GovCloud environments, value can be either 'commercial' or 'gov' depending on the account type
        :param pulumi.Input[bool] is_organization_management_account: Indicates whether this is the management account (formerly known as the root account) of an AWS Organization
        :param pulumi.Input[str] organization_id: The AWS Organization ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_ouses: The list of target Organizational Units
        """
        pulumi.set(__self__, "account_id", account_id)
        if account_type is not None:
            pulumi.set(__self__, "account_type", account_type)
        if asset_inventory is not None:
            pulumi.set(__self__, "asset_inventory", asset_inventory)
        if deployment_method is not None:
            pulumi.set(__self__, "deployment_method", deployment_method)
        if dspm is not None:
            pulumi.set(__self__, "dspm", dspm)
        if idp is not None:
            pulumi.set(__self__, "idp", idp)
        if is_organization_management_account is not None:
            pulumi.set(__self__, "is_organization_management_account", is_organization_management_account)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if realtime_visibility is not None:
            pulumi.set(__self__, "realtime_visibility", realtime_visibility)
        if sensor_management is not None:
            pulumi.set(__self__, "sensor_management", sensor_management)
        if target_ouses is not None:
            pulumi.set(__self__, "target_ouses", target_ouses)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The AWS Account ID
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS account type. Value is 'commercial' for Commercial cloud accounts. For GovCloud environments, value can be either 'commercial' or 'gov' depending on the account type
        """
        return pulumi.get(self, "account_type")

    @account_type.setter
    def account_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_type", value)

    @property
    @pulumi.getter(name="assetInventory")
    def asset_inventory(self) -> Optional[pulumi.Input['CloudAwsAccountAssetInventoryArgs']]:
        return pulumi.get(self, "asset_inventory")

    @asset_inventory.setter
    def asset_inventory(self, value: Optional[pulumi.Input['CloudAwsAccountAssetInventoryArgs']]):
        pulumi.set(self, "asset_inventory", value)

    @property
    @pulumi.getter(name="deploymentMethod")
    def deployment_method(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployment_method")

    @deployment_method.setter
    def deployment_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_method", value)

    @property
    @pulumi.getter
    def dspm(self) -> Optional[pulumi.Input['CloudAwsAccountDspmArgs']]:
        return pulumi.get(self, "dspm")

    @dspm.setter
    def dspm(self, value: Optional[pulumi.Input['CloudAwsAccountDspmArgs']]):
        pulumi.set(self, "dspm", value)

    @property
    @pulumi.getter
    def idp(self) -> Optional[pulumi.Input['CloudAwsAccountIdpArgs']]:
        return pulumi.get(self, "idp")

    @idp.setter
    def idp(self, value: Optional[pulumi.Input['CloudAwsAccountIdpArgs']]):
        pulumi.set(self, "idp", value)

    @property
    @pulumi.getter(name="isOrganizationManagementAccount")
    def is_organization_management_account(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this is the management account (formerly known as the root account) of an AWS Organization
        """
        return pulumi.get(self, "is_organization_management_account")

    @is_organization_management_account.setter
    def is_organization_management_account(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_organization_management_account", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Organization ID
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="realtimeVisibility")
    def realtime_visibility(self) -> Optional[pulumi.Input['CloudAwsAccountRealtimeVisibilityArgs']]:
        return pulumi.get(self, "realtime_visibility")

    @realtime_visibility.setter
    def realtime_visibility(self, value: Optional[pulumi.Input['CloudAwsAccountRealtimeVisibilityArgs']]):
        pulumi.set(self, "realtime_visibility", value)

    @property
    @pulumi.getter(name="sensorManagement")
    def sensor_management(self) -> Optional[pulumi.Input['CloudAwsAccountSensorManagementArgs']]:
        return pulumi.get(self, "sensor_management")

    @sensor_management.setter
    def sensor_management(self, value: Optional[pulumi.Input['CloudAwsAccountSensorManagementArgs']]):
        pulumi.set(self, "sensor_management", value)

    @property
    @pulumi.getter(name="targetOuses")
    def target_ouses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of target Organizational Units
        """
        return pulumi.get(self, "target_ouses")

    @target_ouses.setter
    def target_ouses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "target_ouses", value)


@pulumi.input_type
class _CloudAwsAccountState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 account_type: Optional[pulumi.Input[str]] = None,
                 asset_inventory: Optional[pulumi.Input['CloudAwsAccountAssetInventoryArgs']] = None,
                 cloudtrail_bucket_name: Optional[pulumi.Input[str]] = None,
                 deployment_method: Optional[pulumi.Input[str]] = None,
                 dspm: Optional[pulumi.Input['CloudAwsAccountDspmArgs']] = None,
                 dspm_role_arn: Optional[pulumi.Input[str]] = None,
                 eventbus_arn: Optional[pulumi.Input[str]] = None,
                 eventbus_name: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 iam_role_arn: Optional[pulumi.Input[str]] = None,
                 idp: Optional[pulumi.Input['CloudAwsAccountIdpArgs']] = None,
                 intermediate_role_arn: Optional[pulumi.Input[str]] = None,
                 is_organization_management_account: Optional[pulumi.Input[bool]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 realtime_visibility: Optional[pulumi.Input['CloudAwsAccountRealtimeVisibilityArgs']] = None,
                 sensor_management: Optional[pulumi.Input['CloudAwsAccountSensorManagementArgs']] = None,
                 target_ouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering CloudAwsAccount resources.
        :param pulumi.Input[str] account_id: The AWS Account ID
        :param pulumi.Input[str] account_type: The AWS account type. Value is 'commercial' for Commercial cloud accounts. For GovCloud environments, value can be either 'commercial' or 'gov' depending on the account type
        :param pulumi.Input[str] cloudtrail_bucket_name: The name of the CloudTrail S3 bucket used for real-time visibility
        :param pulumi.Input[str] dspm_role_arn: The ARN of the IAM role to be used by CrowdStrike Data Security Posture Management
        :param pulumi.Input[str] eventbus_arn: The ARN of the Amazon EventBridge used by CrowdStrike to forward messages
        :param pulumi.Input[str] eventbus_name: The name of the Amazon EventBridge used by CrowdStrike to forward messages
        :param pulumi.Input[str] external_id: The external ID used to assume the AWS IAM role
        :param pulumi.Input[str] iam_role_arn: The ARN of the AWS IAM role used to access this AWS account
        :param pulumi.Input[str] intermediate_role_arn: The ARN of the intermediate role used to assume the AWS IAM role
        :param pulumi.Input[bool] is_organization_management_account: Indicates whether this is the management account (formerly known as the root account) of an AWS Organization
        :param pulumi.Input[str] organization_id: The AWS Organization ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_ouses: The list of target Organizational Units
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if account_type is not None:
            pulumi.set(__self__, "account_type", account_type)
        if asset_inventory is not None:
            pulumi.set(__self__, "asset_inventory", asset_inventory)
        if cloudtrail_bucket_name is not None:
            pulumi.set(__self__, "cloudtrail_bucket_name", cloudtrail_bucket_name)
        if deployment_method is not None:
            pulumi.set(__self__, "deployment_method", deployment_method)
        if dspm is not None:
            pulumi.set(__self__, "dspm", dspm)
        if dspm_role_arn is not None:
            pulumi.set(__self__, "dspm_role_arn", dspm_role_arn)
        if eventbus_arn is not None:
            pulumi.set(__self__, "eventbus_arn", eventbus_arn)
        if eventbus_name is not None:
            pulumi.set(__self__, "eventbus_name", eventbus_name)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if iam_role_arn is not None:
            pulumi.set(__self__, "iam_role_arn", iam_role_arn)
        if idp is not None:
            pulumi.set(__self__, "idp", idp)
        if intermediate_role_arn is not None:
            pulumi.set(__self__, "intermediate_role_arn", intermediate_role_arn)
        if is_organization_management_account is not None:
            pulumi.set(__self__, "is_organization_management_account", is_organization_management_account)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if realtime_visibility is not None:
            pulumi.set(__self__, "realtime_visibility", realtime_visibility)
        if sensor_management is not None:
            pulumi.set(__self__, "sensor_management", sensor_management)
        if target_ouses is not None:
            pulumi.set(__self__, "target_ouses", target_ouses)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Account ID
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS account type. Value is 'commercial' for Commercial cloud accounts. For GovCloud environments, value can be either 'commercial' or 'gov' depending on the account type
        """
        return pulumi.get(self, "account_type")

    @account_type.setter
    def account_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_type", value)

    @property
    @pulumi.getter(name="assetInventory")
    def asset_inventory(self) -> Optional[pulumi.Input['CloudAwsAccountAssetInventoryArgs']]:
        return pulumi.get(self, "asset_inventory")

    @asset_inventory.setter
    def asset_inventory(self, value: Optional[pulumi.Input['CloudAwsAccountAssetInventoryArgs']]):
        pulumi.set(self, "asset_inventory", value)

    @property
    @pulumi.getter(name="cloudtrailBucketName")
    def cloudtrail_bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the CloudTrail S3 bucket used for real-time visibility
        """
        return pulumi.get(self, "cloudtrail_bucket_name")

    @cloudtrail_bucket_name.setter
    def cloudtrail_bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloudtrail_bucket_name", value)

    @property
    @pulumi.getter(name="deploymentMethod")
    def deployment_method(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployment_method")

    @deployment_method.setter
    def deployment_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_method", value)

    @property
    @pulumi.getter
    def dspm(self) -> Optional[pulumi.Input['CloudAwsAccountDspmArgs']]:
        return pulumi.get(self, "dspm")

    @dspm.setter
    def dspm(self, value: Optional[pulumi.Input['CloudAwsAccountDspmArgs']]):
        pulumi.set(self, "dspm", value)

    @property
    @pulumi.getter(name="dspmRoleArn")
    def dspm_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the IAM role to be used by CrowdStrike Data Security Posture Management
        """
        return pulumi.get(self, "dspm_role_arn")

    @dspm_role_arn.setter
    def dspm_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dspm_role_arn", value)

    @property
    @pulumi.getter(name="eventbusArn")
    def eventbus_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the Amazon EventBridge used by CrowdStrike to forward messages
        """
        return pulumi.get(self, "eventbus_arn")

    @eventbus_arn.setter
    def eventbus_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventbus_arn", value)

    @property
    @pulumi.getter(name="eventbusName")
    def eventbus_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Amazon EventBridge used by CrowdStrike to forward messages
        """
        return pulumi.get(self, "eventbus_name")

    @eventbus_name.setter
    def eventbus_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eventbus_name", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        The external ID used to assume the AWS IAM role
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the AWS IAM role used to access this AWS account
        """
        return pulumi.get(self, "iam_role_arn")

    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iam_role_arn", value)

    @property
    @pulumi.getter
    def idp(self) -> Optional[pulumi.Input['CloudAwsAccountIdpArgs']]:
        return pulumi.get(self, "idp")

    @idp.setter
    def idp(self, value: Optional[pulumi.Input['CloudAwsAccountIdpArgs']]):
        pulumi.set(self, "idp", value)

    @property
    @pulumi.getter(name="intermediateRoleArn")
    def intermediate_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the intermediate role used to assume the AWS IAM role
        """
        return pulumi.get(self, "intermediate_role_arn")

    @intermediate_role_arn.setter
    def intermediate_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "intermediate_role_arn", value)

    @property
    @pulumi.getter(name="isOrganizationManagementAccount")
    def is_organization_management_account(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this is the management account (formerly known as the root account) of an AWS Organization
        """
        return pulumi.get(self, "is_organization_management_account")

    @is_organization_management_account.setter
    def is_organization_management_account(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_organization_management_account", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Organization ID
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="realtimeVisibility")
    def realtime_visibility(self) -> Optional[pulumi.Input['CloudAwsAccountRealtimeVisibilityArgs']]:
        return pulumi.get(self, "realtime_visibility")

    @realtime_visibility.setter
    def realtime_visibility(self, value: Optional[pulumi.Input['CloudAwsAccountRealtimeVisibilityArgs']]):
        pulumi.set(self, "realtime_visibility", value)

    @property
    @pulumi.getter(name="sensorManagement")
    def sensor_management(self) -> Optional[pulumi.Input['CloudAwsAccountSensorManagementArgs']]:
        return pulumi.get(self, "sensor_management")

    @sensor_management.setter
    def sensor_management(self, value: Optional[pulumi.Input['CloudAwsAccountSensorManagementArgs']]):
        pulumi.set(self, "sensor_management", value)

    @property
    @pulumi.getter(name="targetOuses")
    def target_ouses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of target Organizational Units
        """
        return pulumi.get(self, "target_ouses")

    @target_ouses.setter
    def target_ouses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "target_ouses", value)


class CloudAwsAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 account_type: Optional[pulumi.Input[str]] = None,
                 asset_inventory: Optional[pulumi.Input[Union['CloudAwsAccountAssetInventoryArgs', 'CloudAwsAccountAssetInventoryArgsDict']]] = None,
                 deployment_method: Optional[pulumi.Input[str]] = None,
                 dspm: Optional[pulumi.Input[Union['CloudAwsAccountDspmArgs', 'CloudAwsAccountDspmArgsDict']]] = None,
                 idp: Optional[pulumi.Input[Union['CloudAwsAccountIdpArgs', 'CloudAwsAccountIdpArgsDict']]] = None,
                 is_organization_management_account: Optional[pulumi.Input[bool]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 realtime_visibility: Optional[pulumi.Input[Union['CloudAwsAccountRealtimeVisibilityArgs', 'CloudAwsAccountRealtimeVisibilityArgsDict']]] = None,
                 sensor_management: Optional[pulumi.Input[Union['CloudAwsAccountSensorManagementArgs', 'CloudAwsAccountSensorManagementArgsDict']]] = None,
                 target_ouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        This resource allows management of an AWS account in Falcon.

        ## API Scopes

        The following API scopes are required:

        - Cloud security AWS registration | Read & Write
        - CSPM registration | Read & Write

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The AWS Account ID
        :param pulumi.Input[str] account_type: The AWS account type. Value is 'commercial' for Commercial cloud accounts. For GovCloud environments, value can be either 'commercial' or 'gov' depending on the account type
        :param pulumi.Input[bool] is_organization_management_account: Indicates whether this is the management account (formerly known as the root account) of an AWS Organization
        :param pulumi.Input[str] organization_id: The AWS Organization ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_ouses: The list of target Organizational Units
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CloudAwsAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows management of an AWS account in Falcon.

        ## API Scopes

        The following API scopes are required:

        - Cloud security AWS registration | Read & Write
        - CSPM registration | Read & Write

        :param str resource_name: The name of the resource.
        :param CloudAwsAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudAwsAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 account_type: Optional[pulumi.Input[str]] = None,
                 asset_inventory: Optional[pulumi.Input[Union['CloudAwsAccountAssetInventoryArgs', 'CloudAwsAccountAssetInventoryArgsDict']]] = None,
                 deployment_method: Optional[pulumi.Input[str]] = None,
                 dspm: Optional[pulumi.Input[Union['CloudAwsAccountDspmArgs', 'CloudAwsAccountDspmArgsDict']]] = None,
                 idp: Optional[pulumi.Input[Union['CloudAwsAccountIdpArgs', 'CloudAwsAccountIdpArgsDict']]] = None,
                 is_organization_management_account: Optional[pulumi.Input[bool]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 realtime_visibility: Optional[pulumi.Input[Union['CloudAwsAccountRealtimeVisibilityArgs', 'CloudAwsAccountRealtimeVisibilityArgsDict']]] = None,
                 sensor_management: Optional[pulumi.Input[Union['CloudAwsAccountSensorManagementArgs', 'CloudAwsAccountSensorManagementArgsDict']]] = None,
                 target_ouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudAwsAccountArgs.__new__(CloudAwsAccountArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["account_type"] = account_type
            __props__.__dict__["asset_inventory"] = asset_inventory
            __props__.__dict__["deployment_method"] = deployment_method
            __props__.__dict__["dspm"] = dspm
            __props__.__dict__["idp"] = idp
            __props__.__dict__["is_organization_management_account"] = is_organization_management_account
            __props__.__dict__["organization_id"] = organization_id
            __props__.__dict__["realtime_visibility"] = realtime_visibility
            __props__.__dict__["sensor_management"] = sensor_management
            __props__.__dict__["target_ouses"] = target_ouses
            __props__.__dict__["cloudtrail_bucket_name"] = None
            __props__.__dict__["dspm_role_arn"] = None
            __props__.__dict__["eventbus_arn"] = None
            __props__.__dict__["eventbus_name"] = None
            __props__.__dict__["external_id"] = None
            __props__.__dict__["iam_role_arn"] = None
            __props__.__dict__["intermediate_role_arn"] = None
        super(CloudAwsAccount, __self__).__init__(
            'crowdstrike:index/cloudAwsAccount:CloudAwsAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            account_type: Optional[pulumi.Input[str]] = None,
            asset_inventory: Optional[pulumi.Input[Union['CloudAwsAccountAssetInventoryArgs', 'CloudAwsAccountAssetInventoryArgsDict']]] = None,
            cloudtrail_bucket_name: Optional[pulumi.Input[str]] = None,
            deployment_method: Optional[pulumi.Input[str]] = None,
            dspm: Optional[pulumi.Input[Union['CloudAwsAccountDspmArgs', 'CloudAwsAccountDspmArgsDict']]] = None,
            dspm_role_arn: Optional[pulumi.Input[str]] = None,
            eventbus_arn: Optional[pulumi.Input[str]] = None,
            eventbus_name: Optional[pulumi.Input[str]] = None,
            external_id: Optional[pulumi.Input[str]] = None,
            iam_role_arn: Optional[pulumi.Input[str]] = None,
            idp: Optional[pulumi.Input[Union['CloudAwsAccountIdpArgs', 'CloudAwsAccountIdpArgsDict']]] = None,
            intermediate_role_arn: Optional[pulumi.Input[str]] = None,
            is_organization_management_account: Optional[pulumi.Input[bool]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            realtime_visibility: Optional[pulumi.Input[Union['CloudAwsAccountRealtimeVisibilityArgs', 'CloudAwsAccountRealtimeVisibilityArgsDict']]] = None,
            sensor_management: Optional[pulumi.Input[Union['CloudAwsAccountSensorManagementArgs', 'CloudAwsAccountSensorManagementArgsDict']]] = None,
            target_ouses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'CloudAwsAccount':
        """
        Get an existing CloudAwsAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The AWS Account ID
        :param pulumi.Input[str] account_type: The AWS account type. Value is 'commercial' for Commercial cloud accounts. For GovCloud environments, value can be either 'commercial' or 'gov' depending on the account type
        :param pulumi.Input[str] cloudtrail_bucket_name: The name of the CloudTrail S3 bucket used for real-time visibility
        :param pulumi.Input[str] dspm_role_arn: The ARN of the IAM role to be used by CrowdStrike Data Security Posture Management
        :param pulumi.Input[str] eventbus_arn: The ARN of the Amazon EventBridge used by CrowdStrike to forward messages
        :param pulumi.Input[str] eventbus_name: The name of the Amazon EventBridge used by CrowdStrike to forward messages
        :param pulumi.Input[str] external_id: The external ID used to assume the AWS IAM role
        :param pulumi.Input[str] iam_role_arn: The ARN of the AWS IAM role used to access this AWS account
        :param pulumi.Input[str] intermediate_role_arn: The ARN of the intermediate role used to assume the AWS IAM role
        :param pulumi.Input[bool] is_organization_management_account: Indicates whether this is the management account (formerly known as the root account) of an AWS Organization
        :param pulumi.Input[str] organization_id: The AWS Organization ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_ouses: The list of target Organizational Units
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CloudAwsAccountState.__new__(_CloudAwsAccountState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["account_type"] = account_type
        __props__.__dict__["asset_inventory"] = asset_inventory
        __props__.__dict__["cloudtrail_bucket_name"] = cloudtrail_bucket_name
        __props__.__dict__["deployment_method"] = deployment_method
        __props__.__dict__["dspm"] = dspm
        __props__.__dict__["dspm_role_arn"] = dspm_role_arn
        __props__.__dict__["eventbus_arn"] = eventbus_arn
        __props__.__dict__["eventbus_name"] = eventbus_name
        __props__.__dict__["external_id"] = external_id
        __props__.__dict__["iam_role_arn"] = iam_role_arn
        __props__.__dict__["idp"] = idp
        __props__.__dict__["intermediate_role_arn"] = intermediate_role_arn
        __props__.__dict__["is_organization_management_account"] = is_organization_management_account
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["realtime_visibility"] = realtime_visibility
        __props__.__dict__["sensor_management"] = sensor_management
        __props__.__dict__["target_ouses"] = target_ouses
        return CloudAwsAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The AWS Account ID
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> pulumi.Output[str]:
        """
        The AWS account type. Value is 'commercial' for Commercial cloud accounts. For GovCloud environments, value can be either 'commercial' or 'gov' depending on the account type
        """
        return pulumi.get(self, "account_type")

    @property
    @pulumi.getter(name="assetInventory")
    def asset_inventory(self) -> pulumi.Output['outputs.CloudAwsAccountAssetInventory']:
        return pulumi.get(self, "asset_inventory")

    @property
    @pulumi.getter(name="cloudtrailBucketName")
    def cloudtrail_bucket_name(self) -> pulumi.Output[str]:
        """
        The name of the CloudTrail S3 bucket used for real-time visibility
        """
        return pulumi.get(self, "cloudtrail_bucket_name")

    @property
    @pulumi.getter(name="deploymentMethod")
    def deployment_method(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_method")

    @property
    @pulumi.getter
    def dspm(self) -> pulumi.Output['outputs.CloudAwsAccountDspm']:
        return pulumi.get(self, "dspm")

    @property
    @pulumi.getter(name="dspmRoleArn")
    def dspm_role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the IAM role to be used by CrowdStrike Data Security Posture Management
        """
        return pulumi.get(self, "dspm_role_arn")

    @property
    @pulumi.getter(name="eventbusArn")
    def eventbus_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Amazon EventBridge used by CrowdStrike to forward messages
        """
        return pulumi.get(self, "eventbus_arn")

    @property
    @pulumi.getter(name="eventbusName")
    def eventbus_name(self) -> pulumi.Output[str]:
        """
        The name of the Amazon EventBridge used by CrowdStrike to forward messages
        """
        return pulumi.get(self, "eventbus_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        """
        The external ID used to assume the AWS IAM role
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the AWS IAM role used to access this AWS account
        """
        return pulumi.get(self, "iam_role_arn")

    @property
    @pulumi.getter
    def idp(self) -> pulumi.Output['outputs.CloudAwsAccountIdp']:
        return pulumi.get(self, "idp")

    @property
    @pulumi.getter(name="intermediateRoleArn")
    def intermediate_role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the intermediate role used to assume the AWS IAM role
        """
        return pulumi.get(self, "intermediate_role_arn")

    @property
    @pulumi.getter(name="isOrganizationManagementAccount")
    def is_organization_management_account(self) -> pulumi.Output[bool]:
        """
        Indicates whether this is the management account (formerly known as the root account) of an AWS Organization
        """
        return pulumi.get(self, "is_organization_management_account")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The AWS Organization ID
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="realtimeVisibility")
    def realtime_visibility(self) -> pulumi.Output['outputs.CloudAwsAccountRealtimeVisibility']:
        return pulumi.get(self, "realtime_visibility")

    @property
    @pulumi.getter(name="sensorManagement")
    def sensor_management(self) -> pulumi.Output['outputs.CloudAwsAccountSensorManagement']:
        return pulumi.get(self, "sensor_management")

    @property
    @pulumi.getter(name="targetOuses")
    def target_ouses(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of target Organizational Units
        """
        return pulumi.get(self, "target_ouses")

