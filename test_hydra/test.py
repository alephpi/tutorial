import hydra


@hydra.main(version_base="1.3", config_path=".", config_name="a.yaml")
def main(cfg):
    print(cfg)
    a_instance = hydra.utils.instantiate(cfg, z=30)
    print(a_instance)

if __name__ == "__main__":
    main()