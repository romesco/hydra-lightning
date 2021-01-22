from typing import Any

import pytest
import pytorch_lightning as pl
from hydra.utils import get_class
from hydra.utils import instantiate
from omegaconf import OmegaConf


@pytest.mark.parametrize(
    "modulepath, classname, cfg, passthrough_args, passthrough_kwargs, expected",
    [
        pytest.param(
            "metrics.regression",
            "ExplainedVariance",
            {},
            [],
            {},
            pl.metrics.regression.ExplainedVariance(),
            id="ExplainedVarianceConf",
        ),
        pytest.param(
            "metrics.regression",
            "MeanAbsoluteError",
            {},
            [],
            {},
            pl.metrics.regression.MeanAbsoluteError(),
            id="MeanAbsoluteErrorConf",
        ),
        pytest.param(
            "metrics.regression",
            "MeanSquaredLogError",
            {},
            [],
            {},
            pl.metrics.regression.MeanSquaredLogError(),
            id="MeanSquaredLogErrorConf",
        ),
    ],
)
def test_instantiate_classes(
    modulepath: str,
    classname: str,
    cfg: Any,
    passthrough_args: Any,
    passthrough_kwargs: Any,
    expected: Any,
) -> None:
    full_class = f"hydra_configs.pytorch_lightning.{modulepath}.{classname}Conf"
    schema = OmegaConf.structured(get_class(full_class))
    cfg = OmegaConf.merge(schema, cfg)
    obj = instantiate(cfg, *passthrough_args, **passthrough_kwargs)
    assert isinstance(obj, type(expected))
