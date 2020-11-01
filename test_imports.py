from dataclasses import fields

# with pytorch_lightning version = 0.9.0, this uses the 'legacy configs' from
# legacy/hydra_configs/pytorch_lightning_v091/trainer
import hydra_configs.pytorch_lightning
print(fields(hydra_configs.pytorch_lightning.TrainerConf)[0])
# prints old trainer config


# this however, does not
from hydra_configs.pytorch_lightning.trainer import TrainerConf
print(fields(TrainerConf)[0])
# prints new trainer config (we want old)

# this works as expected:
from hydra_configs.pytorch_lightning_v091.trainer import TrainerConf
print(fields(TrainerConf)[0])
# prints old trainer config
