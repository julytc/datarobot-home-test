# Datarobot home test

Github OAuth app which clones code to the users account

# 1. Github OAuth application

 Create a Github OAuth application. Please follow how to below:
 
[creating-an-oauth-app](https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/ "creating-an-oauth-app")

For Homepage URL and Authorization callback URL please use 127.0.0.1 or any other random name for initial set up.

Please save **Client ID** and **Client Secret** for future use. However these values available at any time from the application settings file.

# 2. Application installation

The application requires endpoint which receives GitHub webhooks.

**For local development** you can use tools like smee.io:

[smee](https://smee.io/)

**For production workload** you should have resources to run application container and public ip address exposed to the world(load balancer, proxy or server public ip address). 

In this example we will use GCE resources.

[gce](https://cloud.google.com/compute "gce")

**2.1** First install google cloud sdk, instruction here:

[sdk_installation](https://cloud.google.com/sdk/ "sdk_installation")

** 2.2** Enable goole container registry, in order to store application image:

[gcr](https://cloud.google.com/container-registry/docs/quickstart "gcr")

*In short:*

run from application repository folder:

**2.2.a** 

`gcloud auth configure-docker`

`docker build -t  gcr.io/[PROJECT-ID]/application:1.0 .`

`docker push gcr.io/[PROJECT-ID]/application:1.0 .`

**2.3** Enabe GKE cluster:

[GKE](https://cloud.google.com/kubernetes-engine/docs/quickstart "GKE")

In short:

**2.3.a**

[kubernetes clusters list](https://console.cloud.google.com/kubernetes/list "kubernetes clusters list")

Press "*Create cluster*" button, on left menu select "*your first cluster*", define name and press *create*.

From left menu go to "*workloads page*" press "*deploy*" button, in menu "*image path*" press select menu and select *application:1.0* image from GCR, add required environment variables:

`GITHUB_CLIENT_ID`

`GITHUB_CLIENT_SECRET`

these values were provided by GitHub OAuth application created on the first step. And
`SECRET_KEY`

random value for securing sessions on the application side(Flask framework requirement).

When all environment variables are set, please press* continue*, define application name on next step and press *deploy*. When operation success you will be redirected to the configuration page, in the menu  "*Exposing services*" press expose. You will be promted to define target port, which is **3000**, then press *expose*. When the operation completes you will be given with public ip in section *External endpoints*.

**3.** The last step is to redefine Homepage URL and callback URL in GitHub OAuth settings, please go back to step **1**, edit your OAuth application settings with :

`Homepage URL`

public URL is given on the previous step, for example:

`http://176.35.91.98`

`Authorization callback URL`

same as homepage URL but with the prefix 

`/github-callback`, for example: 

`http://176.35.91.98/github-callback`

**For detailed technical specification please follow**** link: 

[specification doc](https://github.com/julytc/datarobot-home-test/blob/master/docs/specification.md)
