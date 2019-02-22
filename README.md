### Description
Check script to monitor the rollout status of a Kubernetes Deployment

---

### How it works
For a given deployment, check that the latest rollout has successfully progressed.

##### Results:
* OK: The last rollout for a deployment has successfully progressed.
* ERROR:  The last rollout for a deployment failed to successfully progressed.

---

### Usag
```console
user@host:~$ ./check_kube_deployment_rollout_status.py -h
usage: check_kube_deployment_rollout_status.py [-h] -d DEPLOYMENT
                                               [-n NAMESPACE]
 
user@host:~$ check_kube_deployment_rollout_status.py -d deployment-foo -n namespace-bar
OK, The rollout of deployment-foo has successfully progressed.

```
---

### Requirements
A working kubernetes configuration via either a config file at ~/.kube/config or the environment variable KUBECONFIG
 
##### Python libraries
* argparse
* kubernetes
