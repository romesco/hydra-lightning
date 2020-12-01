import hydra
from configen.config import Config
from configen.configen import generate_module, save


@hydra.main(config_name="conf/configen")
def main(cfg: Config):
    print(cfg)
    for module in cfg.configen.modules:
        code = generate_module(cfg=cfg.configen, module=module)
        save(cfg=cfg.configen, module=module.name, code=code)


if __name__ == "__main__":
    main()
