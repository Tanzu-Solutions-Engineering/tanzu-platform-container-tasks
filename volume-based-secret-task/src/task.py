#!/usr/bin/env python

import yaml
import os
import json
import sys
import shutil


def get_object_by_property(array, prop, value):
    for obj in array:
        if obj.get(prop) == value:
            return obj
    return None

schema_file = 'z-mount-schema.yml'
values_file = 'z-mount-values.yml'
overlay_file = 'z-mount-overlay.yml'

extra_comments = """\
#@data/values
---
#@overlay/match-child-defaults missing_ok=True
"""

workspaceDir = os.environ.get('TANZU_BUILD_WORKSPACE_DIR')
configDir = f"{workspaceDir}/output/config/"

print("adding volume mount overlay")
with open(workspaceDir + '/output/containerapp.yml', 'r') as file:
    containerapp = yaml.safe_load(file)

if "ext.apps.tanzu.vmware.com/mount-secret-as-file" in containerapp["metadata"]["annotations"]:
    volumes = {'ext_mount_secret':{'volumes':[]}}
    mounts = containerapp["metadata"]["annotations"]["ext.apps.tanzu.vmware.com/mount-secret-as-file"]
    mountsParsed = mounts.split(",")
    for mount in mountsParsed:
        details = mount.split("=")
        name = details[0]
        path = details[1]
        secretRef = get_object_by_property(containerapp['spec']['secretEnv'], "name",name )
        volume = {'name': name,'secret': secretRef['secretKeyRef']['name'],'path': path,'key': secretRef['secretKeyRef']['key']}
        volumes['ext_mount_secret']['volumes'].append(volume)

    with open(values_file, "w") as file:
        file.write(extra_comments)
        yaml.dump(volumes, file)

    os.makedirs(os.path.dirname(configDir), exist_ok=True)
    shutil.copy2(values_file,configDir)
    shutil.copy2(schema_file,configDir)
    shutil.copy2(overlay_file,configDir)



else:
    print("no secrets found to mount as files")