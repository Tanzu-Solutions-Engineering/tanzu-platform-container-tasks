# Volume Mount Secrets Task

This containertask adds the ability to mount secrets as volumes in the generated k8s deployment from tanzu build. This may be needed for applications that would like to mount specifric types of config files etc. in specific locations on the container filesystem.


## Usage

Follow the general install instructions [here](../README.md#installing-a-container-task) for installing containertasks into the buildplan. The Image that will be used in this process is `ghcr.io/tanzu-solutions-engineering/volume-mount-task`. This task need to be added after `namedTask: kubernetes-deployment.tanzu.vmware.com` and before `namedTask: kubernetes-carvel-package.tanzu.vmware.com`

The specific containertask config should lok like this:

```yaml
- containerTask:
    command:
    - python
    - task.py
    image: ghcr.io/tanzu-solutions-engineering/volume-mount-task
```

Once the containertask is added to the build plan follow the below steps to use with your containerapp.


1. Add your secrets to the `spec.secretEnv` as defined in the [containerapp docs](https://techdocs.broadcom.com/us/en/vmware-tanzu/platform/tanzu-platform/saas/tnz-platform/spaces-how-to-monitor-scale-apps-configure-env-vars.html). 

2. add the custom annotation to tell the secrets where they should be mounted. see the example below

if my  secretEnv looks like this:
```yaml
 secretEnv:
  - name: INI_CONFIG
    secretKeyRef:
      key: myconfig.ini
      name: my-secret
  - name: PROPS
    secretKeyRef:
      key: myconfig.properties
      name: my-secret
```

then the annoation would like like this.  

```yaml
ext.apps.tanzu.vmware.com/mount-secret-as-file: 'INI_CONFIG=/some/path,PROPS=/some/path/2'
```

the result in the container would be that these two file paths exist. `/some/path/myconfig.ini` and `/some/path/2/myconfig.properties`