#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Python script used to check the rollout status of a given deployment
"""

import argparse
from kubernetes import client, config

# Parse arguements
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--deployment',
                    help='Name of deployment to check',
                    required=True)
parser.add_argument('-n', '--namespace',
                    help='Namespace for deployment',
                    required=False,
                    default='default')
args = parser.parse_args()
deployment = (args.deployment)
namespace = (args.namespace)

# Load kube.cong
config.load_kube_config()

# Establish connection to Kubernetes
kube_conn = client.AppsV1Api()

# Get Specs and Status of Deployment
response = kube_conn.read_namespaced_deployment_status(deployment, namespace)
rollout_status = response.status.conditions[1].message
if 'successfully progressed' in rollout_status:
    print(f"OK, The rollout of {deployment} has succussfully progressed.")
    exit(0)
else:
    print(f"ERROR, The rollout of {deployment}"
          " has failed to progress successfully.")
    exit(2)
