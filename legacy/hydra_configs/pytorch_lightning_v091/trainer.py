# Autogenerated by configen, do not edit.
# If encountering an error, please file an issue @
# https://github.com/romesco/hydra-lightning 
# fmt: off
# isort: skip_file
# flake8: noqa
# Hydra + Lightning:

from dataclasses import dataclass, field
from builtins import list
from omegaconf import MISSING
from typing import Any
from typing import Optional


@dataclass
class TrainerConf:
    _target_: str = "old trainer"
    logger: bool = False  # Union[LightningLoggerBase, Iterable[LightningLoggerBase], bool]
    checkpoint_callback: bool = True  # Union[ModelCheckpoint, bool]
    callbacks: Any = None  # Optional[List[Callback]]
    default_root_dir: Optional[str] = None
    gradient_clip_val: float = 0
    process_position: int = 0
    num_nodes: int = 1
    num_processes: int = 1
    gpus: Any = None  # Union[int, str, List[int], NoneType]
    auto_select_gpus: bool = False
    tpu_cores: Any = None  # Union[int, str, List[int], NoneType]
    log_gpu_memory: Optional[str] = None
    progress_bar_refresh_rate: int = 1
    overfit_batches: float = 0.0  # Union[int, float]
    track_grad_norm: float = -1  # Union[int, float, str]
    check_val_every_n_epoch: int = 1
    fast_dev_run: bool = False
    accumulate_grad_batches: int = 1  # Union[int, Dict[int, int], List[list]]
    max_epochs: int = 1000
    min_epochs: int = 1
    max_steps: Optional[int] = None
    min_steps: Optional[int] = None
    limit_train_batches: float = 1.0 # Union[int, float]
    limit_val_batches: float = 1.0 # Union[int, float]
    limit_test_batches: float = 1.0 # Union[int, float]
    val_check_interval: float = 1.0  # Union[int, float]
    flush_logs_every_n_steps: int = 100
    log_every_n_steps: int = 50
    accelerator: Any = None  # Union[str, Accelerator, NoneType]
    sync_batchnorm: bool = False
    precision: int = 32
    weights_summary: Optional[str] = "top"
    weights_save_path: Optional[str] = None
    num_sanity_val_steps: int = 2
    truncated_bptt_steps: Optional[int] = None
    resume_from_checkpoint: Optional[str] = None
    profiler: Any = None # Union[BaseProfiler, bool, NoneType]
    benchmark: bool = False
    deterministic: bool = False
    reload_dataloaders_every_epoch: bool = False
    auto_lr_find: bool = False # Union[bool, str]
    replace_sampler_ddp: bool = True
    terminate_on_nan: bool = False
    auto_scale_batch_size: bool = False  # Union[str, bool]
    prepare_data_per_node: bool = True
    plugins: Any = None
    amp_backend: str = "native"
    amp_level: str = "O2"
    distributed_backend: Optional[str] = None
    automatic_optimization: bool = True
