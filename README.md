# Tanzu Platform Container Tasks

This repo is a shared collection of commonly used/requested container task. A container task is a way to extend the `tanzu build` process in order to customize the build output.

These are not officially supported by Tanzu.


## Tasks

[volume mounted secrets](volume-based-secret-task/README.md) -  mounts secrets from `secretEnv` as files on the container file system.



## Installing a container task

This section can be used to install container tasks into your existing `containerappbuildplans` in tanzu platform. The platform comes with an existing `containerappbuildplan` in your project context called `simple.tanzu.vmware.com`.

There are two options when adding containertasks. Option oen is to edit and existing runtime in the `contianerappbuildplan` , this could be usefull if you want your task to immediately by available to all `tanzu build` executions without having to specify anything. however this will then be a default. Option two is to add an additional runtime so that it can be used on demand.


To add a container task add the following yaml to either an existing runtime or create a new runtime with the yaml below.


1. edit the build plane

```bash

kubectl edit containerappbuildplans simple.tanzu.vmware.com
```

2. add the below yaml with the correct replacements in the existing runtime or a new runtime. If using a task from this repo, the task specific docs should have the details on the image path that should be used. This will go into the `spec.runtimes[0].steps` section of the speciifc runtime.

```yaml
- name: <name-of-task>
  containerTask:
    image: <full-path-to-image-in-regsitry>
    command: [] #some command to run
```