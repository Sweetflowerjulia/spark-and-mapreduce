#### 1. Run the code on the AWS EMR Notebook. 
Go to EMR console and create cluster.

#### 2. Software configuration
Select EMR - 5.23.0, Hadoop 2.8.5, Spark 2.4.0, Livy 0.5.0, TensorFlow 1.12.0
 
#### 3. Software settings
[{"configurations":[{"classification":"export","properties":{"PYSPARK_PYTHON":"/usr/bin/python3"}}],"classification":"spark-env","properties":{}},{"configurations":[{"classification":"export","properties":{"PYSPARK_PYTHON":"/usr/bin/python3"}}],"classification":"yarn-env","properties":{}},{"classification":"spark","properties":{"maximizeResourceAllocation":"true"}}]

#### 4. Hardware configuration
​    Master Node: m4.2xlarge, 1 instances
​    Core Node: m4.xlarge, 6 instances
​    Task Node: m4.xlarge, 2 instances on demand, 4 instances on spot

#### 5. Bootstrap actions, upload .sh file with below contents
sudo yum -y install git
sudo pip-3.6 install --quiet tensorflow-hub 
sudo pip-3.6 install --quiet numpy
sudo pip-3.6 install --quiet re
sudo pip-3.6 install --quiet scikit-learn
sudo /usr/share/pip-3.6 install nltk
sudo python -m nltk.downloader punkt -d /usr/share/nltk_data

#### 6. Go to Notebook menu to open EMR notebook.

#### 7. Run the code from the first cell.
