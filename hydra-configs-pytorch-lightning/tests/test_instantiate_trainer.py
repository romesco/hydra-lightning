# from typing import Any
# import pytest
# from hydra.utils import get_class
# from hydra.utils import instantiate
# from omegaconf import OmegaConf
# @pytest.mark.parametrize(
#    "modulepath, classname, cfg, passthrough_args, passthrough_kwargs, expected",
#    [
#        pytest.param(
#            "nn.modules.loss",
#            "BCELoss",
#            {},
#            [],
#            {"weight": Tensor([1])},
#            loss.BCELoss(),
#            id="BCELossConf",
#        ),
#    ],
# )
# def test_instantiate_classes(
#    modulepath: str,
#    classname: str,
#    cfg: Any,
#    passthrough_args: Any,
#    passthrough_kwargs: Any,
#    expected: Any,
# ) -> None:
#    full_class = f"hydra_configs.torch.{modulepath}.{classname}Conf"
#    schema = OmegaConf.structured(get_class(full_class))
#    cfg = OmegaConf.merge(schema, cfg)
#    obj = instantiate(cfg, *passthrough_args, **passthrough_kwargs)
#
#    assert isinstance(obj, type(expected))


def f():
    return 4


def test_function():
    assert f() == 4
