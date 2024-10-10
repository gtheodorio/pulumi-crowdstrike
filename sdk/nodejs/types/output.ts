// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface FilevantagePolicyScheduledExclusion {
    /**
     * Description of the scheduled exclusion.
     */
    description: string;
    /**
     * The end date of the scheduled exclusion. Format: YYYY-MM-DD
     */
    endDate: string;
    /**
     * The end time of the scheduled exclusion in 24 hour format. Format: HH:MM
     */
    endTime: string;
    /**
     * Identifier for the scheduled exclusion.
     */
    id: string;
    /**
     * Name of the scheduled exclusion.
     */
    name: string;
    /**
     * A comma separated list of processes to exclude changes from. Example: **&#47;run*me.sh excludes changes made by run*me.sh in any location
     */
    processes: string;
    /**
     * Repeated scheduled exclusion
     */
    repeated?: outputs.FilevantagePolicyScheduledExclusionRepeated;
    /**
     * The start date of the scheduled exclusion. Format: YYYY-MM-DD
     */
    startDate: string;
    /**
     * The start time of the scheduled exclusion in 24 hour format. Format: HH:MM
     */
    startTime: string;
    /**
     * The timezone to use for the time fields. See https://en.wikipedia.org/wiki/List*of*tz*database*time_zones.
     */
    timezone: string;
    /**
     * A comma separated list of users to exclude changes from. Example: user1,user2,admin* excludes changes made by user1, user2, and any user starting with admin
     */
    users: string;
}

export interface FilevantagePolicyScheduledExclusionRepeated {
    /**
     * If the exclusion is all day.
     */
    allDay: boolean;
    /**
     * The days of the month to allow the exclusion. Required if frequency is set to monthly and monthlyOccurrence is set to days. Options: 1-31
     */
    daysOfMonths: number[];
    /**
     * The days of the week to allow the exclusion. Required if frequency is set to weekly or set to monthly and monthlyOccurrence is set to a week. Options: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
     */
    daysOfWeeks: string[];
    /**
     * The end time to end the scheduled exclusion in 24 hour format. Format: HH:MM required if allDay is false
     */
    endTime: string;
    /**
     * The frequency of the exclusion. Options: daily, weekly, monthly
     */
    frequency: string;
    /**
     * The monthly occurrence of the exclusion. Either specify a week (first, second, third, fourth) or set to days to specify days of the month. Options: first, second, third, fourth, days. Required if frequency is set to monthly
     */
    monthlyOccurrence: string;
    /**
     * The start time to allow the scheduled exclusion in 24 hour format. Format: HH:MM required if allDay is false
     */
    startTime: string;
}

export interface FilevantageRuleGroupRule {
    /**
     * Depth below the base path to monitor.
     */
    depth: string;
    /**
     * Description of the filevantage rule.
     */
    description: string;
    /**
     * Enable content capture for the rule. Requires watch*file*write*changes or watch*key*value*set_changes to be enabled.
     */
    enableContentCapture: boolean;
    /**
     * Represents the files, directories, registry keys, or registry values that will be excluded from monitoring.
     */
    exclude: string;
    /**
     * Represents the changes performed by specific processes that will be excluded from monitoring.
     */
    excludeProcesses: string;
    /**
     * Represents the changes performed by specific users that will be excluded from monitoring.
     */
    excludeUsers: string;
    /**
     * List of file names whose content will be monitored. Listed files must match the file include pattern and not match the file exclude pattern.
     */
    fileNames: string[];
    /**
     * Identifier for the filevantage rule.
     */
    id: string;
    /**
     * Represents the files, directories, registry keys, or registry values that will be monitored. Defaults to all (*)
     */
    include: string;
    /**
     * Represents the changes performed by specific processes that will be monitored.
     */
    includeProcesses: string;
    /**
     * Represents the changes performed by specific users that will be monitored.
     */
    includeUsers: string;
    /**
     * Representing the file system or registry path to monitor. All paths must end with the path separator, e.g. c:\windows\ for windows and /usr/bin/ for linux/mac.
     */
    path: string;
    /**
     * Precedence of the rule in the rule group.
     */
    precedence: number;
    /**
     * List of registry values whose content will be monitored. Listed registry values must match the registry include pattern and not match the registry exclude pattern.
     */
    registryValues: string[];
    /**
     * Severity to categorize change events produced by this rule.
     */
    severity: string;
    /**
     * Monitor directory attribute change events.
     */
    watchDirectoryAttributeChanges: boolean;
    /**
     * Monitor directory creation events.
     */
    watchDirectoryCreateChanges: boolean;
    /**
     * Monitor directory deletion events.
     */
    watchDirectoryDeleteChanges: boolean;
    /**
     * Monitor directory permission change events.
     */
    watchDirectoryPermissionChanges: boolean;
    /**
     * Monitor directory rename events.
     */
    watchDirectoryRenameChanges: boolean;
    /**
     * Monitor file attribute change events.
     */
    watchFileAttributeChanges: boolean;
    /**
     * Monitor file creation events.
     */
    watchFileCreateChanges: boolean;
    /**
     * Monitor file deletion events.
     */
    watchFileDeleteChanges: boolean;
    /**
     * Monitor file permission change events.
     */
    watchFilePermissionChanges: boolean;
    /**
     * Monitor file rename events.
     */
    watchFileRenameChanges: boolean;
    /**
     * Monitor file write events.
     */
    watchFileWriteChanges: boolean;
    /**
     * Monitor registry key creation events.
     */
    watchKeyCreateChanges: boolean;
    /**
     * Monitor registry key deletion events.
     */
    watchKeyDeleteChanges: boolean;
    /**
     * Monitor registry key permission change events.
     */
    watchKeyPermissionsChanges: boolean;
    /**
     * Monitor registry key rename events.
     */
    watchKeyRenameChanges: boolean;
    /**
     * Monitor registry value deletion events.
     */
    watchKeyValueDeleteChanges: boolean;
    /**
     * Monitor registry value set events.
     */
    watchKeyValueSetChanges: boolean;
}

