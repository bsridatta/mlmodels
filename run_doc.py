# pylint: disable=C0321,C0103,C0301,E1305,E1121,C0302,C0330,C0111,W0613,W0611,R1705
# -*- coding: utf-8 -*-
"""


"""
import io
import os
import subprocess
import sys

from setuptools import find_packages, setup

######################################################################################
root = os.path.abspath(os.path.dirname(__file__))



##### Version  #######################################################################
# from setup import version, entry_points
print("start Doc")



######################################################################################
#with open("README.md", "r") as fh:
#    long_description = fh.read()


#################################################################################################
des1 = """
## In Jupyter 

#### Model, data, ... definition
```python
model_uri    = "model_tf.1_lstm.py"
model_pars   = {  "num_layers": 1,
                  "size": ncol_input, "size_layer": 128, "output_size": ncol_output, "timestep": 4,
                }
data_pars    = {"data_path": "/folder/myfile.csv"  , "data_type": "pandas" }
compute_pars = { "learning_rate": 0.001, }

out_pars     = { "path": "ztest_1lstm/", "model_path" : "ztest_1lstm/model/"}
save_pars    = { "path" : "ztest_1lstm/model/" }
load_pars    = { "path" : "ztest_1lstm/model/" }


```


#### Using local module (which contain the model)
```python

from mlmodels.models import module_load

module        =  module_load( model_uri= model_uri )                           # Load file definition
model         =  module.Model(model_pars, data_pars, compute_pars)             # Create Model instance
model, sess   =  module.fit(model, data_pars, compute_pars, out_pars)          # fit the model
metrics_val   =  module.fit_metrics( model, sess, data_pars, compute_pars, out_pars) # get stats
module.save(model, sess, save_pars)



#### Inference
model, sess = module.load(load_pars)    #Create Model instance
ypred       = module.predict(model, sess,  data_pars, compute_pars, out_pars)     # predict pipeline


```




###### Using Generic API : Common to all models, models.py methods
```python

from mlmodels.models import module_load, create_model, fit, predict, stats
from mlmodels.models import load  # Load model weights

module        =  module_load( model_uri= model_uri )                           # Load file definition
model         =  model_create(module, model_pars, data_pars, compute_pars)     # Create Model instance
model, sess   =  fit(model, data_pars, compute_pars, out_pars)                 # fit the model
metrics_val   =  fit_metrics( model, sess, data_pars, compute_pars, out_pars)  # get stats

save(model, sess, save_pars)



#### Inference
load_pars = { "path" : "ztest_1lstm/model/", "model_type": "model_tf" }

model, sess  = load( load_pars )       # Create Model instance
ypred        = predict(model, module, sess,  data_pars, compute_pars, out_pars)     





```

"""


###############################################################################################
des2= """
## CLI tools: package provide below tools 
```bash
- ml_models
- ml_optim    
- ml_test


```


### How to use tools
```bash
ml_models --do  
    model_list  :  list all models in the repo                            
    testall     :  test all modules inside model_tf
    test        :  test a certain module inside model_tf
    fit         :  wrap fit generic m    ethod
    predict     :  predict  using a pre-trained model and some data
    generate_config  :  generate config file from code source
    
  ## --do fit  
  --model_uri     model_tf.1_lstm
  --save_folder   myfolder/
  --config_file   myfile.json
  --config_mode   "test"


  ## --do predict  
  --load_folder   mymodel_folder/
    "testall"     :  test all modules inside model_tf
    "test"        :  test a certain module inside model_tf


    "model_list"  :  #list all models in the repo          
    "fit"         :  wrap fit generic m    ethod
    "predict"     :  predict  using a pre-trained model and some data
    "generate_config"  :  generate config file from code source


ml_optim --do
    test      :  Test the hyperparameter optimization for a specific model
    test_all  :  TODO, Test all
    search    :  search for the best hyperparameters of a specific model


ml_test
  "search"    :  search for the best hyperparameters of a specific model




### Command line tool sample

#### generate config file
    ml_models  --do generate_config  --model_uri model_tf.1_lstm.py  --save_folder "c:\myconfig\"

#### TensorFlow LSTM model
    ml_models  --model_uri model_tf/1_lstm.py  --do test

#### PyTorch models
    ml_models  --model_uri model_tch/mlp.py  --do test
    
    
#### Custom  Models
    ml_models --do test  --model_uri "D:\_devs\Python01\gitdev\mlmodels\mlmodels\model_tf\1_lstm.py"



#### Model param search test
    ml_optim --do test


#### For normal optimization search method
    ml_optim --do search --ntrials 1  --config_file optim_config.json --optim_method normal
    ml_optim --do search --ntrials 1  --config_file optim_config.json --optim_method prune  ###### for pruning method

    ml_optim --modelname model_tf.1_lstm.py  --do test
    ml_optim --modelname model_tf.1_lstm.py  --do search


```

"""





##########################################################################################
des3 =  """
#### Distributed training on Pytorch Horovod
```
#### Distributed Pytorch on CPU (using Horovod and MPI on Linux, 4 processes)  in model_tch/mlp.py
    mlmodels/distri_torch_mpirun.sh   4    model_tch.mlp    mymodel.json


```

"""


##########################################################################################
### Packages  ####################################################
packages = ["mlmodels"] + ["mlmodels." + p for p in find_packages("mlmodels")]




#########################################################################################
def os_package_root_path(add_path="",n=0):
  from pathlib import Path
  add_path = os.path.join(Path(__file__).parent.absolute(), add_path)
  # print("os_package_root_path,check", add_path)
  return add_path


def get_recursive_files(folderPath, ext='/*model*/*.py'):
  import glob
  files = glob.glob( folderPath + ext, recursive=True) 
  return files


# Get all the model.py into folder  
folder = None
folder = os_package_root_path() if folder is None else folder
# print(folder)
module_names = get_recursive_files(folder, r'/*model*//*model*/*.py' )                       




des = """
#### Model list 

```
--model_uri


"""
for t in module_names :
    t = t.replace(folder, "").replace("\\", ".")

    if "__init__.py" in t  :
      des = des  + "\n\n"
    else  :    
      if  not 'util' in  t and not 'preprocess' in t :
        des = des + str(t) + "\n" 

des = des + """
```

"""

   





#########################################################################################
################ Print on file
with open("README_model_list.md", mode="w") as f :
  f.writelines(des1)
  f.writelines(des2)
  f.writelines(des3)
  f.writelines(des)
