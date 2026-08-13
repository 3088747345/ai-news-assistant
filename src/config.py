import yaml


def load_sources():

    with open(
        "config/sources.yaml",
        "r",
        encoding="utf-8"
    ) as f:

        config = yaml.safe_load(f)

    return config.get("sources", [])