export interface GetSensorUpdatePolicyBuildsLinux {
    /**
     * All sensor builds for the specific platform.
     */
    alls: outputs.GetSensorUpdatePolicyBuildsLinuxAll[];
    /**
     * The latest sensor build.
     */
    latest: outputs.GetSensorUpdatePolicyBuildsLinuxLatest;
    /**
     * The n-1 sensor build.
     */
    n1: outputs.GetSensorUpdatePolicyBuildsLinuxN1;
    /**
     * The n-2 sensor build.
     */
    n2: outputs.GetSensorUpdatePolicyBuildsLinuxN2;
}

export interface GetSensorUpdatePolicyBuildsLinuxAll {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsLinuxArm64 {
    /**
     * All sensor builds for the specific platform.
     */
    alls: outputs.GetSensorUpdatePolicyBuildsLinuxArm64All[];
    /**
     * The latest sensor build.
     */
    latest: outputs.GetSensorUpdatePolicyBuildsLinuxArm64Latest;
    /**
     * The n-1 sensor build.
     */
    n1: outputs.GetSensorUpdatePolicyBuildsLinuxArm64N1;
    /**
     * The n-2 sensor build.
     */
    n2: outputs.GetSensorUpdatePolicyBuildsLinuxArm64N2;
}

export interface GetSensorUpdatePolicyBuildsLinuxArm64All {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsLinuxArm64Latest {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsLinuxArm64N1 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsLinuxArm64N2 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsLinuxLatest {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsLinuxN1 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsLinuxN2 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsMac {
    /**
     * All sensor builds for the specific platform.
     */
    alls: outputs.GetSensorUpdatePolicyBuildsMacAll[];
    /**
     * The latest sensor build.
     */
    latest: outputs.GetSensorUpdatePolicyBuildsMacLatest;
    /**
     * The n-1 sensor build.
     */
    n1: outputs.GetSensorUpdatePolicyBuildsMacN1;
    /**
     * The n-2 sensor build.
     */
    n2: outputs.GetSensorUpdatePolicyBuildsMacN2;
}

export interface GetSensorUpdatePolicyBuildsMacAll {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsMacLatest {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsMacN1 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsMacN2 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsWindows {
    /**
     * All sensor builds for the specific platform.
     */
    alls: outputs.GetSensorUpdatePolicyBuildsWindowsAll[];
    /**
     * The latest sensor build.
     */
    latest: outputs.GetSensorUpdatePolicyBuildsWindowsLatest;
    /**
     * The n-1 sensor build.
     */
    n1: outputs.GetSensorUpdatePolicyBuildsWindowsN1;
    /**
     * The n-2 sensor build.
     */
    n2: outputs.GetSensorUpdatePolicyBuildsWindowsN2;
}

export interface GetSensorUpdatePolicyBuildsWindowsAll {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsWindowsLatest {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsWindowsN1 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface GetSensorUpdatePolicyBuildsWindowsN2 {
    /**
     * The build number for a specific sensor version.
     */
    build: string;
    /**
     * The target platform for a the build.
     */
    platform: string;
    /**
     * CrowdStrike Falcon Sensor version.
     */
    sensorVersion: string;
    /**
     * The stage for the build.
     */
    stage: string;
}

export interface PreventionPolicyLinuxCloudAntiMalware {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyLinuxSensorAntiMalware {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyMacCloudAdwareAndPup {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyMacCloudAntiMalware {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyMacSensorAdwareAndPup {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyMacSensorAntiMalware {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyWindowsAdwareAndPup {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyWindowsCloudAntiMalware {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyWindowsCloudAntiMalwareMicrosoftOfficeFiles {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyWindowsCloudAntiMalwareUserInitiated {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyWindowsExtendedUserModeData {
    /**
     * Machine learning level for detection.
     */
    detection: string;
}

export interface PreventionPolicyWindowsSensorAntiMalware {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface PreventionPolicyWindowsSensorAntiMalwareUserInitiated {
    /**
     * Machine learning level for detection.
     */
    detection: string;
    /**
     * Machine learning level for prevention.
     */
    prevention: string;
}

export interface SensorUpdatePolicySchedule {
    /**
     * Enable the scheduler for sensor update policy.
     */
    enabled: boolean;
    /**
     * The time block to prevent sensor updates. Only set when enabled is true.
     */
    timeBlocks?: outputs.SensorUpdatePolicyScheduleTimeBlock[];
    /**
     * The time zones that will be used for the time blocks. Only set when enabled is true.
     */
    timezone?: string;
}

export interface SensorUpdatePolicyScheduleTimeBlock {
    /**
     * The days of the week the time block should be active.
     */
    days: string[];
    /**
     * The end time for the time block in 24HR format. Must be atleast 1 hour more than start_time.
     */
    endTime: string;
    /**
     * The start time for the time block in 24HR format. Must be atleast 1 hour before end_time.
     */
    startTime: string;
}

