
# Docker container
## Create and deploy docker container on Azure


1. Create your machine learning model and save it. I have used pickle for this (native to python). Be careful not to mix different versions of pickle (python2 and python3 are incompatible). The docker container default is python 2, so I recommend using that for your model. Otherwise the Dockerfile needs to be configured differently from this guide.
2. Adapt and inser your code into App.py, a general tip is to have as little code as possible in here since it is difficult to debug in this environment.
3. Create dockerhub account
4. Create dockerhub repo (I have used the following structure "docker/app")
5. Create similar folder stucture locally (docker/app/app)
6. CD into the app folder
7. run docker build -t "docker/app:App_v0.1" .
8. run -d -p 5000:5000 docker/app:App_v0.1
9. open browser and go to http://0.0.0.0:5000/ to test your app
10. If everything works, we want to publish the container to dockerhub with the following command: docker push "docker/app:App_v0.1"
11. Go to http://portal.azure.com
12. Click "Create a resource"
13. Search and click "Web app for containers"
14. Go to container settings and input credentials to your dockerhub, and input the path and startup file (App.py)
15. Go to overview and start your Web App.
16. In overview you can find the link to the web app, which will be https://<nameOfApp>.azurewebsites.net
17. Open browser and navigate to your app
