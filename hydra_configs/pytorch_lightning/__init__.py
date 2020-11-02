import sys
from packaging import version
import pytorch_lightning as pl

try:
    if version.parse(pl.__version__) > version.parse("1.0.0"):
        from hydra_configs.pytorch_lightning.trainer import *
        from hydra_configs.pytorch_lightning.callbacks import *
        from hydra_configs.pytorch_lightning.metrics.classification import * 
        from hydra_configs.pytorch_lightning.metrics.regression import * 
    else:
        from hydra_configs.pytorch_lightning_v091 import * 
        from hydra_configs.pytorch_lightning_v091.trainer import * 
        from hydra_configs.pytorch_lightning_v091.callbacks import * 
        from hydra_configs.pytorch_lightning_v091.metrics.classification import * 
        from hydra_configs.pytorch_lightning_v091.metrics.regression import * 
except ImportError as err:
    raise ImportError("Your version of lightning is currently incompatible with the generated hydra configs.")

