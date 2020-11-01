from packaging import version
import pytorch_lightning as pl

try:
    if version.parse(pl.__version__) > version.parse("1.0.0"):
        import hydra_configs.pytorch_lightning
    else:
        from hydra_configs.pytorch_lightning_v091.trainer import * 
except ImportError as err:
    raise ImportError("Your version of lightning is currently incompatible with the generated hydra configs.")

