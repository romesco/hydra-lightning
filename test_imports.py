import hydra_configs.pytorch_lightning
from dataclasses import fields

print(fields(hydra_configs.pytorch_lightning.TrainerConf)[0])
