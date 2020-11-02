from dataclasses import fields

'''
all of these examples are run using the deprecated, pytorch_lightning version = 0.9.0
-> expected functionality is to use the 'legacy configs' from legacy/hydra_configs/pytorch_lightning_v091/trainer
'''

########### this works as expected. up-to-date gets 'main', out-of-date gets 'legacy'
import hydra_configs.pytorch_lightning
print(fields(hydra_configs.pytorch_lightning.TrainerConf)[0])
print(fields(hydra_configs.pytorch_lightning.EarlyStoppingConf)[0])
print(fields(hydra_configs.pytorch_lightning.AccuracyConf)[0])

############ this also works as expected
#from hydra_configs.pytorch_lightning_v091.trainer import TrainerConf
#print(fields(TrainerConf)[0])

############ we have yet to make this work properly:
#from hydra_configs.pytorch_lightning.trainer import TrainerConf
#print(fields(TrainerConf)[0])
############ prints new trainer config (we want old)
