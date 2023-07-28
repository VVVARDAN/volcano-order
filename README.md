**README**

This README file provides an overview of the `main.py` Python script and the `vcjob.yaml` YAML file. These files are part of a Kubernetes environment and are designed to work together to run a job using the Volcano scheduler.

### main.py

The `main.py` script is a Python script designed to run as an init container within a Kubernetes environment. The purpose of this script is to wait for the "master" pod to become running before allowing the worker pods to proceed. The script checks the status of the "master" pod within the same namespace, and if the "master" pod is running, it exits, enabling the worker pods to continue their tasks. The script utilizes the Kubernetes Python client to interact with the Kubernetes API.

**TODO section:**
There is a TODO section in the `main.py` script, where you can specify parameters that the script can accept. Currently, the parameters are commented out, and the script waits for the "master" pod without any specific parameters.

### vcjob.yaml

The `vcjob.yaml` YAML file is a Kubernetes Job definition that utilizes the Volcano scheduler to manage the execution of the job. The Job consists of two tasks: "master" and "worker," where "worker" depends on the successful completion of the "master" task.

**Job Details:**
- Name: job-test-v506
- Task Topology: "master" and "worker" tasks are topologically ordered, meaning "worker" will not start until "master" is completed successfully.
- Task Anti-Affinity: "master" and "worker" tasks are anti-affine, meaning they will not be scheduled on the same node.

**Master Task:**
- The "master" task has one replica and runs an `nginx` container, which sleeps for 0.2 minutes.
- Resource Requests and Limits: The "master" task requests 50Mi of memory and 1 CPU, with a limit of 100Mi memory and 1 CPU.
- Restart Policy: The "master" task has a restart policy of "Never."

**Worker Task:**
- The "worker" task has three replicas and runs an `nginx` container, which sleeps for 0.2 minutes.
- Resource Requests and Limits: The "worker" task requests 5Mi of memory and 1 CPU, with a limit of 10Mi memory and 1 CPU.
- Restart Policy: The "worker" task has a restart policy of "Never."

**TODO section:**
There is a TODO section in the "worker" task definition where you can specify environment variables for the `my_init` init container. Currently, the environment variable `PARAMS` is commented out. You can uncomment this section and provide specific parameters for the `my_init` init container.

### Running the Job

To run the job, follow these steps:

1. Build the Docker image for the `my_init` init container with the required modifications to the `main.py` script and push it to a container registry.

2. Update the `vcjob.yaml` file with the correct image name (e.g., `my_init:latest`) for the `my_init` init container.

3. Apply the `vcjob.yaml` file to your Kubernetes cluster:

```
kubectl apply -f vcjob.yaml
```

4. The Volcano scheduler will manage the execution of the job, ensuring that the "master" task runs first, and upon successful completion, the "worker" tasks will proceed.

5. If you uncomment the TODO sections in `main.py` and `vcjob.yaml` and provide appropriate parameters, the `main.py` script and the `my_init` init container will be able to accept and use these parameters during the job execution.

**Note:** Make sure you have the necessary permissions and configurations to run Jobs in your Kubernetes cluster, and that you have set up the Volcano scheduler appropriately for job management.