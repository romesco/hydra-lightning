# flake8: noqa
# Original example from: https://github.com/PyTorchLightning/pytorch-lightning/blob/master/pl_examples/basic_examples/mnist.py

import os

import torch
from pytorch_lightning import LightningModule, Trainer
from pytorch_lightning.callbacks import ModelCheckpoint
from torch.utils.data import Dataset

import hydra
from hydra.utils import instantiate
from hydra.core.config_store import ConfigStore
from dataclasses import dataclass, field
from typing import Any, List, Dict
from omegaconf import OmegaConf

# structured config imports
from hydra_configs.torch.optim import SGDConf
from hydra_configs.torch.optim.lr_scheduler import StepLRConf 
from hydra_configs.torch.utils.data.dataloader import DataLoaderConf
from hydra_configs.pytorch_lightning.trainer import TrainerConf
from hydra_configs.pytorch_lightning.callbacks import ModelCheckpointConf

run_dir = "${now:%Y-%m-%d}"

@dataclass
class TopLvlConf:
    hydra: Any = field(default_factory=lambda: {"run": {"dir": run_dir }})
    trainer: TrainerConf = TrainerConf(
        limit_val_batches=1,
        max_epochs=1,
        weights_summary=None,
        accelerator="ddp",
        gpus=2,
        deterministic=True,
        benchmark=False,
        checkpoint_callback=True,
        default_root_dir=os.path.join(os.getcwd(), run_dir),
        callbacks=[ModelCheckpointConf(
            monitor="x",
            mode="max",
            verbose=True,
            save_top_k=1,
            dirpath=".",
        )]
    )
    dataloader: DataLoaderConf = DataLoaderConf(num_workers=12)
    optim: Any = SGDConf(lr=0.1)
    scheduler: Any = StepLRConf(step_size=1)

cs = ConfigStore.instance()
cs.store(name="toplvlconf", node=TopLvlConf)

class RandomDataset(Dataset):
    def __init__(self, size, length):
        self.len = length
        self.data = torch.randn(length, size)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return self.len


class BoringModel(LightningModule):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.layer = torch.nn.Linear(32, 2)

    def forward(self, x):
        return self.layer(x)

    def loss(self, batch, prediction):
        # An arbitrary loss to have a loss that updates the model weights during `Trainer.fit` calls
        return torch.nn.functional.mse_loss(prediction, torch.ones_like(prediction))

    def step(self, x):
        x = self.layer(x)
        out = torch.nn.functional.mse_loss(x, torch.ones_like(x))
        return out

    def training_step(self, batch, batch_idx):
        output = self.layer(batch)
        loss = self.loss(batch, output)
        return {"loss": loss}

    def training_step_end(self, training_step_outputs):
        return training_step_outputs

    def training_epoch_end(self, outputs) -> None:
        torch.stack([x["loss"] for x in outputs]).mean()

    def validation_step(self, batch, batch_idx):
        output = self.layer(batch)
        loss = self.loss(batch, output)
        return {"x": loss}

    def test_step(self, batch, batch_idx):
        output = self.layer(batch)
        loss = self.loss(batch, output)
        return {"y": loss}

    def configure_optimizers(self):
        optimizer = instantiate(self.cfg.optim, params=self.parameters())
        scheduler = instantiate(self.cfg.scheduler, optimizer=optimizer)
        return optimizer 

@hydra.main(config_name="toplvlconf")
def test_run(cfg):
    #print(OmegaConf.to_yaml(cfg))

    class TestModel(BoringModel):
        def on_train_epoch_start(self) -> None:
            print("override any method to prove your bug")

    # fake data
    train_data = instantiate(cfg.dataloader, dataset=RandomDataset(32, 64))
    val_data = instantiate(cfg.dataloader, dataset=RandomDataset(32, 64))
    test_data = instantiate(cfg.dataloader, dataset=RandomDataset(32, 64))

    # model
    model = TestModel(cfg)
    trainer = instantiate(cfg.trainer)
    trainer.fit(model, train_data, val_data)
    trainer.test(test_dataloaders=test_data)


if __name__ == "__main__":
    test_run()
