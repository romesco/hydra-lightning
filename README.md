## Quick Start:

```
pip install git+https://github.com/romesco/hydra-lightning/#subdirectory=hydra-configs-pytorch-lightning
```

```python
from hydra_configs.pytorch_lightning.trainer import TrainerConf
```

## What is this?

This is a collection of auto-generated configuration files to enable using [Pytorch Lightning](https://github.com/pytorchlightning/pytorch-lightning) with [Hydra](https://hydra.cc). The emphasis on this repository is to provide a stable set of base configs that track the current versions of Lightning and Hydra. If either changes its API, these configs will update automatically as well.

Here is an example of the base config for the `EarlyStopping` Callback from Pytorch Lightning:

```python
@dataclass
class EarlyStoppingConf:
    _target_: str = "pytorch_lightning.callbacks.EarlyStopping"
    monitor: str = "early_stop_on"
    min_delta: float = 0.0
    patience: int = 3
    verbose: bool = False
    mode: str = "auto"
    strict: bool = True
```

This is useful because it allows you to quickly import these configs like:

```python
from hydra_configs.pytorch_lightning.callbacks import EarlyStoppingConf
```

Now you are free to use this config with its pre-set defaults and override any values programatically using one of:

1. command line args
2. yaml files
3. structured configs (dataclasses)

## Looking for `torch` configs?

If you're interested in configuring Lightning classes, you're probably interested in configuring normal torch classes as well.
Things like:

```python
Adam
LRStep
Linear
Dataset
DataLoader
...
```

Please find those in the pytorch repository:
https://github.com/pytorch/hydra-torch/

## Tutorials

#### Configuring Pytorch with Hydra:

1. [Basic Tutorial](https://github.com/pytorch/hydra-torch/blob/master/examples/mnist_00.md)
2. Intermediate Tutorial (coming soon)
3. Advanced Tutorial (coming soon)

#### Lightning

1. Basic Tutorial (coming soon - for now see [examples/mnist_00.py](examples/mnist_00.py)).
2. Intermediate Tutorial (coming soon)

## Dev Installation

`poetry install`

## Regenerate configs

`poetry run generate-configs`
